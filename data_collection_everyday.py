import schedule
from fetching_currency_data import get_currency
import pandas as pd
from datetime import datetime
import time
import warnings

def save_all_currency_data():
    '''This function gets a currency rate from a day on 12:00 o'clock and update the file all_currency_data when the currency was withdrawn today the function skip'''
    file_path = "all_currency_data.csv"
     
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame()
        
    today = datetime.today().date()
    result = get_currency(0)
    
    if not df.empty and df['date'].iloc[-1] == str(today):
        print("Data for today already exists. Skipping update.")
        return
    
    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
        df = df._append({"date": result[0], "USD/PLN": result[1], "CHF/PLN": result[2], "EUR/PLN": result[3]}, ignore_index=True)
        df['EUR/USD'] = df['EUR/PLN'] / df['USD/PLN']
        df['CHF/USD'] = df['CHF/PLN'] / df['USD/PLN']
        
        df.to_csv(file_path, index=False)
        print(f"Data for {today} has been saved.")
    
schedule.every().day.at("12:00").do(save_all_currency_data)

while True:
    schedule.run_pending()
    time.sleep(1)
        
        