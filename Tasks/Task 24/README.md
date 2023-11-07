# Session : 1/11/2023

## 5 Examples of different cases of Seasonality of time series analysis

1. Weather\
    Time series analysis is also used frequently by weatherman to predict what the temperatures will be during different months and seasons throughout the year.

   > `Temperature Seasonality` : there are distinct seasonal temperature patterns. For instance, you might observe colder temperatures during the winter and warmer temperatures during the summer, leading to a seasonal oscillation in temperature data.

2. Hotel Occupancy Rate\
    The occupancy rate in hotels can exhibit clear seasonal patterns.

   > `Holiday Season` : Hotels often experience higher occupancy rates during holiday seasons and vacation periods. For instance, in many tourist destinations, you'll see increased bookings during summer holidays or major cultural and festive holidays like Christmas and New Year's.

   > `Seasonal Tourism`: Many tourist destinations have distinct high and low seasons due to weather conditions or specific attractions. For example, ski resorts tend to have higher occupancy during the winter season, while beach resorts may have higher occupancy in the summer.

3. Ice Cream Sales\
    The consumption of specific food and beverage items can exhibit clear seasonality patterns due to various factors.

   > `Weather-Related Seasonality`: Ice cream sales often follow a seasonal pattern influenced by temperature and weather conditions. In many regions, ice cream consumption tends to be higher during the warm summer months when people seek ways to cool down.

   > `Holiday Season`: Seasonal holidays often lead to increased ice cream sales as it's a popular treat for celebrations and gatherings during the summer.

4. Clothing Sales
   > `Seasonal Fashion Collections`: The fashion industry typically operates on a seasonal basis, with designers and retailers releasing new clothing collections for spring, summer, fall, and winter. Each season's collection corresponds to the upcoming weather and style trends, leading to seasonal fluctuations in clothing sales.
5. Airline Passenger Traffic
   > `Holiday and Vacation Season`: The airline industry experiences clear seasonality related to holidays and vacation periods. During holiday seasons, such as Thanksgiving, Christmas, or summer vacations, there is a surge in passenger traffic as people travel to visit family and friends or go on vacation.

## Machine learning models that is used in time series analysis

- Autoregressive (AR)
- Integrated (I)
- Moving Average(MA)
- Autoregressive Moving Average (ARMA)
- Autoregressive Integrated Moving Average (ARIMA)
- VAR (Vector Autoregression)
- Long Short-Term Memory (LSTM)

## ACF vs PACF

### Auto-Correlation Function (ACF)

ACF measures the correlation between a time series and its lagged values at different time lags. It quantifies the linear relationship between the series at time 't' and the series at time 't-k', where 'k' is the lag.

**Interpretation:**

- Peaks or troughs in the ACF plot indicate the presence of periodic patterns or seasonality in the data.

**Purpose:**

- ACF is useful for determining the order of the moving average (MA) component in an ARIMA model. The number of significant lags in the ACF plot can provide insights into the order of the MA component.

### Partial Auto-Correlation Function (PACF)

PACF measures the correlation between a time series and its lagged values while controlling for the intermediate lags. It quantifies the direct linear relationship between the series at time 't' and the series at time 't-k', where 'k' is the lag, after removing the effects of the intermediate lags.

**Interpretation:**

- PACF helps you understand the direct or instantaneous correlation between the series at different lags. It can reveal the number of lags at which autocorrelation drops to near-zero after controlling for the effects of the intermediate lags.

**Purpose:**

- PACF is useful for determining the order of the autoregressive (AR) component in an ARIMA model. The number of significant lags in the PACF plot can provide insights into the order of the AR component.
