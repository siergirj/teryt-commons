import yaml
from pymongo import MongoClient
from utils import config

# read configuration
cfg = config()

# open DB connection
mongo = MongoClient(cfg['mongo']['host'], cfg['mongo']['port'])
db = mongo.teryt


# functions to manipulate district collection
class DistrictDAO:
    
    # get all
    def find_all(self):
        cursor = db.district.find()
        result = []
        for c in cursor:
            data = {}
            data['id'] = c['id']
            data['name'] = c['name']
            data['type'] = c['type']
            data['href'] = 'asdasdasda'
            result.append(data)
        return result
    
    # save city
    def save(self, id, name, type, timestamp):
        return db.district.insert_one(
                {
                    "id" : id,
                    "name" : name,
                    "type" : type,
                    "timestamp": timestamp
                }
            )
        
    def truncate(self):
        db.district.drop()