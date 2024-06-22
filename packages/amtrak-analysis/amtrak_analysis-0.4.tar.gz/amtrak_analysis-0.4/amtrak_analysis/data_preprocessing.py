import pandas as pd
import pkg_resources

def load_amtrak_data(file_path=None):
    """Amtrak 데이터를 로드하고 전처리"""
    if file_path is None:
        # 패키지 내부의 기본 CSV 파일 경로 설정
        file_path = pkg_resources.resource_filename('amtrak_analysis', 'data/Amtrak.csv')
    Amtrak_df = pd.read_csv(file_path)  # CSV 파일에서 데이터 읽기
    Amtrak_df['Date'] = pd.to_datetime(Amtrak_df.Month, format='%d/%m/%Y')  # 'Month' 열을 datetime 형식으로 변환하여 'Date' 열에 저장
    ridership_ts = pd.Series(Amtrak_df.Ridership.values, index=Amtrak_df.Date, name='Ridership')  # 시계열 데이터 생성
    ridership_ts.index = pd.DatetimeIndex(ridership_ts.index, freq=ridership_ts.index.inferred_freq)  # 인덱스에 빈도 설정
    return ridership_ts  # 전처리된 시계열 데이터 반환