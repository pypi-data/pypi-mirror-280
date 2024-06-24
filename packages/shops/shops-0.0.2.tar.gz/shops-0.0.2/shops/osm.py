import osm_bot_abstraction_layer.util_download_file
import osm_bot_abstraction_layer.tag_knowledge as tag_knowledge
import os
import os.path
import osmium
import csv
import json
import base64
from pathlib import Path

# TODO: something to manage dates?
# to allow clearing on request?
# maybe something to get age of when file was obtained?

def _download_and_process(location_code, path_processing_directory):
    """
    this will obtain Geofabrik extract and process it to make it ready to list data
    note that this can take some time (TODO: give estimate)
    path_processing_directory should point to directory where script will be able to delete, create and modify file and folders - space usage can be significant there (depending on processed area, TODO: give estimate) and faster drive will make processing faster
    
    location_code will be used to download data from Geofabrik
    downloaded file are from https://download.geofabrik.de/ (thanks for making this available, go buy their services if you need them!)

    for example https://download.geofabrik.de/europe/poland/malopolskie.html would have code
    europe/poland/malopolskie
    (TODO: maybe allow passing entire url like this?)
    """
    if path_processing_directory.is_dir() == False:
        raise Exception(path_processing_directory, "is not directory!")

    directory_path = downloaded_pbf_file_directory(path_processing_directory)
    if directory_path.is_dir() == False:
        directory_path.mkdir(parents=True)
    download_url = "https://download.geofabrik.de/" + location_code + "-latest.osm.pbf"
    filename = downloaded_pbf_file_name(location_code)
    osm_bot_abstraction_layer.util_download_file.download_file_if_not_present_already(download_url, str(directory_path), filename)
    pbf_file_filepath = downloaded_pbf_file_filepath(location_code, path_processing_directory)
    nodecache_file_filepath = pbf_nodecache_file_filepath(location_code, path_processing_directory)
    if os.path.isfile(nodecache_file_filepath) == False:
        create_osmium_nodecache(pbf_file_filepath, nodecache_file_filepath)

def create_osmium_nodecache(pbf_file_filepath, nodecache_file_filepath):
    print("building nodecache")
    # https://github.com/osmcode/pyosmium/blob/v3.7.0/examples/create_nodecache.py
    # https://github.com/osmcode/pyosmium/blob/v3.7.0/examples/use_nodecache.py
    # https://docs.osmcode.org/pyosmium/latest/intro.html#handling-geometries
    reader = osmium.io.Reader(str(pbf_file_filepath), osmium.osm.osm_entity_bits.NODE)

    idx = osmium.index.create_map("sparse_file_array," + str(nodecache_file_filepath))
    lh = osmium.NodeLocationsForWays(idx)

    osmium.apply(reader, lh)

    reader.close()
    print("building nodecache completed")

def pbf_nodecache_file_filepath(location_code, path_processing_directory):
    return downloaded_pbf_file_filepath(location_code, path_processing_directory).with_suffix(".pbf.nodecache")

def downloaded_pbf_file_filepath(location_code, path_processing_directory):
    return downloaded_pbf_file_directory(path_processing_directory) / downloaded_pbf_file_name(location_code)

def downloaded_pbf_file_directory(path_processing_directory):
    return path_processing_directory / "geofabrik_downloads"

def downloaded_pbf_file_name(location_code):
    return location_code.replace("/", "-") + ".osm.pbf"

def is_shoplike_based_on_this_tag_group(tags_dict):
    """
    broad shop definition, vending machine qualifies as shop here
    """
    # TODO: what about shop=no?
    # TODO: what about shop=vacant?
    # TODO: what about prefixed ones like dissued:shop=yes?
    
    # TODO: move upstream, release a new version of osm_bot_abstraction_layer.tag_knowledge
    # TODO: and of file downloader for that matter
    if len(tags_dict) == 0:
        return False
    if tags_dict.get("office") == "yes":
        return True
    if tags_dict.get("shop") == "yes":
        return True
    if tags_dict.get("shop") == "vacant":
        return True
    for important_main_key in ['amenity', 'shop', 'craft', 'office', 'leisure', 'healthcare']:
        if tags_dict.get(important_main_key) != None:
            # TODO reduce costs of this checks, several functions calls there are NOT needed
            # maybe cache it? build tag filter and make tag filter builder cachable?
            return tag_knowledge.is_shoplike(tags_dict)
    return False # no need for expensive checks

