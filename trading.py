from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# getting data
ts = TimeSeries(key='BMOZOE9D5X9ECSP9', output_format='pandas')
data, meta_data = ts.get_daily(symbol='TSLA')

print(data.head())
