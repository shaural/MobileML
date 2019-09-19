import requests


def get_stock_data(stock_symbol, start_date, end_date):
    base_url = 'https://marketdata.websol.barchart.com/getHistory.json'
    api_key = open('apiKey.txt').readline().strip()
    params = {'apikey': api_key, 'symbol': stock_symbol, 'type': 'daily', 'startDate': start_date, 'endDate': end_date}
    data_response = requests.get(base_url, params)
    print(data_response.url)
    return data_response.json()


def decode_json_response(json_data):
    open_prices = []
    close_prices = []
    highs = []
    lows = []
    volumes = []
    results = json_data.get('results')
    for result in results:
        open_prices.append(result.get('open'))
        close_prices.append(result.get('close'))
        highs.append(result.get('high'))
        lows.append(result.get('low'))
        volumes.append(result.get('volume'))
    return open_prices, close_prices, highs, lows, volumes


def calculate_diffs(input_array):
    diffs = []
    for i in range(len(input_array) - 1):
        diff = input_array[i + 1] - input_array[i]
        if diff >= 0:
            diffs.append(1)
        else:
            diffs.append(0)
    return diffs


def calc_price_diff(open_prices, close_prices):
    price_diffs = []
    for i in range(len(open_prices) - 1):
        diff = open_prices[i + 1] - close_prices[i]
        if diff >= 0:
            price_diffs.append([1, 0])
        else:
            price_diffs.append([0, 1])
    return price_diffs


def build_data_subsets(stock_symbol, start_date, end_date):
    json_data = get_stock_data(stock_symbol, start_date, end_date)
    open_prices, close_prices, highs, lows, volumes = decode_json_response(json_data)

    open_diffs = calculate_diffs(open_prices)
    close_diffs = calculate_diffs(close_prices)
    high_diffs = calculate_diffs(highs)
    low_diffs = calculate_diffs(lows)
    volume_diffs = calculate_diffs(volumes)

    labels = calc_price_diff(open_prices, close_prices)

    final_data = []
    for i in range(len(open_diffs)):
        final_data.append([open_diffs[i], close_diffs[i], high_diffs[i], low_diffs[i], volume_diffs[i]])

    return final_data, labels
