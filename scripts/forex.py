from utils import read_json_file, upload_data_to_redis, write_csv

from collections import namedtuple


CURRENCY_CODES_JSON_FILE = 'assets/currency_codes.json'
CURRENCY_RATES_JSON_FILE = 'assets/currency_rates.json'
CONVERSIONS_INFO_CSV_FILE = 'assets/conversion_info.csv'

CURRENCY_CODES_DATA_IDENTIFIER = 'symbols'
CURRENCY_RATES_DATA_IDENTIFIER = 'rates'

CURRENCY_CODES_NAMESPACE_IDENTIFIER = 'currency_codes'
CURRENCY_RATES_NAMESPACE_IDENTIFIER = 'currency_rates'
CONVERSION_INFO_NAMESPACE_IDENTIFIER = 'conversion_info'

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
                rate=round(currency_rates_data[currency_code], 6),
                inverse=round(1 / currency_rates_data[currency_code], 6)
            )
        )

    return currency_codes_data, currency_rates_data, currency_conversion_data


def upload_currency_data_to_redis(codes_data, rates_data, conversion_data):
    upload_data_to_redis(
        data_set=codes_data,
        namespace_mapping=CURRENCY_CODES_NAMESPACE_IDENTIFIER
    )

    upload_data_to_redis(
        data_set=rates_data,
        namespace_mapping=CURRENCY_RATES_NAMESPACE_IDENTIFIER
    )

    for conversion in conversion_data:
        conversion: ConversionInfo = conversion
        upload_data_to_redis(
            data_set=conversion._asdict(),
            namespace_mapping=CONVERSION_INFO_NAMESPACE_IDENTIFIER,
            namespace_modifier=conversion.code
        )


def main():
    codes, rates, conversions = process_currency_data()

    upload_currency_data_to_redis(
        codes_data=codes,
        rates_data=rates,
        conversion_data=conversions
    )

    # write_csv(filepath=CONVERSIONS_INFO_CSV_FILE, data=conversions)


if __name__ == '__main__':
    main()
