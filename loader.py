import csv
import yaml
from datetime import datetime
from pymongo import MongoClient
from city import CityDAO
from province import ProvinceDAO
from utils import config

# read configuration
cfg = config()

# DAO to manipulate collections
c = CityDAO()
p = ProvinceDAO()

 
# drop all collections before load 
def refresh():
    if cfg['mongo']['refresh']: 
        c.truncate()
        p.truncate()


# load TERC collections
def load_terc():
    # Load csv file
    with open(cfg['terc']['path']) as file:
        # read & skip headers
        r = csv.reader(file, delimiter=';')
        r.next()
        
        for row in r:
            if row:  # row not empty
                if row[5] == cfg['terc']['type']['city']:  # if row represents city
                    c.save ('test_id', row[0], row[4], datetime.strptime(row[6], "%Y-%m-%d"))
                elif row[5] == cfg['terc']['type']['commune']:
                    print('asd')    
                elif row[5] == cfg['terc']['type']['province']:  
                    print('asd')
                elif row[5] == cfg['terc']['type']['county']:        
                    print('asd')


def main():
    # drop all collections before load 
    refresh()

    # load TERC collections
    load_terc()


if __name__ == "__main__":
    main()        
