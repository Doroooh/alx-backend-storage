#!/usr/bin/env python3
""" Nginx Log Statistics """
from pymongo import MongoClient

def display_log_stats():
    """Displaying the statistics from the Nginx log collection stored in MongoDB."""
    db_client = MongoClient('mongodb://127.0.0.1:27017')
    log_data = db_client.logs.nginx

    total_logs = log_data.count_documents({})
    print(f'Total log entries: {total_logs}')

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Request Methods Count:')
    for method in http_methods:
        method_count = log_data.count_documents({"method": method})
        print(f'\t{method}: {method_count}')

    status_path_count = log_data.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'Status path access count: {status_path_count}')

if __name__ == "__main__":
    display_log_stats()
