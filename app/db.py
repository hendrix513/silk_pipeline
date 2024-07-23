import numpy as np
from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017/')
db = client.db
collection = db.hosts


async def write_to_db(df):
    collection.delete_many({})
    row_dicts = [{k: v for k, v in row.items() if not (isinstance(v, float) and np.isnan(v))} for _, row in df.iterrows()]
    collection.insert_many(row_dicts)

