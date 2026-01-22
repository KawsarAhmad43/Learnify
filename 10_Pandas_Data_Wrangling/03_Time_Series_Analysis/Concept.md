# Time Series Analysis with Pandas

## 1. DateTimeIndex
To perform time series analysis, the index of your DataFrame should be a `DatetimeIndex`.
```python
df.index = pd.to_datetime(df['Date'])
```

## 2. Resampling
Change the frequency of your time series (e.g., from Days to Months).
*   **Downsampling**: Aggregating data (e.g., Daily -> Monthly Mean).
*   **Upsampling**: Expanding data (e.g., Monthly -> Daily), often requires filling (interpolation).

```python
# Calculate monthly mean
df.resample('M').mean()
```

## 3. Rolling Windows
Perform calculations on a sliding window of data. Useful for smoothing or finding trends.
```python
# 7-day moving average
df['Price'].rolling(window=7).mean()
```

## 4. Shifting
Shift data forward or backward in time. Useful for calculating differences (lag/lead).
```python
# Calculate daily change
df['Change'] = df['Price'] - df['Price'].shift(1)
```
