import pandas as pd

df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)

df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
