import csv
import yaml
from datetime import datetime
from pymongo import MongoClient
from city import CityDAO

# read configuration
with open("config.yaml", 'r') as config:
    cfg = yaml.load(config)

# DAO to manipulate city collection
c = CityDAO()

# Load TERC
with open(cfg['terc']['path']) as file:
    # read & skip headers
    r = csv.reader(file, delimiter=';')
    r.next()
    
    # drop all cities from collection 
    if cfg['drop']:
        c.truncate()

    i = 1    
    # load cities
    for row in r:
        if row and row[5] == cfg['terc']['type']['city']:
            c.save (i, row[0], row[4], datetime.strptime(row[6], "%Y-%m-%d"))
            i = i + 1
