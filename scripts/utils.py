from redis import Redis

import csv
import json


def read_json_file(filepath, data_identifier):
    with open(filepath) as jsonfile:
        data = json.load(jsonfile)

        return data[data_identifier]


# def read_csv_file(filepath):
#     with open(filepath, 'r') as csvfile:
#         reader = csv.reader(csvfile)

#         data = list()

#         for row in reader:
#             data.append(ConversionInfo(*row))

#         return data


def write_csv(filepath, data):
    with open(filepath, 'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Code', 'Name', 'Rate', 'Inverse'))
        writer.writerows(data)


def redis_client(host='localhost', port=6379) -> Redis:
    return Redis(host, port, decode_responses=True)


# TODO: Add value namespace mapping param
def upload_data_to_redis(data_set, namespace_identifier):
    redis = redis_client()

    if redis.get(namespace_identifier) is None:
        redis.hset(
            namespace_identifier,
            mapping=data_set
        )
