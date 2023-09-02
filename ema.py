def ema_calculation(data, length):
    ema = data.ewm(span=length, min_periods=length).mean()
    return ema
