#!/usr/bin/env python3
"""
Module that updates the topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name (str): school name to match
        topics (list of str): list of new topics
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )

