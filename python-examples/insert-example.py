from client import collection
from example import create_new_document

document = create_new_document("world")

result = collection.insert_one(document)

print(result.inserted_id)