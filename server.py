from flask import Flask, jsonify
from flask_restful import Resource
from pymongo import MongoClient
from city import CityDAO
from province import ProvinceDAO
from commune import CommuneDAO
from county import CountyDAO
from district import DistrictDAO
from village import VillageDAO

app = Flask(__name__)

# DAO to manipulate collections
cit = CityDAO()
pro = ProvinceDAO()
com = CommuneDAO()
cou = CountyDAO()
dis = DistrictDAO()
vil = VillageDAO()


@app.route("/en/city", methods=['GET'])
def city():
    return jsonify({'cities' : cit.find_all()})


@app.route("/en/province", methods=['GET'])
def province():
    return jsonify({'provincies' : pro.find_all()})


@app.route("/en/commune", methods=['GET'])
def commune():
    return jsonify({'communies' : com.find_all()})


@app.route("/en/county", methods=['GET'])
def county():
    return jsonify({'counties' : cou.find_all()})

@app.route("/en/district", methods=['GET'])
def district():
    return jsonify({'districties' : dis.find_all()})

@app.route("/en/village", methods=['GET'])
def village():
    return jsonify({'villages' : vil.find_all()})

if __name__ == '__main__':
     app.run(port=5002)
 
