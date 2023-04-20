#!lua name=forexlib

local REDIS_HOSTNAME = 'localhost'
local REDIS_PORT = '6379'

local CURRENCY_CODE_NAMESPACE = 'currency_codes'
local CURRENCY_RATES_NAMESPACE = 'currency_rates'
local CONVERSION_INFO_NAMESPACE = 'conversion_info'

local function get_currency_codes()
    return redis.call('hgetall', CURRENCY_CODE_NAMESPACE)
end

local function get_currency_rates()
    return redis.call('hgetall', CURRENCY_RATES_NAMESPACE)
end

local function get_conversion_info(currency_code)
    return redis.call('hgetall', CONVERSION_INFO_NAMESPACE .. ':' .. currency_code)
end

redis.register_function('forex_codes', get_currency_codes)
redis.register_function('forex_rates', get_currency_rates)
redis.register_function('conversion_info', get_conversion_info)
