from client import collection

document = {"hello": "test"}

result = collection.insert_one(document)

print(result.inserted_id)