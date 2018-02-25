import csv
from city import CityDAO
from province import ProvinceDAO
from county import CountyDAO
from commune import CommuneDAO
from district import DistrictDAO
from village import VillageDAO
from utils import config

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
                if row[5] in [type['city']['regular'], type['city']['capital'], type['city']['county']]:  # if row represents city
                    city.save('test_id', row[0], row[4], row[5], row[6])
                elif row[5] in [type['commune']['city'], type['commune']['village'], type['commune']['city_village']]:
                    commune.save(row[0], row[4], row[5], row[6])
                elif row[5] == type['village']:  
                    village.save(row[0], row[4], row[6])
                elif row[5] == type['county']:        
                    county.save(row[0], row[4], row[6])
                elif row[5] in [type['district']['regular'], type['district']['delegacy']]:        
                    district.save(row[0], row[4], row[5], row[6])
                elif row[5].decode('utf-8') == type['province']:  
                    province.save(row[0], row[4], row[6])
                
                else:
                    print row


def main():
    # drop all collections before load 
    refresh()

    # load TERC collections
    load_terc()


if __name__ == "__main__":
    main()        
