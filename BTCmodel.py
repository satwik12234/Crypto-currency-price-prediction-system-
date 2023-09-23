data.drop(columns=["Volume (BTC)","Close (ETH)","Volume (ETH)","Close (USDT)","Volume (USDT)","Close (BNB)","Volume (BNB)"])
del data['Date']
scaler=MinMaxScaler(feature_range=(0,1))
closedf=scaler.fit_transform(np.array(data).reshape(-1,1))
print(closedf.shape)
