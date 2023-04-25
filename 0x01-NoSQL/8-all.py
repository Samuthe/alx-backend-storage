# Write a Python function that lists all documents in a collection:

#     Prototype: def list_all(mongo_collection):
#     Return an empty list if no document in the collection
#     mongo_collection will be the pymongo collection object

import pymongo


def list_all(mongo_collection):
    '''
    print all lists
    '''
    details = mongo_collection.find()
    if details:
        return [values for values in details]
    else:
        return []
    
    