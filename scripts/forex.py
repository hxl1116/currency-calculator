from utils import read_json_file, redis_client, upload_data_to_redis

from collections import namedtuple


CURRENCY_CODES_JSON_FILE = 'assets/currency_codes.json'
CURRENCY_RATES_JSON_FILE = 'assets/currency_rates.json'
CURRENCY_INFO_CSV_FILE = 'assets/forex_rates.csv'

CURRENCY_CODES_DATA_IDENTIFIER = 'symbols'
CURRENCY_RATES_DATA_IDENTIFIER = 'rates'

CURRENCY_CODES_NAMESPACE_IDENTIFIER = 'currency_codes'
CURRENCY_RATES_NAMESPACE_IDENTIFIER = 'currency_rates'

ConversionInfo = namedtuple('ConversionInfo', 'code name rate inverse')


def process_currency_data():
    currency_codes_data: dict = read_json_file(
        CURRENCY_CODES_JSON_FILE,
        CURRENCY_CODES_DATA_IDENTIFIER
    )

    currency_rates_data: dict = read_json_file(
        CURRENCY_RATES_JSON_FILE,
        CURRENCY_RATES_DATA_IDENTIFIER
    )

    currency_conversion_data = list()

    for currency_code, currency_name in currency_codes_data.items():
        currency_conversion_data.append(
            ConversionInfo(
                code=currency_code,
                name=currency_name,
                rate=currency_rates_data[currency_code],
                inverse=(1 / currency_rates_data[currency_code])
            )
        )

    return currency_codes_data, currency_rates_data, currency_conversion_data


def upload_currency_data_to_redis(codes_data, rates_data, conversion_data):
    upload_data_to_redis(
        data_set=codes_data,
        namespace_identifier=CURRENCY_CODES_NAMESPACE_IDENTIFIER
    )
    upload_data_to_redis(
        data_set=rates_data,
        namespace_identifier=CURRENCY_RATES_NAMESPACE_IDENTIFIER
    )

    # TODO: Upload conversion data


def main():
    codes, rates, conversions = process_currency_data()

    upload_currency_data_to_redis(
        codes_data=codes,
        rates_data=rates,
        conversion_data=conversions
    )


if __name__ == '__main__':
    main()
