import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def plot_combined_chart(data):
    # Group data by 'n' for the candlestick chart
    grouped = data.groupby('n')['rounds']
    summary = grouped.agg(
        min='min',
        q1=lambda x: x.quantile(0.25),
        median='median',
        q3=lambda x: x.quantile(0.75),
        max='max'
    ).reset_index()
    stats_data = grouped.agg(
        mean='mean',
        median='median',
        mode=lambda x: x.mode().iloc[0]
    ).reset_index()
    
    # Initialize the plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Candlestick plot
    # Plotting the box for interquartile range
    # ax.bar(summary['n'], summary['q3'] - summary['q1'], bottom=summary['q1'], width=3, color='skyblue', edgecolor='black')
    # Lines for max and min
    # ax.vlines(summary['n'], summary['min'], summary['max'], color='black', linewidth=1.5)

    # Regression plots on the same axis
    sns.regplot(x='n', y='mean', data=stats_data, ax=ax, label='Mean Regression', ci=None, scatter_kws={"s": 10}, line_kws={"color":"red", "linewidth": 1.5})
    sns.regplot(x='n', y='median', data=stats_data, ax=ax, label='Median Regression', ci=None, scatter_kws={"s": 10}, line_kws={"color":"green", "linewidth": 1.5})
    sns.regplot(x='n', y='mode', data=stats_data, ax=ax, label='Mode Regression', ci=None, scatter_kws={"s": 10}, line_kws={"color":"blue", "linewidth": 1.5})
    
    # Setting labels and titles
    ax.set_xlabel('n')
    ax.set_ylabel('Rounds')
    ax.set_title('Combined Candlestick and Regression Analysis for Rounds per N')
    
    # Legend and grid
    ax.legend()
    ax.grid(True)

    plt.show()

# Sample usage with commented execution
data = load_data('round_data_1_100_1.csv')
plot_combined_chart(data)