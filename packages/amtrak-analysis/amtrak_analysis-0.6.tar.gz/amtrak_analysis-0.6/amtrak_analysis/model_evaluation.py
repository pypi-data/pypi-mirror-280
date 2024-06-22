import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.tsa import tsatools
import numpy as np

def split_data(ts, n_valid):
    """시계열 데이터를 훈련 데이터와 검증 데이터로 분할"""
    n_train = len(ts) - n_valid  # 훈련 데이터 크기 설정
    train_ts = ts[:n_train]  # 훈련 데이터
    valid_ts = ts[n_train:]  # 검증 데이터
    return train_ts, valid_ts  # 훈련 데이터와 검증 데이터 반환

def calculate_trailing_average(train_ts, valid_ts, window):
    """훈련 데이터에 대한 후행 이동 평균을 계산하고 검증 데이터에 대한 예측값을 생성"""
    ma_trailing = train_ts.rolling(window).mean()  # 후행 이동 평균 계산
    last_ma = ma_trailing.iloc[-1]  # 마지막 후행 이동 평균 값 저장 (FutureWarning 해결)
    ma_trailing_pred = pd.Series(last_ma, index=valid_ts.index)  # 마지막 후행 이동 평균 값을 사용하여 검증 데이터 기간에 대한 예측값 생성
    return ma_trailing, ma_trailing_pred  # 후행 이동 평균과 예측값 반환

def regression_with_trend_seasonality(train_df, valid_df):
    """트렌드와 계절성을 포함한 회귀 모형을 적합"""
    import numpy as np  # 함수 내에서 numpy를 임포트

    formula = 'Ridership ~ trend + np.square(trend) + C(Month)'  # 회귀 모형 수식 정의
    # patsy 환경에서 np를 사용할 수 있도록 설정
    env = {'np': np}
    ridership_lm_trendseason = sm.ols(formula=formula, data=train_df, eval_env=env).fit()  # 회귀 모형 적합
    ridership_prediction = ridership_lm_trendseason.predict(valid_df.iloc[0, :])  # 검증 데이터의 첫 번째 행에 대해 예측값 계산
    ma_trailing = ridership_lm_trendseason.resid.rolling(12).mean()  # 훈련 데이터에 대한 마지막 후행 이동 평균 계산
    return ridership_prediction, ma_trailing, ridership_lm_trendseason  # 예측값, 후행 이동 평균, 회귀 모형 반환

def add_trend_and_month(df):
    """데이터프레임에 트렌드와 월 정보를 추가"""
    df = tsatools.add_trend(df, trend='ct')  # 트렌드 열 추가
    df['Month'] = df.index.month  # 월 정보 열 추가
    return df  # 트렌드와 월 정보가 추가된 데이터프레임 반환