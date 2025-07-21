#!/usr/bin/env python3
# Task - 8

from pymongo import MongoClient
list_all = __import__('8-all').list_all

client = MongoClient('mongodb://127.0.0.1:27017')
school_collection = client.my_db.school
schools = list_all(school_collection)
for school in schools:
    print("[{}] {}".format(school.get('_id'), school.get('name')))

