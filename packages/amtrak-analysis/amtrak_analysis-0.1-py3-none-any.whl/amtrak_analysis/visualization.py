import matplotlib.pyplot as plt

def plot_moving_averages(ts, ma_centered, ma_trailing):
    """Plot original time series with moving averages."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ts.plot(ax=ax, color='black', linewidth=0.25)
    ma_centered.plot(ax=ax, linewidth=2)
    ma_trailing.plot(ax=ax, style='--', linewidth=2)
    ax.set_xlabel('Time')
    ax.set_ylabel('Ridership')
    ax.legend(['Ridership', 'Centered Moving Average', 'Trailing Moving Average'])
    plt.show()

def plot_trailing_average(train_ts, valid_ts, ma_trailing, ma_trailing_pred):
    """Plot trailing average and prediction with residuals."""
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(9, 7.5))
    ma_trailing.plot(ax=axes[0], linewidth=2, color='C1')
    ma_trailing_pred.plot(ax=axes[0], linewidth=2, color='C1', linestyle='dashed')

    residual = train_ts - ma_trailing
    residual.plot(ax=axes[1], color='C1')
    
    residual = valid_ts - ma_trailing_pred
    residual.plot(ax=axes[1], color='C1', linestyle='dashed')

    plt.show()