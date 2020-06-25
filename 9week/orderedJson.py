import json
from collections import OrderedDict

with open("customer.json") as json_file:
    data = json.load(json_file, object_pairs_hook=OrderedDict)

print(data)