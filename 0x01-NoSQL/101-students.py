#!/usr/bin/env python3
""" The Top students """


def top_students(mongo_collection: object):
    """function to return all the students, sorting by the average score"""

    top = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top
