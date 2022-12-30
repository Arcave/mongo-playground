from pathlib import Path
import json
from client import collection

for path in Path('json-files').rglob('*.json'):
    file = open('json-files/'+path.name, "r")
    json_object = json.load(file)
    result = collection.insert_one(json_object)
    file.close()