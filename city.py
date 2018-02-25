from pymongo import MongoClient
import yaml

# read configuration
with open("./config.yaml", 'r') as config:
    cfg = yaml.load(config)

# open DB connection
mongo = MongoClient(cfg['mongo']['host'], cfg['mongo']['port'])
db = mongo.teryt

#functions to manipulate city collection
class CityDAO:
    
    # get all
    def findAll(self):
        cursor = db.city.find()
        result = []
        for c in cursor:
            data = {}
            data['id'] = c['id']
            data['name'] = c['name']
            data['href'] = 'asdasdasda'
            result.append(data)
        return result
    
    # save city
    def save(self, id, province_id, name, timestamp):
        return db.city.insert_one(
                {
                    "id" : id,
                    "province_id" : province_id,
                    "name" : name,
                    "timestamp": timestamp
                }
            )
        
    def truncate(self):
        db.city.drop()

# data['province_id'] = c['province_id']
            # data['timestamp'] = c['timestamp']        