def get_way_center(way, nodeindex):
    osmium_coordinate_precision = 10_000_000
    max_lat = -90 * osmium_coordinate_precision
    max_lon = -180 * osmium_coordinate_precision
    min_lat = 90 * osmium_coordinate_precision
    min_lon = 180 * osmium_coordinate_precision
    for n in way.nodes:
        loc = nodeindex.get(n.ref) # note that cache is used here
        if max_lat < loc.y:
            max_lat = loc.y
        if min_lat > loc.y:
            min_lat = loc.y
        if max_lon < loc.x:
            max_lon = loc.x
        if min_lon > loc.x:
            min_lon = loc.x
    # Coordinates are stored as 32 bit signed integers after multiplying the coordinates 
    #with osmium::coordinate_precision = 10,000,000. This means we can store coordinates 
    # with a resolution of better than one centimeter, good enough for OSM use. 
    # The main OSM database uses the same system.
    # We do this to save memory, a 32 bit integer uses only 4 bytes, a double uses 8.
    # https://osmcode.org/libosmium/manual.html
    return ((max_lon + min_lon)/2/osmium_coordinate_precision, (max_lat + min_lat)/2/osmium_coordinate_precision)

def get_relation_center(relation, ways_location_cache):
    max_lat = -90
    max_lon = -180
    min_lat = 90
    min_lon = 180
    for member in relation.members:
        if member.type == "w":
            if member.ref in ways_location_cache:
                lon = ways_location_cache[member.ref][0]
                lat = ways_location_cache[member.ref][1]
                if max_lat < lat:
                    max_lat = lat
                if min_lat > lat:
                    min_lat = lat
                if max_lon < lon:
                    max_lon = lon
                if min_lon > lon:
                    min_lon = lon
    return ((max_lon + min_lon)/2, (max_lat + min_lat)/2)

def relation_size_limit():
    """
    exists to prevent processing crashing just because someone add bad shop tag or office tag
    to some outsized relation with thousands of elements or worse
    """
    # https://www.openstreetmap.org/relation/3321177 (possibly valid, but a poor idea at best!)
    # https://www.openstreetmap.org/note/4301459 (about seemingly invalid)
    return 200

