#!/usr/bin/env python3
""" The MongoDB Operations with the Python using pymongo """


from typing import List


def schools_by_topic(mongo_collection: object, topic: str) -> List:
    """ The Python function to return list of
    school having a specific topic """
    data = mongo_collection.find({"topics": topic})
    list_doc = [d for d in data]
    return list_doc
