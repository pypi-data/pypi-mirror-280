# Shops Package

Provides data about shops in a given location, based on OpenStreetMap data.

Remember about license, see [https://www.openstreetmap.org/copyright](https://www.openstreetmap.org/copyright)

```
import shops
import os

# data from https://download.geofabrik.de/europe/andorra.html
# you can try north-america/us code standing for
# https://download.geofabrik.de/north-america/us.html
# but in such case you should expect much longer processing
location_code = "europe/andorra"
# pernament location is better, this is used in example as it likely to exist on almost any Linux
path_processing_directory = "/tmp/ATP"
os.mkdir(path_processing_directory)
for entry in shops.osm.list_shops(location_code, path_processing_directory):
    print(entry)
```

# Installation

`pip install shops`

It is uploaded to [pypi.org](https://pypi.org/project/shops/)

# Behind scenes

Data is downloaded, preprocessed and output cached within specified folder.

First run will take long time especially for longer datasets.

# Run tests

```
python3 -m unittest
```

# Contributions

Bug reports, benchmarks, ideas, pull requests, suggestions and maybe thanks are welcome on the issue tracker!

I am especially looking for ways to make this code faster.

Note that for larger code changes opening issue first, before sending patch, may be a good idea.
