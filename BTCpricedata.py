import tensorflow as tf
import pandas as pd

# Sample DataFrame
data = pd.read_csv("crypto-currency-dataset.csv", parse_dates=['Date'])

# Convert 'Date' column to Unix timestamps (seconds since the epoch)
data['Date'] = data['Date'].apply(lambda x: x.timestamp())

data
