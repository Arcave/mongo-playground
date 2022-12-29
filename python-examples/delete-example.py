from client import collection

document = {"hello": "test2"}

result = collection.delete_many(document)

print(result.deleted_count, " documents deleted.")