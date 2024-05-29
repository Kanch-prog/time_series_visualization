# Analyzing Google Trends Data for 'Diet', 'Gym', and 'Finance'

![Status](https://img.shields.io/badge/status-active-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![Python](https://img.shields.io/badge/python-3.8%2B-blue)

In this project, we analyze the Google Trends data for three search terms: **'diet'**, **'gym'**, and **'finance'**. The data is monthly and spans several years, making it a good candidate for time series analysis to understand trends, seasonality, and correlations among these search terms. The key steps and observations in the project are outlined below.

## Steps

1. **Load the Data**
   - We start by loading the data from a CSV file and inspecting its structure.
   - Initial inspection of the first few rows and the data types of the columns reveals that the 'month' column is of type object and needs to be converted to a DateTime format.

2. **Convert 'month' Column**
   - Convert the 'month' column to a DateTime data type and set it as the index of the DataFrame. This allows us to handle the data as a time series.

3. **Plot Time Series Data**
   - Plot the time series data for 'diet', 'gym', and 'finance' to observe the general trends and patterns.
   - **Observation:** The plots show noticeable seasonality, particularly in the 'diet' series, which spikes every January.
   - ![Figure 1](url_to_figure_1)

4. **Calculate and Plot Rolling Averages**
   - Calculate and plot the rolling averages for 'diet' and 'gym' with a window size of 12 months to smooth out noise and highlight trends.
   - **Observation:** The 'diet' series shows clear yearly seasonality, while the 'gym' series shows a more consistent upward trend.

5. **Compare Rolling Averages**
   - Plot the rolling averages of 'diet' and 'gym' on the same figure to compare their trends.
   - **Observation:** 'Diet' shows periodic spikes, while 'gym' demonstrates a steady increase over time, indicating different underlying patterns.
   - ![Figure 2](url_to_figure_2)

6. **First-Order Differencing**
   - Apply first-order differencing to the 'diet' series to remove the trend and better investigate seasonality.
   - **Observation:** The differenced plot highlights the seasonality with clear peaks every January, indicating a strong seasonal component.
   - ![Figure 3](url_to_figure_3)

7. **Compute and Compare Correlations**
   - Compute and compare the correlation coefficients of the original series and their first-order differences.
   - **Observation:** The original series shows negative correlation between 'diet' and 'gym', but the differenced series shows a high positive correlation, indicating that their seasonal components are correlated.
   - ![Figure 4](url_to_figure_4) ![Figure 6](url_to_figure_6)

8. **Plot Autocorrelation**
   - Plot the autocorrelation of the 'diet' series to identify periodicity.
   - **Observation:** The autocorrelation plot shows significant peaks at lags of 12 months, 24 months, and 36 months, confirming the yearly seasonality of the 'diet' series.
   - ![Figure 5](url_to_figure_5)

## Summary of Findings

- **Seasonality:** The 'diet' series exhibits strong yearly seasonality with peaks every January, likely due to New Year's resolutions.
- **Trends:** The 'gym' series shows a steady upward trend, indicating increasing interest over time.
- **Correlation:** While 'diet' and 'gym' are negatively correlated when considering both trend and seasonality, their seasonal components are positively correlated.
- **Autocorrelation:** The 'diet' series is autocorrelated with itself at a lag of 12 months, confirming its yearly periodicity.

## Badges

![GitHub repo size](https://img.shields.io/github/repo-size/Kanch-prog/time_series_visualization) ![GitHub issues](https://img.shields.io/github/issues/Kanch-prog/time_series_visualization) ![GitHub pull requests](https://img.shields.io/github/issues-pr/Kanch-prog/time_series_visualization)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author:** Your Name
- **Email:** your.email@example.com
- **GitHub:** [your_username](https://github.com/Kanch-prog)
