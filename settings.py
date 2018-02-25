# mongo DB
MONGO_DBNAME = 'teryt'

province_schema = {
    'id': {
        'type': 'string'
    },
    'name': {
        'type': 'string'
    },
    'timestamp': {
        'type': 'string'
    }
}

province = {
    'resource_methods': ['GET'],
    'schema': province_schema
}

city = {
    'resource_methods': ['GET'],
    'schema': province_schema
}

commune = {
    'resource_methods': ['GET'],
    'schema': province_schema
}

county = {
    'resource_methods': ['GET'],
    'schema': province_schema
}

district = {
    'resource_methods': ['GET'],
    'schema': province_schema
}

village = {
    'resource_methods': ['GET'],
    'schema': province_schema
}

DOMAIN = {
    'province': province,
    'city' : city,
    'commune' : commune,
    'county' : county,
    'district' : district,
    'village' : village
}
