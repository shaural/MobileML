import requests

def get_stock_data(stock_symbol, start_date, end_date):
    base_url = 'https://marketdata.websol.barchart.com/getHistory.json'
    api_key = open('apiKey.txt').readline().strip()
    params = {'apikey': api_key, 'symbol': stock_symbol, 'type': 'daily', 'startDate': start_date, 'endDate': end_date}
    data_response = requests.get(base_url, params)
    print(data_response.url)
    return data_response.json()

print(get_stock_data('AAPL', '20190917', '20190919'))