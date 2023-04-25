def validate_email_payload(payload):
    # Validate sender name
    sender_name = payload.get('sender_name')
    if not sender_name:
        raise ValueError("Sender name is required.")
    if not (5 <= len(sender_name.strip()) <= 30):
        raise ValueError("Sender name should be between 5 and 30 characters.")

    # Validate sender email address
    sender_addr = payload.get('sender_addr')
    if not sender_addr:
        raise ValueError("Sender address is required.")
    if not (6 <= len(sender_addr) <= 254):
        raise ValueError("Sender address length should be between 6 and 254 bytes.")
    if sender_addr.count('@') != 1:
        raise ValueError("Sender address should contain exactly one '@' character.")
    local, domain = sender_addr.split('@')
    if len(local) > 64:
        raise ValueError("Local part of sender address should be no longer than 64 bytes.")
    if len(domain) > 251:
        raise ValueError("Domain part of sender address should be no longer than 251 bytes.")
    if not all(c.isalnum() or c in ['_', '.', '+', '-'] for c in local):
        raise ValueError("Sender address contains invalid characters.")

    # Validate receiver name
    receiver_name = payload.get('receiver_name')
    if not receiver_name:
        raise ValueError("Receiver name is required.")
    if not (5 <= len(receiver_name.strip()) <= 60):
        raise ValueError("Receiver name should be between 5 and 60 characters.")

    # Validate receiver email address
    receiver_addr = payload.get('receiver_address')
    if not receiver_addr:
        raise ValueError("Receiver address is required.")
    if not (6 <= len(receiver_addr) <= 254):
        raise ValueError("Receiver address length should be between 6 and 254 bytes.")
    if receiver_addr.count('@') != 1:
        raise ValueError("Receiver address should contain exactly one '@' character.")
    local, domain = receiver_addr.split('@')
    if len(local) > 64:
        raise ValueError("Local part of receiver address should be no longer than 64 bytes.")
    if len(domain) > 251:
        raise ValueError("Domain part of receiver address should be no longer than 251 bytes.")
    if not all(c.isalnum() or c in ['_', '.', '+', '-'] for c in local):
        raise ValueError("Receiver address contains invalid characters.")

    # Validate HTML body
    html = payload.get('html')
    if not html:
        raise ValueError("HTML body is required.")

    # Validate replacements dictionary
    replacements = payload.get('replacements')
    if not isinstance(replacements, dict):
        raise ValueError("Replacements should be a dictionary.")
    if not all(key in payload for key in ['sender_name', 'sender_addr', 'receiver_name', 'receiver_address', 'html', 'replacements']):
        raise ValueError('Missing required parameter')

    # Validate sender and receiver names
    sender_name = payload['sender_name'].strip()
    if not (5 <= len(sender_name) <= 30):
        raise ValueError('Invalid sender name')
    
    receiver_name = payload['receiver_name'].strip()
    if not (5 <= len(receiver_name) <= 60):
        raise ValueError('Invalid receiver name')

    # Validate sender and receiver email addresses
    sender_addr = payload['sender_addr'].strip()
    receiver_addr = payload['receiver_address'].strip()
    valid_tlds = ('.com', '.net', '.org')

    for addr in (sender_addr, receiver_addr):
        if len(addr) > 254:
            raise ValueError('Invalid email address')

        parts = addr.split('@')
        if len(parts) != 2:
            raise ValueError('Invalid email address')

        local_part, domain_part = parts
        if not (1 <= len(local_part) <= 64 and 1 <= len(domain_part) <= 251):
            raise ValueError('Invalid email address')

        # if local_part[0] == '.' or local_part[-]

    # If all validations pass, return True
    return True








# #!/usr/bin/env python3

# # Improve 12-log_stats.py by adding the top 10 of the
# # most present IPs in the collection nginx of the database logs:
# # The IPs top must be sorted (like the example below)


# """
# Aggregation operations
# """
# from pymongo import MongoClient
# from collections import OrderedDict
# from typing import Tuple


# def get_nginx_stats() -> Tuple:
#     """
#     Queries nginx collection for specific data
#     - Returns:
#         - count of all documents
#         - count of each method in the collection
#         - count of each GET calls to /status path
#         - count of top 10 visited ips
#     """
#     client: MongoClient = MongoClient()
#     db = client.logs
#     collection = db.nginx
#     methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
#     method_stats = []
#     for method in methods:
#         method_count = collection.count_documents({'method': method})
#         method_stats.append({'method': method, 'count': method_count})
#     doc_count = collection.estimated_document_count()
#     status_path_stats = collection.count_documents({'method': 'GET',
#                                                     'path': '/status'})
#     pipeline = [{'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
#                 {'$sort': OrderedDict([('count', -1)])},
#                 {'$limit': 10}]
#     top_ips = collection.aggregate(pipeline)
#     client.close()
#     return doc_count, method_stats, status_path_stats, top_ips


# def print_nginx_stats() -> None:
#     """
#     Prints stats from nginx query
#     """
#     doc_count, method_stats, status_path_stats, top_ips = get_nginx_stats()
#     print(f'{doc_count} logs')
#     print('Methods:')
#     for method in method_stats:
#         print(f'\tmethod {method.get("method")}: {method.get("count")}')
#     print(f'{status_path_stats} status check')
#     print('IPs:')
#     for ip in top_ips:
#         print(f'\t{ip.get("_id")}: {ip.get("count")}')


# if __name__ == '__main__':
#     print_nginx_stats()
