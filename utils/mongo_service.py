import csv

from dao.city import CityDAO
from dao.province import ProvinceDAO
from dao.county import CountyDAO
from dao.commune import CommuneDAO
from dao.district import DistrictDAO
from dao.village import VillageDAO
from dao.utils import config

# read configuration
cfg = config()


# DAO to manipulate collections
city = CityDAO()
province = ProvinceDAO()
commune = CommuneDAO()
county = CountyDAO()
district = DistrictDAO()
village = VillageDAO()



# drop all collections before load 
def refresh():
    if cfg['mongo']['refresh']: 
        city.truncate()
        province.truncate()
        commune.truncate()
        county.truncate()
        district.truncate()
        village.truncate()


# load TERC collections
def load_terc():
    # Load csv file
    with open(cfg['terc']['path']) as file:
        # read & skip headers
        r = csv.reader(file, delimiter=';')
        r.next()
        
        type = cfg['terc']['type']
     
        for row in r:
            if row:  # if row not empty
                if row[5].decode('utf-8') in [type['city']['regular'], type['city']['capital'], type['city']['county']]:  # if row represents city
                    city.save('test_id', row[0], row[4], row[5], row[6])
                elif row[5].decode('utf-8') in [type['commune']['city'], type['commune']['village'], type['commune']['city_village'], type['commune']['capital']]:
                    commune.save(row[0], row[4], row[5], row[6])
                elif row[5] == type['village']:  
                    village.save(row[0], row[4], row[6])
                elif row[5] == type['county']:        
                    county.save(row[0], row[4], row[6])
                elif row[5] in [type['district']['regular'], type['district']['delegacy']]:        
                    district.save(row[0], row[4], row[5], row[6])
                elif row[5].decode('utf-8') == type['province']:  
                    province.save(row[0], row[4], row[6])