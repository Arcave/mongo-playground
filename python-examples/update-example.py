from client import collection

document = {"hello": "test"}

query = document

newdocument = { "hello": "test2" }

setdocument = { "$set": newdocument }

collection.update_one(query, setdocument)

results = collection.find(newdocument)

for item in results:
  print(item)