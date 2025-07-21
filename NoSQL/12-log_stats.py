#!/usr/bin/env python3
""" MongoDB Nginx log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total number of logs
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count status checks
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
