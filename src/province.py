import yaml
from pymongo import MongoClient
from utils import config

# read configuration
cfg = config()

# open DB connection
mongo = MongoClient(cfg['mongo']['host'], cfg['mongo']['port'])
db = mongo.teryt


# functions to manipulate province collection
class ProvinceDAO:
    
    # get all
    def find_all(self):
        cursor = db.province.find()
        result = []
        for c in cursor:
            data = {}
            data['id'] = c['id']
            data['name'] = c['name']
            data['href'] = 'asdasdasda'
            result.append(data)
        return result
    
    # save city
    def save(self, id, name, timestamp):
        return db.province.insert_one(
                {
                    "id" : id,
                    "name" : name,
                    "timestamp": timestamp
                }
            )
        
    def truncate(self):
        db.province.drop()
