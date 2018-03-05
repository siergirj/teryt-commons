import csv
import yaml


# read configuration
def config():
    with open("config.yml", 'r') as config:
        return yaml.load(config)
