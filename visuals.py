import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

def new_plotter():
    ts = TimeSeries(key='BMOZOE9D5X9ECSP9', output_format='pandas')
    ticker = input("Ticker: ")

    try:
        data, meta_data = ts.get_intraday(
            symbol=ticker, interval='15min', outputsize='compact')

        data['date'] = data.index

        fig = go.Figure(data=[go.Candlestick(x=data['date'],
                    open=data['1. open'],
                    high=data['2. high'],
                    low=data['3. low'],
                    close=data['4. close']
                    )])

        fig.show()

    except Exception as e:
        print(e)

new_plotter()


