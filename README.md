Project Description: Analyzing Google Trends Data for 'Diet', 'Gym', and 'Finance'

In this project, we analyze the Google Trends data for three search terms: 'diet', 'gym', and 'finance'. The data is monthly and spans several years, making it a good candidate for time series analysis to understand trends, seasonality, and correlations among these search terms. The key steps and observations in the project are outlined below.

Steps

1. We start by loading the data from a CSV file and inspecting its structure.
Initial inspection of the first few rows and the data types of the columns reveals that the 'month' column is of type object and needs to be converted to a DateTime format.

2. Convert the 'month' column to a DateTime data type and set it as the index of the DataFrame. This allows us to handle the data as a time series.

3.Plot the time series data for 'diet', 'gym', and 'finance' to observe the general trends and patterns.
Observation: The plots show noticeable seasonality, particularly in the 'diet' series, which spikes every January.
![Figure_1](https://github.com/Kanch-prog/time_series_visualization/assets/121807277/872f5c20-ee75-4008-9399-ea7927e7f7e3)

4.Calculate and plot the rolling averages for 'diet' and 'gym' with a window size of 12 months to smooth out noise and highlight trends.
Observation: The 'diet' series shows clear yearly seasonality, while the 'gym' series shows a more consistent upward trend.

5. Plot the rolling averages of 'diet' and 'gym' on the same figure to compare their trends.
Observation: 'Diet' shows periodic spikes, while 'gym' demonstrates a steady increase over time, indicating different underlying patterns.
![Figure_2](https://github.com/Kanch-prog/time_series_visualization/assets/121807277/266795df-0ed7-4947-a510-ed150af09fc7)

6.Apply first-order differencing to the 'diet' series to remove the trend and better investigate seasonality.
Observation: The differenced plot highlights the seasonality with clear peaks every January, indicating a strong seasonal component.
![Figure_3](https://github.com/Kanch-prog/time_series_visualization/assets/121807277/0b597e95-094b-4db5-8630-8b0fd86d7ff4)

7.Compute and compare the correlation coefficients of the original series and their first-order differences.
Observation: The original series shows negative correlation between 'diet' and 'gym', but the differenced series shows a high positive correlation, indicating that their seasonal components are correlated.
![Figure_4](https://github.com/Kanch-prog/time_series_visualization/assets/121807277/6960795f-fecf-44fa-a877-7a76523c6a35)
![Figure_6](https://github.com/Kanch-prog/time_series_visualization/assets/121807277/bceb03f1-2eea-4d91-85bc-5c922f7c4bf1)

8.Plot the autocorrelation of the 'diet' series to identify periodicity.
Observation: The autocorrelation plot shows significant peaks at lags of 12 months, 24 months, and 36 months, confirming the yearly seasonality of the 'diet' series.
![Figure_5](https://github.com/Kanch-prog/time_series_visualization/assets/121807277/cac82551-f107-4eac-9306-3db57934e232)

Summary of findings: 
      Seasonality: The 'diet' series exhibits strong yearly seasonality with peaks every January, likely due to New Year's resolutions.
      Trends: The 'gym' series shows a steady upward trend, indicating increasing interest over time.
      Correlation: While 'diet' and 'gym' are negatively correlated when considering both trend and seasonality, their seasonal components are positively correlated.
      Autocorrelation: The 'diet' series is autocorrelated with itself at a lag of 12 months, confirming its yearly periodicity
