from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
# import matplotlib.dates as mpl_dates
import pandas as pd
from datetime import date, timedelta

def get_data():

    # getting data
    ts = TimeSeries(key='BMOZOE9D5X9ECSP9', output_format='pandas')

    ticker = input("Ticker: ")

    try:
        data, meta_data = ts.get_intraday(symbol=ticker, interval='15min', outputsize='compact')

        # moving date to column
        data['date'] = data.index

        print(data.head())

        # filter for current trading day (work days of week)

        # create dataset to plot
        ohlc = data.loc[:, ['date', '1. open', '2. high', '3. low', '4. close']]

        ohlc['date'] = pd.to_datetime(ohlc['date'])
        # ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num)
        ohlc = ohlc.astype(float)

        # extracting dataframes
        high = data['2. high']
        low = data['3. low']
        open = data['1. open']
        close = data['4. close']

        # typical price, seems to be working
        typical_price = (high + low + close) / 3
        print(typical_price.head())

        # moving average
        moving_average = typical_price.rolling(window=20).mean()
        print(moving_average)

        # bollinger band
        num_std = 2

        bollinger_upper = moving_average + num_std * typical_price.std()
        bollinger_lower = moving_average - num_std * typical_price.std()

        # adding moving_average and bollinger band to ohlc dataset
        ohlc['SMA20'] = moving_average
        ohlc['bollinger_upper'] = bollinger_upper
        ohlc['bollinger_lower'] = bollinger_lower

        # creating chart
        plt.style.use('ggplot')
        fig, ax = plt.subplots()

        candlestick_ohlc(ax, ohlc.values, width=0.6,
                        colorup='green', colordown='red', alpha=0.8)

        # setting labels and titles
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        fig.suptitle('Daily Candlestick Chart of ' + ticker)

        # formatting date
        # date_format = mpl_dates.DateFormatter('%d-%m-%Y')
        # ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()

        # adding moving average
        ax.plot(ohlc['date'], ohlc['SMA20'], color='blue', label='SMA20')

        # adding bollinger band
        ax.plot(ohlc['date'], ohlc['bollinger_upper'],
                color='orange', label='Bollinger upper')
        ax.plot(ohlc['date'], ohlc['bollinger_lower'],
                color='orange', label='Bollinger lower')

        ax.fill_between(ohlc['date'], ohlc['bollinger_upper'],
                        ohlc['bollinger_lower'], alpha=0.3)

        fig.tight_layout()

        plt.legend()
        plt.show()

    except:
        print("Something went wrong")

def get_data2():
    # getting data
    ts = TimeSeries(key='BMOZOE9D5X9ECSP9', output_format='pandas')

    ticker = input("Ticker: ")

    try:
        data, meta_data = ts.get_intraday(symbol=ticker, interval='15min', outputsize='compact')

        # only one day
        today = date.today()
        print("Today's date:", today)

        data['date'] = data.index


        if today.strftime("%A") == 'Saturday':
                today = today - timedelta(1)
        elif today.strftime("%A") == 'Sunday':
            today = today - timedelta(2)

        print('Modified date:', today, '-', today.strftime("%A"))

        data = data.loc[pd.to_datetime(data['date']) >= today]
        print(data.head())

        # create dataset to plot
        ohlc = data.loc[:, ['date', '1. open', '2. high', '3. low', '4. close']]

        # ohlc['date'] = pd.to_datetime(ohlc['date'])
        # ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num)
        # ohlc = ohlc.astype(float)

        # extracting dataframes
        high = data['2. high']
        low = data['3. low']
        open = data['1. open']
        close = data['4. close']

        # typical price, seems to be working
        typical_price = (high + low + close) / 3
        print(typical_price.head())

        # moving average
        moving_average = typical_price.rolling(window=20).mean()
        print(moving_average)

        # bollinger band
        num_std = 2

        bollinger_upper = moving_average + num_std * typical_price.std()
        bollinger_lower = moving_average - num_std * typical_price.std()

        # adding moving_average and bollinger band to ohlc dataset
        ohlc['SMA20'] = moving_average
        ohlc['bollinger_upper'] = bollinger_upper
        ohlc['bollinger_lower'] = bollinger_lower

        # creating chart
        plt.style.use('ggplot')
        fig, ax = plt.subplots()

        print('INFO:', ohlc.info())

        candlestick_ohlc(ax, ohlc.values, width=0.6,
                        colorup='green', colordown='red', alpha=0.8)

        # setting labels and titles
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        fig.suptitle('Daily Candlestick Chart of ' + ticker)

        # formatting date
        # date_format = mpl_dates.DateFormatter('%d-%m-%Y %H:%M:%S')
        # ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()

        # adding moving average
        ax.plot(ohlc['date'], ohlc['SMA20'], color='blue', label='SMA20')

        # adding bollinger band
        ax.plot(ohlc['date'], ohlc['bollinger_upper'],
                color='orange', label='Bollinger upper')
        ax.plot(ohlc['date'], ohlc['bollinger_lower'],
                color='orange', label='Bollinger lower')

        ax.fill_between(ohlc['date'], ohlc['bollinger_upper'],
                        ohlc['bollinger_lower'], alpha=0.3)

        fig.tight_layout()

        plt.legend()
        plt.show()

    except Exception as e:
        print(e)

def boi():
    today = date.today()
    print('Today:', today)
    print('Today in text:', today.strftime("%A"))

    # check for weekends
    if today.strftime("%A") == 'Saturday':
        today = today - timedelta(1)
    elif today.strftime("%A") == 'Sunday':
        today = today - timedelta(2)

    print('Modified date:', today, '-', today.strftime("%A"))

# boi()
get_data2()

# i need the freshet piece of data - need to ping API every minute




