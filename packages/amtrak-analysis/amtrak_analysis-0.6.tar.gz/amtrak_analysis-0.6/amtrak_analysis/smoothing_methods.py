import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def calculate_moving_averages(ts, window):
    """중심 및 후행 이동 평균 계산"""
    ma_centered = ts.rolling(window, center=True).mean()  # 중심 이동 평균 계산
    ma_trailing = ts.rolling(window).mean()  # 후행 이동 평균 계산
    
    # 인덱스를 조정하여 원래 시계열과 맞춤
    ma_centered = pd.Series(ma_centered[:-1].values, index=ma_centered.index[1:])
    ma_trailing = pd.Series(ma_trailing[:-1].values, index=ma_trailing.index[1:])
    
    return ma_centered, ma_trailing  # 중심 이동 평균과 후행 이동 평균 반환

def exponential_smoothing(ts, trend=None, seasonal=None, seasonal_periods=None, freq=None):
    """시계열 데이터에 지수 평활법을 적용"""
    exp_smooth = ExponentialSmoothing(ts, trend=trend, seasonal=seasonal, seasonal_periods=seasonal_periods, freq=freq).fit()
    return exp_smooth.fittedvalues, exp_smooth.forecast(len(ts)), exp_smooth.resid  # 적합값, 예측값, 잔차 반환