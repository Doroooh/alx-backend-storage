#!/usr/bin/env python3
""" MongoDB Document Insertion """

def add_document(collection: object, **document_data):
    """Inserts a new document into the given MongoDB collection using keyword arguments.

    Args:
        collection (object): The pymongo collection instance where the document will be inserted.
        document_data: Arbitrary keyword arguments representing the document fields and values.

    Returns:
        The ID of the inserted document.
    """
    inserted = collection.insert_one({**document_data})
    return inserted.inserted_id
