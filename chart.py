import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from tkinter import filedialog
from ema import ema_calculation


class ChartPlotter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.interval = False
        self.length = False
        self.ohlc = None
        self.ema = False

    def read_data(self):
        self.df = pd.read_csv(self.file_path, skiprows=1, names=['Timestamp', 'Price'])
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        self.df.set_index('Timestamp', inplace=True)

    def aggregate_candles(self):
        if isinstance(self.interval, bool):
            self.interval = input("Введите интервал (например, '5Min', '1H', '1D'): ")
        self.ohlc = self.df['Price'].resample(self.interval).ohlc()
        self.ohlc.reset_index(inplace=True)
        self.ohlc['Timestamp'] = self.ohlc['Timestamp'].map(mdates.date2num)

    def calculate_ema(self):
        if isinstance(self.length, bool):
            self.length = int(input("Введите длину EMA (количество периодов): "))
        self.ema = ema_calculation(self.ohlc['close'], self.length)

    def plot_chart(self):
        fig, ax = plt.subplots()
        candlestick_ohlc(ax, self.ohlc.values, width=0.6, colorup='g', colordown='r')
        if not isinstance(self.ema, bool):
            ax.plot(self.ohlc['Timestamp'], self.ema, label=f'EMA ({self.length} periods)')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.xticks(rotation=45)
        plt.xlabel('Timestamp')
        plt.ylabel('Price')
        ax.legend()
        plt.title('Candlestick Chart with EMA')
        save_path = filedialog.asksaveasfilename(defaultextension='.png')
        plt.savefig(save_path)
        plt.show()
