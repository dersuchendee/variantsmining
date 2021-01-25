import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv("slopeSP.csv", header= 0)

df['RelFreq1'] = df['Chapter I'] /  df['Chapter I'].sum()
df['RelFreq1'] = df['RelFreq1'].multiply(100)

df['RelFreq2'] = df['Chapter II'] /  df['Chapter II'].sum()
df['RelFreq2'] = df['RelFreq2'].multiply(100)

df['RelFreq3'] = df['Chapter III'] /  df['Chapter III'].sum()
df['RelFreq3'] = df['RelFreq3'].multiply(100)

df['RelFreq4'] = df['Chapter IV'] /  df['Chapter IV'].sum()
df['RelFreq4'] = df['RelFreq4'].multiply(100)

df['RelFreq5'] = df['Chapter V'] /  df['Chapter V'].sum()
df['RelFreq5'] = df['RelFreq5'].multiply(100)

df['RelFreq6'] = df['Chapter VI'] /  df['Chapter VI'].sum()
df['RelFreq6'] = df['RelFreq6'].multiply(100)

df['RelFreq7'] = df['Chapter VII'] /  df['Chapter VII'].sum()
df['RelFreq7'] = df['RelFreq7'].multiply(100)

df['RelFreq8'] = df['Chapter VIII'] /  df['Chapter VIII'].sum()
df['RelFreq8'] = df['RelFreq8'].multiply(100)

df.to_csv('relfreq_SP.csv')