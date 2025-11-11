import requests

def fetch_stock_data(symbol, token, start_date=None, end_date=None):
    base_url = "https://api.twelvedata.com/time_series"  # Replace with your TIME_SERIES.url()
    
    params = {
        'apikey': token,
        'symbol': symbol.upper(),
        'interval': '1day',  # TimeFrame.ONE_DAY equivalent
        'format': 'CSV',
        'outputsize': '5000'
    }
    
    if start_date:
        params['start_date'] = start_date
    
    if end_date:
        params['end_date'] = end_date
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raises exception for 4xx/5xx errors
    
    return response.text


token = "66950322bf134aeda8255e083b983bbc"
symbol = "GOOGL"
csv_data = fetch_stock_data(symbol, token)

# Replace header with capitalized version
lines = csv_data.split('\n')
lines[0] = 'Date;Open;High;Low;Close;Volume'
csv_data = '\n'.join(lines)

# Write to CSV file named as symbol.csv
with open(f"{symbol}.csv", "w") as f:
    f.write(csv_data)

print(f"Data saved to {symbol}.csv")