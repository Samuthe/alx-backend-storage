#Write a Python function that returns all students sorted by average score:

#Prototype: def top_students(mongo_collection):
#mongo_collection will be the pymongo collection object
#The top must be ordered
#The average score must be part of each item returns with key = averageScore

#!/usr/bin/env python3
"""
Aggregation operations: average
"""
from collections import OrderedDict


def top_students(mongo_collection):
    """
    Gets list of students from mongo collection
    and returns the list of computed average for
    each student
    """
    pipeline = [{'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
                {'$sort': OrderedDict([('averageScore', -1), ('name', 1)])}]
    return mongo_collection.aggregate(pipeline)

