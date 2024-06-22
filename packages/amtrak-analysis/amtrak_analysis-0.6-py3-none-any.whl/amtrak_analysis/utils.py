import pandas as pd
import matplotlib.pyplot as plt

def singleGraphLayout(ax, ylim, train_df, valid_df):
    """단일 그래프의 레이아웃을 설정"""
    ax.set_xlim('1990', '2004-6')  # x축 범위 설정
    ax.set_ylim(*ylim)  # y축 범위 설정
    ax.set_xlabel('Time')  # x축 레이블 설정

    one_month = pd.Timedelta('31 days')  # 한 달을 나타내는 시간 델타
    xtrain = (min(train_df.index), max(train_df.index) - one_month)  # 훈련 데이터 구간 설정
    xvalid = (min(valid_df.index) + one_month, max(valid_df.index) - one_month)  # 검증 데이터 구간 설정
    xtv = xtrain[1] + 0.5 * (xvalid[0] - xtrain[1])  # 훈련과 검증 데이터 구간의 경계 설정
    ypos = 0.9 * ylim[1] + 0.1 * ylim[0]  # y축 상한 설정

    ax.add_line(plt.Line2D(xtrain, (ypos, ypos), color='black', linewidth=0.5))  # 훈련 데이터 구간 선 추가
    ax.add_line(plt.Line2D(xvalid, (ypos, ypos), color='black', linewidth=0.5))  # 검증 데이터 구간 선 추가
    ax.axvline(x=xtv, ymin=0, ymax=1, color='black', linewidth=0.5)  # 훈련과 검증 데이터 경계선 추가
    ypos = 0.925 * ylim[1] + 0.075 * ylim[0]  # y축 상한 조정

    ax.text('1995', ypos, 'Training')  # 'Training' 텍스트 추가
    ax.text('2002-3', ypos, 'Validation')  # 'Validation' 텍스트 추가

def graphLayout(axes, train_df, valid_df):
    """여러 그래프의 레이아웃을 설정"""
    singleGraphLayout(axes[0], [1300, 2550], train_df, valid_df)  # 첫 번째 축의 레이아웃 설정
    singleGraphLayout(axes[1], [-550, 550], train_df, valid_df)  # 두 번째 축의 레이아웃 설정

    train_df.plot(y='Ridership', ax=axes[0], color='C0', linewidth=0.75)  # 훈련 데이터 플로팅
    valid_df.plot(y='Ridership', ax=axes[0], color='C0', linestyle='dashed', linewidth=0.75)  # 검증 데이터 플로팅 (점선으로)

    axes[1].axhline(y=0, xmin=0, xmax=1, color='black', linewidth=0.5)  # 두 번째 축에 0 기준선 추가
    axes[0].set_xlabel('')  # 첫 번째 축의 x축 레이블 제거
    axes[0].set_ylabel('Ridership (in 000s)')  # 첫 번째 축의 y축 레이블 설정
    axes[1].set_ylabel('Forecast Errors')  # 두 번째 축의 y축 레이블 설정

    if axes[0].get_legend():
        axes[0].get_legend().remove()  # 첫 번째 축의 범례 제거