from redis import Redis

import csv
import json


def read_json_file(filepath, data_identifier):
    with open(filepath) as jsonfile:
        data = json.load(jsonfile)

        return data[data_identifier]


def write_csv(filepath, data):
    with open(filepath, 'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Code', 'Name', 'Rate', 'Inverse'))
        writer.writerows(data)


def redis_client(host='localhost', port=6379) -> Redis:
    return Redis(host, port, decode_responses=True)


def upload_data_to_redis(data_set, namespace_mapping, namespace_modifier=None):
    redis = redis_client()

    if namespace_modifier:
        namespace_mapping = f'{namespace_mapping}:{namespace_modifier}'

    # Check to see if hash already exists
    if redis.get(namespace_mapping) is None:
        redis.hset(namespace_mapping, mapping=data_set)
