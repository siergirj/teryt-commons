import yaml
from datetime import datetime
from pymongo import MongoClient
from utils import config

# read configuration
cfg = config()

# open DB connection
mongo = MongoClient(cfg['mongo']['host'], cfg['mongo']['port'])
db = mongo.teryt


# functions to manipulate county collection
class CountyDAO:
    
    # get all
    def find_all(self):
        cursor = db.county.find()
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
        return db.county.insert_one(
                {
                    "id" : id,
                    "name" : name,
                    "timestamp": datetime.strptime(timestamp, "%Y-%m-%d")
                }
            )
        
    def truncate(self):
        db.county.drop()