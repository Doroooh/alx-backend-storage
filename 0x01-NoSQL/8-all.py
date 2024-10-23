#!/usr/bin/env python3
""" MongoDB Document Lister """

def fetch_all_documents(collection: object) -> list:
    """Fetching all documents from a specified MongoDB collection.

    Args:
        collection (object): 
        The pymongo collection instance to query from.

    Returns:
        list: A list of all documents in the collection, or an empty list if no documents are found.
    """
    documents = collection.find({})
    return list(documents) if documents else []
