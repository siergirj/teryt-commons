from flask import Flask, jsonify
from flask_restful import Resource
from pymongo import MongoClient
from city import CityDAO

app = Flask(__name__)

c = CityDAO()

@app.route("/en/city", methods=['GET'])
def city():
    return jsonify({'cities' : c.find_all()})

@app.route("/en/province")
def province():
    return "Hello province!"


if __name__ == '__main__':
     app.run(port=5002)
 