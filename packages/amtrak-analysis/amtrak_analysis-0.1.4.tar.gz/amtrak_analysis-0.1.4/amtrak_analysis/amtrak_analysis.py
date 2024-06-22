import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import statsmodels.formula.api as sm
from statsmodels.tsa import tsatools
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing

def plot_ridership(data_path):
    """
    Amtrak 승객 데이터를 시각화하는 함수.
    원본 시계열 데이터와 중심 및 후행 이동 평균을 플롯함.

    :param data_path: Amtrak 데이터 파일 경로
    """
    Amtrak_df = pd.read_csv(data_path)
    Amtrak_df['Date'] = pd.to_datetime(Amtrak_df.Month, format='%d/%m/%Y')
    ridership_ts = pd.Series(Amtrak_df.Ridership.values, index=Amtrak_df.Date, name='Ridership')
    ridership_ts.index = pd.DatetimeIndex(ridership_ts.index, freq=ridership_ts.index.inferred_freq)
    ma_centered = ridership_ts.rolling(12, center=True).mean()
    ma_trailing = ridership_ts.rolling(12).mean()
    ma_centered = pd.Series(ma_centered[:-1].values, index=ma_centered.index[1:])
    ma_trailing = pd.Series(ma_trailing[:-1].values, index=ma_trailing.index[1:])
    fig, ax = plt.subplots(figsize=(8, 7))
    ax = ridership_ts.plot(ax=ax, color='black', linewidth=0.25)
    ma_centered.plot(ax=ax, linewidth=2)
    ma_trailing.plot(ax=ax, style='--', linewidth=2)
    ax.set_xlabel('Time')
    ax.set_ylabel('Ridership')
    ax.legend(['Ridership', 'Centered Moving Average', 'Trailing Moving Average'])
    plt.show()

def moving_average_forecast(data_path, nValid=36):
    """
    후행 이동 평균을 사용한 승객 데이터 예측 및 잔차 시각화.

    :param data_path: Amtrak 데이터 파일 경로
    :param nValid: 검증 데이터 크기
    """
    Amtrak_df = pd.read_csv(data_path)
    Amtrak_df['Date'] = pd.to_datetime(Amtrak_df.Month, format='%d/%m/%Y')
    ridership_ts = pd.Series(Amtrak_df.Ridership.values, index=Amtrak_df.Date, name='Ridership')
    ridership_ts.index = pd.DatetimeIndex(ridership_ts.index, freq=ridership_ts.index.inferred_freq)
    nTrain = len(ridership_ts) - nValid
    train_ts = ridership_ts[:nTrain]
    valid_ts = ridership_ts[nTrain:]
    ma_trailing = train_ts.rolling(12).mean()
    last_ma = ma_trailing[-1]
    ma_trailing_pred = pd.Series(last_ma, index=valid_ts.index)
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(9, 7.5))
    ma_trailing.plot(ax=axes[0], linewidth=2, color='C1')
    ma_trailing_pred.plot(ax=axes[0], linewidth=2, color='C1', linestyle='dashed')
    residual = train_ts - ma_trailing
    residual.plot(ax=axes[1], color='C1')
    residual = valid_ts - ma_trailing_pred
    residual.plot(ax=axes[1], color='C1', linestyle='dashed')
    graphLayout(axes, train_ts, valid_ts)

def linear_regression_forecast(data_path, nTrain, nValid):
    """
    선형 회귀 모형을 사용하여 승객 데이터를 예측.

    :param data_path: Amtrak 데이터 파일 경로
    :param nTrain: 훈련 데이터 크기
    :param nValid: 검증 데이터 크기
    """
    Amtrak_df = pd.read_csv(data_path)
    Amtrak_df['Date'] = pd.to_datetime(Amtrak_df.Month, format='%d/%m/%Y')
    ridership_ts = pd.Series(Amtrak_df.Ridership.values, index=Amtrak_df.Date, name='Ridership')
    ridership_ts.index = pd.DatetimeIndex(ridership_ts.index, freq=ridership_ts.index.inferred_freq)
    ridership_df = tsatools.add_trend(ridership_ts, trend='ct')
    ridership_df['Month'] = ridership_df.index.month
    train_df = ridership_df[:nTrain]
    valid_df = ridership_df[nTrain:]
    formula = 'Ridership ~ trend + np.square(trend) + C(Month)'
    ridership_lm_trendseason = sm.ols(formula=formula, data=train_df).fit()
    ridership_prediction = ridership_lm_trendseason.predict(valid_df.iloc[0, :])
    ma_trailing = ridership_lm_trendseason.resid.rolling(12).mean()
    print('Prediction', ridership_prediction[0])
    print('ma_trailing', ma_trailing[-1])

