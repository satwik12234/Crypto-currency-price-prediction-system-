close1 = data['Close (BTC)']
data = pd.DataFrame({'Date': 'Date', 'Close (BTC)': close1})

axis = data.plot(x='Date', y='Close (BTC)')
axis.set_xlabel("Date")
axis.set_ylabel("Close Price")
