#!/usr/bin/python

import logging
import logging.config
import argparse

import utils.mongo_service

# Load logger configuration
logging.config.fileConfig('logging.conf')

def main():
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Load TERC from csv file into MongoDB.')
    parser.add_argument('-d', action='store_true', help='refresh all collections (drop all before load)')
    parser.add_argument('-t', action='store_true', help='load TERC from default directory')
    parser.add_argument('--log', dest='level', help='set log level (default=INFO)', default='INFO')

    # parse input parameters 
    args = parser.parse_args()
    
    # create logger for this APP
    logger = logging.getLogger('TERC loading')
    # set logging level from argv
    logger.setLevel(args.level)

    # drop all collections before load 
    if args.d:
        utils.mongo_service.refresh()
        logger.info('All collections dropped')

    # load TERC collections
    if args.t:
        utils.mongo_service.load_terc()
        logger.info('TERC loaded')


if __name__ == "__main__":
    main()        
