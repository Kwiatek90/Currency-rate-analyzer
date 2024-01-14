import pandas as pd

def select_currency_data(df):
    try:
        user_input = input("Enter currency pairs separated by commas (USD/PLN, CHF/PLN, EUR/PLN, EUR/USD, CHF/USD):")
        selected_currencies = [currency.strip().upper() for currency in user_input.split(',')]

        valid_columns = df.columns
        invalid_currencies = [currency for currency in selected_currencies if currency not in valid_columns]
        
        if invalid_currencies:
            raise KeyError(f"Invalid currency(s): {', '.join(invalid_currencies)}")
        
        selected_df = save_selected_currency_data(df, selected_currencies)

        user_input = input("You want to save this data to csv file? (Yes/No)")
        
        if user_input.strip().lower() == "yes":
            selected_df.to_csv("selected_currency_data.csv", index=False)
            print(f"Data for {', '.join(selected_currencies)} has been saved!")
        else:
            print("Program ends ...")
        
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        
def save_selected_currency_data(df, selected_currencies):
    selected_columns = ['date'] + [currency for currency in selected_currencies]
    selected_df = df[selected_columns]
    print(selected_df)
    return selected_df

def select_currency_data_analysis(df):
    user_input = input("Enter the currency pair for which you want to calculate statistics (USD/PLN, CHF/PLN, EUR/PLN, EUR/USD, CHF/USD): ")
    selected_currency_pair = user_input.strip().upper()

    calculate_currency_stats(df, selected_currency_pair)
    
def calculate_currency_stats(df, currency_pair):
    try:
        df = df.dropna()
        currency_column = df[currency_pair]
        currency_date = df['date']
        
        average_rate = currency_column.mean()
        median_rate = currency_column.median()
        min_rate = currency_column.min()
        max_rate = currency_column.max()
        start_date = currency_date.min()
        end_date = currency_date.max()
        
        print(f"Statistics for {currency_pair} from date {start_date} to {end_date}:")
        print(f"Average Rate: {average_rate:.4f}")
        print(f"Median Rate: {median_rate:.4f}")
        print(f"Minimum Rate: {min_rate:.4f}")
        print(f"Maximum Rate: {max_rate:.4f}")
        
    except KeyError as e:
        print(f"Invalid currency pair: {e.args[0]}")
    except Exception as e:
        print(f"Error calculating statistics: {e}")

if __name__ == '__main__':
    
    file_path = "all_currency_data.csv"
    df = pd.read_csv(file_path)
    
    user_input = input("Hello! What do you want to do with the exchange rate data? You want to view specific currencies (Select 1) or you want to analyze a specific currency (Select 2)")
    if user_input == "1":
        select_currency_data(df)
    elif user_input == "2":
        select_currency_data_analysis(df)
    else:
        print("Wrong choices!")
    