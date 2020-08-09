import pymongo, json



my_client = pymongo.MongoClient('mongodb+srv://xdhacks:applebanana@cluster0.s06sf.mongodb.net/xdhacks?retryWrites=true&w=majority')
my_db = my_client['xdhacks']
my_col = my_db['data']
patient = my_col.find({}, {'_id': '5f2f1e3d218e81e41faf62d4'}).limit(1)
print(patient[0])
