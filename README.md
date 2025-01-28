# CSC 1019 Practice 04
In this practice you will perform a bit of mini data analysis, but more importantly, you will get more practice with lists and breaking problems down into functions.

You will receive a series of values representing hourly Air Quality Index readings (AQI). The AQI is a measure of how clean the air is using various measurements (PM 2.5, Ozone, CO2, etc.). The following table links AQI values to descriptions.

| Air Quality Index | Air quality description |
| ---      | ---                     |
| 0-50     | Good                    |
| 51 - 100 | Moderate                |
| 101 - 150 | Unhealthy for sensitive groups |
| 151 - 200 | Unhealthy              |
| 201-300   | Very unhealthy         |
| 301 - 500 | Hazardous              |


## Input
You will receive input on the console.
1. The first value you receive will be an integer representing the number of AQI values to expect.
2. Each AQI will be an integer on a separate line.

### Example
```
10
50
51
100
150
125
93
60
56
45
50
```

## Output
You will output the number of readings, maximum, minimum, and average of the values (to the nearest whole number), the number of readings below and above the average, along with a description of the average value using the table above.
**You must output in the EXACT format below.**
```
Readings: 10
Min: 45
Max: 150
Average: 78
Readings Below Average: 6
Readings Above Average: 4
Description: Moderate
```
## Restrictions
Do not use Python's built-in `max()` or `min()` functions. Yes, in the real world, I want you to use them. However, I want you to be familiar with the algorithms needed to figure out the maximum and minimum values of a list. In fact, these should be separate functions.
