import csv
import yaml


# read configuration
def config():
    with open("config.yaml", 'r') as config:
        return yaml.load(config)
