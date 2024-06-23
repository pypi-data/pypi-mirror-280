import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from .visualization import plot_moving_averages, plot_forecasts

# FutureWarning 무시 설정
warnings.simplefilter(action='ignore', category=FutureWarning)

class AmtrakAnalysis:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df['Date'] = pd.to_datetime(self.df.Month, format='%d/%m/%Y')
        self.ridership_ts = pd.Series(self.df.Ridership.values, index=self.df.Date, name='Ridership')
        self.ridership_ts.index = pd.DatetimeIndex(self.ridership_ts.index, freq=self.ridership_ts.index.inferred_freq)

    def calculate_moving_averages(self):
        ma_centered = self.ridership_ts.rolling(12, center=True).mean()
        ma_trailing = self.ridership_ts.rolling(12).mean()
        return ma_centered, ma_trailing

    def split_data(self, n_valid=36):
        n_train = len(self.ridership_ts) - n_valid
        train_ts = self.ridership_ts[:n_train]
        valid_ts = self.ridership_ts[n_train:]
        return train_ts, valid_ts

    def trailing_moving_average_forecast(self, train_ts, valid_ts):
        ma_trailing = train_ts.rolling(12).mean()
        last_ma = ma_trailing.iloc[-1]
        ma_trailing_pred = pd.Series(last_ma, index=valid_ts.index)
        return ma_trailing, ma_trailing_pred

    def calculate_residuals(self, train_ts, ma_trailing, valid_ts, ma_trailing_pred):
        train_residual = train_ts - ma_trailing
        valid_residual = valid_ts - ma_trailing_pred
        return train_residual, valid_residual

    def run_analysis(self, n_valid=36):
        ma_centered, ma_trailing = self.calculate_moving_averages()
        plot_moving_averages(self.ridership_ts, ma_centered, ma_trailing)
        
        train_ts, valid_ts = self.split_data(n_valid)
        
        ma_trailing, ma_trailing_pred = self.trailing_moving_average_forecast(train_ts, valid_ts)
        
        residual_train, residual_valid = self.calculate_residuals(train_ts, ma_trailing, valid_ts, ma_trailing_pred)
        
        plot_forecasts(train_ts, valid_ts, ma_trailing, ma_trailing_pred, residual_train, residual_valid)

    def plot_moving_averages(self):
        ma_centered, ma_trailing = self.calculate_moving_averages()
        plot_moving_averages(self.ridership_ts, ma_centered, ma_trailing)

    def plot_forecasts(self, n_valid=36):
        train_ts, valid_ts = self.split_data(n_valid)
        ma_trailing, ma_trailing_pred = self.trailing_moving_average_forecast(train_ts, valid_ts)
        residual_train, residual_valid = self.calculate_residuals(train_ts, ma_trailing, valid_ts, ma_trailing_pred)
        plot_forecasts(train_ts, valid_ts, ma_trailing, ma_trailing_pred, residual_train, residual_valid)