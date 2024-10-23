#!/usr/bin/env python3
""" Updating the topics """


from typing import List


def update_topics(mongo_collection: object, name: str, topics: List[str]):
    """Changing all topics for a school document based on the name

    Args:
        mongo_collection (object): [description]
        name (str): [description]
        topics (List[str]): [description]
    """
    data = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return data.modified_count