def residual_analysis(data_path, nTrain, nValid):
    """
    선형 회귀 모형의 잔차를 분석하고 시각화.

    :param data_path: Amtrak 데이터 파일 경로
    :param nTrain: 훈련 데이터 크기
    :param nValid: 검증 데이터 크기
    """
    Amtrak_df = pd.read_csv(data_path)
    Amtrak_df['Date'] = pd.to_datetime(Amtrak_df.Month, format='%d/%m/%Y')
    ridership_ts = pd.Series(Amtrak_df.Ridership.values, index=Amtrak_df.Date, name='Ridership')
    ridership_ts.index = pd.DatetimeIndex(ridership_ts.index, freq=ridership_ts.index.inferred_freq)
    ridership_df = tsatools.add_trend(ridership_ts, trend='ct')
    ridership_df['Month'] = ridership_df.index.month
    train_df = ridership_df[:nTrain]
    valid_df = ridership_df[nTrain:]
    formula = 'Ridership ~ trend + np.square(trend) + C(Month)'
    ridership_lm_trendseason = sm.ols(formula=formula, data=train_df).fit()
    residuals_ts = ridership_lm_trendseason.resid
    residuals_pred = valid_df.Ridership - ridership_lm_trendseason.predict(valid_df)
    fig, ax = plt.subplots(figsize=(9, 4))
    ridership_lm_trendseason.resid.plot(ax=ax, color='black', linewidth=0.5)
    residuals_pred.plot(ax=ax, color='black', linewidth=0.5)
    ax.set_ylabel('Ridership')
    ax.axhline(y=0, xmin=0, xmax=1, color='grey', linewidth=0.5)
    expSmooth = ExponentialSmoothing(residuals_ts, freq='MS')
    expSmoothFit = expSmooth.fit(smoothing_level=0.2)
    expSmoothFit.fittedvalues.plot(ax=ax)
    expSmoothFit.forecast(len(valid_df)).plot(ax=ax, style='--', linewidth=2, color='C0')
    singleGraphLayout(ax, [-550, 550], train_df, valid_df)

def exponential_smoothing_forecast(data_path, nTrain, nValid):
    """
    가법적 트렌드와 계절성을 가진 지수 평활 모델을 사용하여 승객 데이터 예측.

    :param data_path: Amtrak 데이터 파일 경로
    :param nTrain: 훈련 데이터 크기
    :param nValid: 검증 데이터 크기
    """
    Amtrak_df = pd.read_csv(data_path)
    Amtrak_df['Date'] = pd.to_datetime(Amtrak_df.Month, format='%d/%m/%Y')
    ridership_ts = pd.Series(Amtrak_df.Ridership.values, index=Amtrak_df.Date, name='Ridership')
    ridership_ts.index = pd.DatetimeIndex(ridership_ts.index, freq=ridership_ts.index.inferred_freq)
    train_ts = ridership_ts[:nTrain]
    valid_ts = ridership_ts[nTrain:]
    expSmooth = ExponentialSmoothing(train_ts, trend='additive', seasonal='additive', seasonal_periods=12, freq='MS')
    expSmoothFit = expSmooth.fit()
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(9, 7.5))
    expSmoothFit.fittedvalues.plot(ax=axes[0], linewidth=2, color='C1')
    expSmoothFit.forecast(len(valid_ts)).plot(ax=axes[0], linewidth=2, color='C1', linestyle='dashed')
    residual = train_ts - expSmoothFit.fittedvalues
    residual.plot(ax=axes[1], color='C1')
    residual = valid_ts - expSmoothFit.forecast(len(valid_ts))
    residual.plot(ax=axes[1], color='C1', linestyle='dashed')
    graphLayout(axes, train_ts, valid_ts)

