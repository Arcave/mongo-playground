document = {
    "field1": "123",
    "field2": "123",
    "field3": "123",
}

def create_new_document(value):
    new_document = document
    new_document['field3'] = value
    return new_document