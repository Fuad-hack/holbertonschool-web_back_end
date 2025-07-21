#!/usr/bin/env python3
""" Task - 8 """

def list_all(mongo_collection):
    """
    Lists all documents in a collection
    Args:
        mongo_collection: pymongo collection object
    Returns:
        List of documents, or empty list if no document exists
    """
    return list(mongo_collection.find())