def list_shops(location_code, path_processing_directory):
    # based on https://github.com/osmcode/pyosmium/tree/v3.7.0/examples
    # https://docs.osmcode.org/pyosmium/latest/intro.html#collecting-data-from-an-osm-file
    # https://docs.osmcode.org/pyosmium/latest/intro.html#handling-geometries
    # https://docs.osmcode.org/pyosmium/latest/intro.html#interfacing-with-shapely
    # https://github.com/osmcode/pyosmium/blob/master/examples/use_nodecache.py

    path_processing_directory = Path(path_processing_directory) # TODO should we expect path object to be passed?

    _download_and_process(location_code, path_processing_directory)
    osm_file = downloaded_pbf_file_filepath(location_code, path_processing_directory)

    class WaysCollectorHandler(osmium.SimpleHandler):
        """
        collect ways that are needed for building relation geometries
        """
        def __init__(self):
            super(WaysCollectorHandler, self).__init__()
            self.ways_needed_by_relations = {}
            self.relation_counter = 0

        def relation(self, o):
            if is_shoplike_based_on_this_tag_group(o.tags) == False:
                return
            if o.tags.get('type') != 'multipolygon':
                return
            self.relation_counter += 1
            if len(o.members) > relation_size_limit():
                print("https://www.openstreetmap.org/relation/" + str(o.id), "relation is overly complex,", len(o.members), "members, skipping it")
                return
            for member in o.members:
                if member.type == "w":
                    self.ways_needed_by_relations[member.ref] = None

    class CollectorHandler(osmium.SimpleHandler):
        """
        collect and record shop locations
        """
        def __init__(self, idx, ways_needed_by_relations):
            """
            ways_needed_by_relations is cache of way locations, created by WaysCollectorHandler
            """
            super(CollectorHandler, self).__init__()
            self.idx = idx
            self.ways_needed_by_relations = ways_needed_by_relations
            self.ways_needed_by_relations_set_for_quick_check = set(ways_needed_by_relations)

        def node(self, o):
            if is_shoplike_based_on_this_tag_group(o.tags):
                csv_shops_file_writer.writerow([o.location.lat, o.location.lon, encode_dict_to_base64(dict(o.tags)), "https://www.openstreetmap.org/node/" + str(o.id)])

        def way(self, o):
            if is_shoplike_based_on_this_tag_group(o.tags): # would crash if code would be reached
                center = get_way_center(o, self.idx)
                csv_shops_file_writer.writerow([center[1], center[0], encode_dict_to_base64(dict(o.tags)), "https://www.openstreetmap.org/way/" + str(o.id)])
            if o.id in self.ways_needed_by_relations_set_for_quick_check:
                self.ways_needed_by_relations[o.id] = get_way_center(o, self.idx)
                #print("center of way", o.id, "calculated as requested")

        def relation(self, o):
            if is_shoplike_based_on_this_tag_group(o.tags): # would crash if code would be reached
                if o.tags.get('type') != 'multipolygon':
                    return
                if len(o.members) > relation_size_limit():
                    print("https://www.openstreetmap.org/relation/" + str(o.id), "relation is overly complex,", len(o.members), "members, skipping it")
                center = get_relation_center(o, self.ways_needed_by_relations)
                csv_shops_file_writer.writerow([center[1], center[0], encode_dict_to_base64(dict(o.tags)), "https://www.openstreetmap.org/relation/" + str(o.id)])

    response_store_filepath = path_processing_directory / ("shop_listing_" + location_code.replace("/", "-") + ".csv")
    response_success_marker_filepath = path_processing_directory / ("shop_listing_" + location_code.replace("/", "-") + ".csv.success")
    if response_success_marker_filepath.is_file() != True or response_success_marker_filepath.is_file() != True:
        clear_files(response_store_filepath, response_success_marker_filepath)
        print("generation of", response_store_filepath, "started")
        w = WaysCollectorHandler()
        w.apply_file(osm_file)
        print(w.relation_counter, "relations", len(w.ways_needed_by_relations), 'ways in relations')

        with open(response_store_filepath, "w") as myfile:
            csv_shops_file_writer = csv.writer(myfile)
            csv_shops_file_writer.writerow(["lat", "lon", "osm_tags_dict_in_base64", "osm_link"])
            idx = osmium.index.create_map("sparse_file_array," + str(pbf_nodecache_file_filepath(location_code, path_processing_directory)))
            h = CollectorHandler(idx, w.ways_needed_by_relations)
            h.apply_file(osm_file)
        with open(response_success_marker_filepath, "w") as myfile:
            myfile.write("run completed")
    for entry in load_and_yield_data_from_file(response_store_filepath):
        yield entry

def load_and_yield_data_from_file(response_store_filepath):
    with open(response_store_filepath) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        for row in reader:
            yield {"tags": decode_base64_to_dict(row[2]), "center": {'lat': float(row[0]), 'lon': float(row[1])}, "osm_link": row[3]}

def clear_files(response_store_filepath, response_success_marker_filepath):
    if response_store_filepath.is_file():
        response_store_filepath.unlink() #=remove =delete
    if response_success_marker_filepath.is_file():
        response_success_marker_filepath.unlink() #=remove =delete

#gptchat generated
def encode_dict_to_base64(input_dict):
    # Convert the dictionary to a JSON string
    json_str = json.dumps(input_dict)
    # Encode the JSON string to bytes
    json_bytes = json_str.encode('utf-8')
    # Encode the bytes to a Base64 string
    base64_bytes = base64.b64encode(json_bytes)
    # Convert Base64 bytes to a string
    base64_str = base64_bytes.decode('utf-8')
    return base64_str

#gptchat generated
def decode_base64_to_dict(base64_str):
    # Decode the Base64 string to bytes
    base64_bytes = base64_str.encode('utf-8')
    # Decode the bytes to a JSON string
    json_bytes = base64.b64decode(base64_bytes)
    # Convert the JSON bytes to a string
    json_str = json_bytes.decode('utf-8')
    # Convert the JSON string to a dictionary
    output_dict = json.loads(json_str)
    return output_dict
