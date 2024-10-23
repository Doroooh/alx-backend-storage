#!/usr/bin/env python3
""" Log analysis - enhanced version """
from pymongo import MongoClient

def log_summary():
    """Displaying the summary of log data including the method counts and the top 10 IPs from the nginx collection in the logs database."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx

    total_logs = log_collection.count_documents({})
    print(f'Total log entries: {total_logs}')

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('HTTP Methods Count:')
    for method in http_methods:
        method_count = log_collection.count_documents({"method": method})
        print(f'\tMethod {method}: {method_count}')

    status_check_count = log_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'Status check logs: {status_check_count}')

    top_ip_addresses = log_collection.aggregate([
        {"$group": {"_id": "$ip", "occurrences": {"$sum": 1}}},
        {"$sort": {"occurrences": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "ip_address": "$_id", "occurrences": 1}}
    ])

    print("Top 10 IP Addresses:")
    for entry in top_ip_addresses:
        ip_address = entry.get("ip_address")
        occurrence = entry.get("occurrences")
        print(f'\t{ip_address}: {occurrence}')

if __name__ == "__main__":
    log_summary()
