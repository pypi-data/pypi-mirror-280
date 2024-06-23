import matplotlib.pyplot as plt

def plot_moving_averages(ridership_ts, ma_centered, ma_trailing):
    fig, ax = plt.subplots(figsize=(8, 7))
    ridership_ts.plot(ax=ax, color='black', linewidth=0.25)
    ma_centered.plot(ax=ax, linewidth=2)
    ma_trailing.plot(ax=ax, style='--', linewidth=2)
    ax.set_xlabel('Time')
    ax.set_ylabel('Ridership')
    ax.legend(['Ridership', 'Centered Moving Average', 'Trailing Moving Average'])
    plt.show()

def plot_forecasts(train_ts, valid_ts, ma_trailing, ma_trailing_pred, residual_train, residual_valid):
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(9, 7.5))
    ma_trailing.plot(ax=axes[0], linewidth=2, color='C1')
    ma_trailing_pred.plot(ax=axes[0], linewidth=2, color='C1', linestyle='dashed')
    residual_train.plot(ax=axes[1], color='C1')
    residual_valid.plot(ax=axes[1], color='C1', linestyle='dashed')
    axes[0].set_title('Trailing Moving Average & Forecast')
    axes[1].set_title('Residuals')
    for ax in axes:
        ax.set_xlabel('Time')
    plt.tight_layout()
    plt.show()