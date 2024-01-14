import requests
import pandas as pd
import datetime
import warnings
import concurrent.futures

def get_exchange_rate_from_day(currency, day):
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{day}/?format=json"
    response = requests.get(url)
    
    try:
        data = response.json()
        currency_rate = data["rates"][0]["mid"]
    except requests.exceptions.JSONDecodeError:
        currency_rate = None
        
    return currency_rate

def get_currency(day):
    day = get_day_before(day)
    usd_rate = get_exchange_rate_from_day('usd', day)
    chf_rate = get_exchange_rate_from_day('chf', day)
    eur_rate = get_exchange_rate_from_day('eur', day)
    return day, usd_rate, chf_rate, eur_rate

def get_day_before(n):
    today = datetime.date.today()
    n_day = datetime.timedelta(days = n)
    day = today - n_day
    return str(day)

if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)

        with concurrent.futures.ProcessPoolExecutor() as executor:
            df = pd.DataFrame()
            
            results = list(executor.map(get_currency, range(90)))
                
            for result in results:
                df = df._append({"date": result[0], "USD/PLN": result[1], "CHF/PLN": result[2], "EUR/PLN": result[3]}, ignore_index=True)
            
            df['EUR/USD'] = df['EUR/PLN'] / df['USD/PLN']
            df['CHF/USD'] = df['CHF/PLN'] / df['USD/PLN']
            
            df = df.dropna()
            df.to_csv("all_currency_data.csv", index=False)
            
            print(df)
    


    
    