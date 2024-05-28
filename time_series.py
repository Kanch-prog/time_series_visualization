import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv('multiTimeline.csv', skiprows=1)
print(df.head(10))

df.info()

# renaming columns headers
df.columns = ['month', 'diet', 'gym', 'finance']

#turn the 'month' column into a DateTime data type and make it the index of the DataFrame.
df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)
print(df.head(10))


#plot data as 3 line plots on a single figure (one for each column, namely, 'diet', 'gym', and 'finance')
df.plot(figsize=(20, 10), linewidth=5, fontsize=20)
# Set the labels
plt.xlabel('Year', fontsize=20)
plt.ylabel('Values', fontsize=20)
# Show the plot
plt.show()

#by taking rolling average smooth noisa and seasonality for 'diet'
diet = df[['diet']]
diet.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);
plt.ylabel('Values', fontsize=20)
plt.show()

#by taking rolling average smooth noisa and seasonality for 'gym'
gym = df[['gym']]
gym.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);
plt.ylabel('Values', fontsize=20)
plt.show()

#comparing the two search terms above by plotting trends on a single frame
df_rm = pd.concat([diet.rolling(12).mean(), gym.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Values', fontsize=20)
plt.show()

#first-order differencing to remove trend to investigate seasonality
diet.diff().plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);

#compute correlation coefficients of all
print(df.corr())

#plot the first-order differences of these timeseries and compute the correlation
df.diff().plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);
plt.show()

print(df.diff().corr())

#plot the autocorrelation of the 'diet' series: on the x-axis, you have the lag and on the y-axis, you have how correlated the time series is with itself at that lag.
pd.plotting.autocorrelation_plot(diet)
plt.show()