def print_model_params(expSmoothFit):
    """
    지수 평활 모델의 파라미터 및 평가 지표를 출력.

    :param expSmoothFit: 피팅된 지수 평활 모델
    """
    print(expSmoothFit.params)
    print('AIC: ', expSmoothFit.aic)
    print('AICc: ', expSmoothFit.aicc)
    print('BIC: ', expSmoothFit.bic)

def compare_smoothing_methods(data_path):
    """
    이동 평균법과 지수 평활법을 비교하여 시각화.

    :param data_path: Amtrak 데이터 파일 경로
    """
    data = pd.read_csv(data_path, index_col='Month', parse_dates=True)
    ridership = data['Ridership']
    alpha = 0.2
    w = int(2 / alpha - 1)
    moving_avg = ridership.rolling(window=w).mean()
    exp_smooth = SimpleExpSmoothing(ridership).fit(smoothing_level=alpha).fittedvalues
    plt.figure(figsize=(14, 7))
    plt.plot(ridership, label='Original Data', color='blue', alpha=0.5)
    plt.plot(moving_avg, label=f'Moving Average (window={w})', color='red', linestyle='--', linewidth=2)
    plt.plot(exp_smooth, label=f'Exponential Smoothing (alpha={alpha})', color='green', linestyle='--', linewidth=2)
    plt.xlabel('Month')
    plt.ylabel('Ridership')
    plt.title('Comparison of Moving Average and Exponential Smoothing')
    plt.legend(loc='best')
    plt.show()

def singleGraphLayout(ax, ylim, train_df, valid_df):
    """
    그래프 레이아웃을 설정하는 함수.

    :param ax: Matplotlib 축 객체
    :param ylim: y축 범위
    :param train_df: 훈련 데이터프레임
    :param valid_df: 검증 데이터프레임
    """
    ax.set_xlim('1990', '2004-6')
    ax.set_ylim(*ylim)
    ax.set_xlabel('Time')
    one_month = pd.Timedelta('31 days')
    xtrain = (min(train_df.index), max(train_df.index) - one_month)
    xvalid = (min(valid_df.index) + one_month, max(valid_df.index) - one_month)
    xtv = xtrain[1] + 0.5 * (xvalid[0] - xtrain[1])
    ypos = 0.9 * ylim[1] + 0.1 * ylim[0]
    ax.add_line(plt.Line2D(xtrain, (ypos, ypos), color='black', linewidth=0.5))
    ax.add_line(plt.Line2D(xvalid, (ypos, ypos), color='black', linewidth=0.5))
    ax.axvline(x=xtv, ymin=0, xmax=1, color='black', linewidth=0.5)
    ypos = 0.925 * ylim[1] + 0.075 * ylim[0]
    ax.text('1995', ypos, 'Training')
    ax.text('2002-3', ypos, 'Validation')

def graphLayout(axes, train_df, valid_df):
    """
    여러 그래프의 레이아웃을 설정하는 함수.

    :param axes: Matplotlib 축 객체 배열
    :param train_df: 훈련 데이터프레임
    :param valid_df: 검증 데이터프레임
    """
    singleGraphLayout(axes[0], [1300, 2550], train_df, valid_df)
    singleGraphLayout(axes[1], [-550, 550], train_df, valid_df)
    train_df.plot(y='Ridership', ax=axes[0], color='C0', linewidth=0.75)
    valid_df.plot(y='Ridership', ax=axes[0], color='C0', linestyle='dashed', linewidth=0.75)
    axes[1].axhline(y=0, xmin=0, xmax=1, color='black', linewidth=0.5)
    axes[0].set_xlabel('')
    axes[0].set_ylabel('Ridership (in 000s)')
    axes[1].set_ylabel('Forecast Errors')
    if axes[0].get_legend():
        axes[0].get_legend().remove()