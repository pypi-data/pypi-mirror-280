import matplotlib.pyplot as plt

def plot_moving_averages(ts, ma_centered, ma_trailing):
    """원본 시계열 데이터와 이동 평균을 플로팅"""
    fig, ax = plt.subplots(figsize=(8, 7))
    ts.plot(ax=ax, color='black', linewidth=0.25)  # 원본 시계열 데이터 플로팅
    ma_centered.plot(ax=ax, linewidth=2)  # 중심 이동 평균 플로팅
    ma_trailing.plot(ax=ax, style='--', linewidth=2)  # 후행 이동 평균 플로팅
    ax.set_xlabel('Time')
    ax.set_ylabel('Ridership')
    ax.legend(['Ridership', 'Centered Moving Average', 'Trailing Moving Average'])
    plt.show()  # 그래프 출력

def plot_trailing_average(train_ts, valid_ts, ma_trailing, ma_trailing_pred):
    """후행 이동 평균과 예측값을 잔차와 함께 플로팅"""
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(9, 7.5))
    ma_trailing.plot(ax=axes[0], linewidth=2, color='C1')  # 훈련 데이터의 후행 이동 평균 플로팅
    ma_trailing_pred.plot(ax=axes[0], linewidth=2, color='C1', linestyle='dashed')  # 검증 데이터 기간 동안의 예측값 플로팅

    residual = train_ts - ma_trailing  # 훈련 데이터 잔차 계산
    residual.plot(ax=axes[1], color='C1')  # 훈련 데이터 잔차 플로팅
    
    residual = valid_ts - ma_trailing_pred  # 검증 데이터 잔차 계산
    residual.plot(ax=axes[1], color='C1', linestyle='dashed')  # 검증 데이터 잔차 플로팅

    plt.show()  # 그래프 출력

def plot_residuals_with_smoothing(residuals_ts, valid_ts, ridership_lm_trendseason, expSmoothFit):
    """잔차와 지수 평활법 적용 결과를 플로팅"""
    fig, ax = plt.subplots(figsize=(9, 4))
    ridership_lm_trendseason.resid.plot(ax=ax, color='black', linewidth=0.5)  # 잔차 플로팅
    residuals_pred = valid_ts.Ridership - ridership_lm_trendseason.predict(valid_ts)  # 검증 데이터의 잔차 계산
    residuals_pred.plot(ax=ax, color='black', linewidth=0.5)
    ax.set_ylabel('Ridership')
    ax.axhline(y=0, xmin=0, xmax=1, color='grey', linewidth=0.5)  # y=0 기준선 추가
    
    expSmoothFit.fittedvalues.plot(ax=ax)  # 지수 평활법 적합값 플로팅
    expSmoothFit.forecast(len(valid_ts)).plot(ax=ax, style='--', linewidth=2, color='C0')  # 지수 평활법 예측값 플로팅

    plt.show()  # 그래프 출력