from scripts.utils import read_json_file, redis_client

from collections import namedtuple


CURRENCY_CODES_JSON_FILE = 'assets/currency_codes.json'
CURRENCY_RATES_JSON_FILE = 'assets/currency_rates.json'
CURRENCY_INFO_CSV_FILE = 'assets/forex_rates.csv'

CURRENCY_CODES_DATA_IDENTIFIER = 'symbols'
CURRENCY_RATES_DATA_IDENTIFIER = 'rates'

CurrencyCode = namedtuple('CurrencyCode', 'code name')
CurrencyRate = namedtuple('CurrencyRate', 'code rate')
ConversionInfo = namedtuple('ConversionInfo', 'code name rate inverse')


def combine_currency_data(rates_data, symbols_data):
    rates = list()

    for k, v in rates_data.items():
        rates.append(ConversionInfo(k, symbols_data[k], v, round(1/v, 7)))

    return rates


def process_currency_data():
    currency_codes_data = read_json_file(
        CURRENCY_CODES_JSON_FILE,
        CURRENCY_CODES_DATA_IDENTIFIER
    )

    currency_rates_data = read_json_file(
        CURRENCY_RATES_JSON_FILE,
        CURRENCY_RATES_DATA_IDENTIFIER
    )


def upload_currency_data_to_redis(currency_codes_data, currency_rates_data):
    redis = redis_client()

    if redis.get('currency_info') is None:
        pass


def load_data(forex_data):
    redis = redis_client()

    if redis.get('forex_rates') is None:
        redis.hset('forex_rates', mapping={rate.symbol: f'forex_rate:{rate.symbol}'
                                           for rate in forex_data})

    for rate in forex_data:
        redis.hset(f'forex_rate:{rate.symbol}', mapping=rate._asdict())


def main():
    process_currency_data()


if __name__ == '__main__':
    main()
