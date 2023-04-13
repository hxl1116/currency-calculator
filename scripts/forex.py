from collections import namedtuple
from redis import Redis

import csv
import json

FOREX_RATES_JSON_FILE = '/Users/henrylarson/Documents/Projects/Misc/currency-calc/assets/forex_rates.json'
FOREX_SYMBOLS_JSON_FILE = '/Users/henrylarson/Documents/Projects/Misc/currency-calc/assets/forex_symbols.json'
FOREX_RATES_CSV_FILE = '/Users/henrylarson/Documents/Projects/Misc/currency-calc/assets/forex_rates.csv'

ConversionInfo = namedtuple('ConversionInfo', 'code name rate inverse')


def read_json(filepath, key):
    with open(filepath) as jsonfile:
        data = json.load(jsonfile)

        return data[key]


def read_csv(filepath):
    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)

        data = list()

        for row in reader:
            data.append(ConversionInfo(*row))

        return data
            

def write_csv(filepath, data):
    with open(filepath, 'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Code', 'Name', 'Rate', 'Inverse'))
        writer.writerows(data)


def merge_data(rates_data, symbols_data):
    rates = list()

    for k, v in rates_data.items():
        rates.append(ConversionInfo(k, symbols_data[k], v, round(1/v, 7)))

    return rates


def connect(host='localhost', port=6379):
    return Redis(host, port, decode_responses=True)


def load_data(forex_data):
    redis: Redis = connect()

    if redis.get('forex_rates') is None:
        redis.hset('forex_rates', mapping={rate.symbol: f'forex_rate:{rate.symbol}'
                                           for rate in forex_data})

    for rate in forex_data:
        redis.hset(f'forex_rate:{rate.symbol}', mapping=rate._asdict())


def main():
    # rates_data = read_json(FOREX_RATES_JSON_FILE, 'rates')
    # symbols_data = read_json(FOREX_SYMBOLS_JSON_FILE, 'symbols')
    # forex_data = merge_data(rates_data, symbols_data)

    # write_csv('forex_rates.csv', forex_data)

    forex_data = read_csv(FOREX_RATES_CSV_FILE)

    load_data(forex_data)


if __name__ == '__main__':
    main()
