from craigslist.utils.json_utils import parse_json


qp_map = {
    #vehicle
    'location': 'location',
    'hasPhoto': 'hasPic',
    'mostRecent': 'postedToday',
    'noDuplicates': 'bundleDuplicates',
    'zipCode': 'postal',
    'searchDistance': 'search_distance',
    'minPrice': 'min_price',
    'maxPrice': 'max_price',
    'make': 'make',
    'model': 'model',
    'minModelYear': 'min_auto_year',
    'maxModelYear': 'max_auto_year',
    'minOdometer': 'min_auto_miles',
    'maxOdometer': 'max_auto_miles'
}

def create_url(raw_data):
    json_data = parse_json(raw_data)
    location = json_data['location']
    mapped_data = map_data(json_data)
    url = f'{location}.craigslist.org/search/cta'+ create_query_params(mapped_data=mapped_data)
    return ('https://'+ url).lower()

def create_query_params(mapped_data):
    first_iter = True
    qp = ''
    for key, value in mapped_data.items():
        qp += f'{"?" if first_iter else "&"}{key}={value}'
        first_iter = False
    return qp

def map_data(data): 
    mapped_data = {}
    for key, value in data.items():
        if key in qp_map:
            mapped_data[qp_map[key]] = value
    map_exceptions(mapped_data)
    return mapped_data

def map_exceptions(mapped_data):
    del mapped_data['location']
    keys = mapped_data.keys()
    map_true_false(mapped_data)

    if 'make' in keys or 'model' in keys:
        mapped_data['auto_make_model'] = ''
        if 'make' in keys:
            mapped_data['auto_make_model'] += f'{mapped_data["make"]}'
            del mapped_data['make']
        if 'model' in keys:
            mapped_data['auto_make_model'] += f'+{mapped_data["model"]}'
            del mapped_data['model']

def map_true_false(dict):
    keys_to_del = []
    for key, value in dict.items():
        if value == True:
            dict[key] = 1
        elif value == False: 
            keys_to_del.append(key)
    for key in keys_to_del: 
        del dict[key]

