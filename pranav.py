import pymongo, json
import pandas as pd
from bson.objectid import ObjectId


my_client = pymongo.MongoClient('mongodb+srv://xdhacks:applebanana@cluster0.s06sf.mongodb.net/xdhacks?retryWrites=true&w=majority')
my_db = my_client['xdhacks']
my_col = my_db['data']
patient = my_col.find_one({'_id': str(id)})
entries = list(patient)
print(patient)
