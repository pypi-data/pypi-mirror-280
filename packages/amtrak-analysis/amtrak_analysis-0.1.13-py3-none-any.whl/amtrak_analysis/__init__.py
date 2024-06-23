import pkg_resources
from .analysis import AmtrakAnalysis

def create_default_analysis():
    csv_path = pkg_resources.resource_filename(__name__, 'data/Amtrak.csv')
    return AmtrakAnalysis(csv_path)

def calculate_moving_averages():
    analysis = create_default_analysis()
    ma_centered, ma_trailing = analysis.calculate_moving_averages()
    print(ma_centered.head())
    print(ma_trailing.head())
    analysis.plot_moving_averages()

def split_data(n_valid=36):
    analysis = create_default_analysis()
    train_ts, valid_ts = analysis.split_data(n_valid)
    print(train_ts.head())
    print(valid_ts.head())

def trailing_moving_average_forecast():
    analysis = create_default_analysis()
    train_ts, valid_ts = analysis.split_data()
    ma_trailing, ma_trailing_pred = analysis.trailing_moving_average_forecast(train_ts, valid_ts)
    print(ma_trailing.head())
    print(ma_trailing_pred.head())

def calculate_residuals():
    analysis = create_default_analysis()
    train_ts, valid_ts = analysis.split_data()
    ma_trailing, ma_trailing_pred = analysis.trailing_moving_average_forecast(train_ts, valid_ts)
    residual_train, residual_valid = analysis.calculate_residuals(train_ts, ma_trailing, valid_ts, ma_trailing_pred)
    print(residual_train.head())
    print(residual_valid.head())

def run_analysis(n_valid=36):
    analysis = create_default_analysis()
    analysis.run_analysis(n_valid)

def plot_forecasts(n_valid=36):
    analysis = create_default_analysis()
    analysis.plot_forecasts(n_valid)

def compare_smoothing_methods(alpha=0.2):
    analysis = create_default_analysis()
    analysis.compare_smoothing_methods(alpha)