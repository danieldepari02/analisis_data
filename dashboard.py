import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")

day_df = pd.read_csv("https://raw.githubusercontent.com/danieldepari02/analisis_data/main/day.csv")
day_df
hour_df = pd.read_csv("https://raw.githubusercontent.com/danieldepari02/analisis_data/main/hour.csv")
hour_df
dteday_columns = ["dteday"]
 
for column in dteday_columns:
  day_df[column] = pd.to_datetime(day_df[column])
dteday_columns = ["dteday"]
 
for column in dteday_columns:
  hour_df[column] = pd.to_datetime(hour_df[column])

df_time = day_df.copy()
df = df_time.copy()


df['weekday'] = df['weekday'].map({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'})



pivot_weekday = df.groupby(by=["weekday"]).agg({
    "cnt": "mean"
}).reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).reset_index()

pd.options.display.float_format = '{:.2f}'.format
print("\n===============================================\n")
print("Average Bike Renting number for each day")
print(pivot_weekday.to_string(index=False))
print("\n===============================================\n")

df = df_time.copy()


df['weathersit'] = df['weathersit'].map({1: 'Clear', 2: 'Cloudy', 3: 'Light Rain', 4: 'Heavy Rain'})
df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})


weathersit_order = ['Clear', 'Cloudy', 'Light Rain', 'Heavy Rain']
season_order = ['Spring', 'Summer', 'Fall', 'Winter']


pivot_weathersit = df.groupby(by=["weathersit"]).agg({
    "cnt": "mean"
}).reindex(weathersit_order, fill_value=0).reset_index()
pivot_season = df.groupby(by=["season"]).agg({
    "cnt": "mean"
}).reindex(season_order, fill_value=0).reset_index()


pd.options.display.float_format = '{:.2f}'.format
print("Average Bike Renting towards weather:")
print(pivot_weathersit.to_string(index=False))
print("\n===============================================\n")
print("Average Bike Renting towards season :")
print(pivot_season.to_string(index=False))

df_time = hour_df.copy()
df = df_time.copy()


df['hr'] = df['hr'].map({0: '00.00', 1: '01.00', 2: '02.00', 3: '03.00', 4: '04.00', 5: '05.00', 6: '06.00', 7: '07.00', 8: '08.00', 9: '09.00', 10: '10.00', 11: '11.00', 12: '12.00', 13: '13.00', 14: '14.00', 15: '15.00', 16: '16.00', 17: '17.00', 18: '18.00', 19: '19.00', 20: '20.00', 21: '21.00', 22: '22.00', 23: '23.00'})
hr_order = ['00.00', '01.00', '02.00', '03.00', '04.00', '05.00', '06.00', '07.00', '08.00', '09.00', '10.00', '11.00', '12.00', '13.00', '14.00', '15.00', '16.00', '17.00', '18.00', '19.00', '20.00', '21.00', '22.00', '23.00']

pivot_hr = df.groupby(by=["hr"]).agg({
    "cnt": "mean"
}).reindex(hr_order, fill_value=0).reset_index()


pd.options.display.float_format = '{:.2f}'.format
print("\n===============================================\n")
print("Average Bike Renting number for each hour")
print(pivot_hr.to_string(index=False))
print("\n===============================================\n")

plt.figure(figsize=(10, 6))
plt.plot(pivot_weekday['weekday'], pivot_weekday['cnt'], marker='o', color='green', linestyle='-')
plt.title('Average Bike Renting Number for Each Day')
plt.xlabel('Day')
plt.ylabel('Average Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()

df = df_time.copy()

df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['yr'] = df['yr'].map({0: '2011', 1: '2012'})


pivot_season_year = df.groupby(['season', 'yr'])['cnt'].sum().reset_index()
x = pivot_season_year['season'].unique()
y1 = pivot_season_year[pivot_season_year['yr'] == '2011']['cnt']
y2 = pivot_season_year[pivot_season_year['yr'] == '2012']['cnt']

plt.figure(figsize=(10, 6))
plt.bar(x, y1, color='skyblue', label='2011', width=0.4, alpha=0.8)
plt.bar(x, y2, bottom=y1, color='salmon', label='2012', width=0.4, alpha=0.8)

plt.xlabel('Season')
plt.ylabel('Bike Renting (Juta)')
plt.title('Bike Renting according Year and Season')
plt.legend(title='Year')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(pivot_hr['hr'], pivot_hr['cnt'], marker='o', color='skyblue', linestyle='-')
plt.title('Average Bike Renting Number for Each Hour')
plt.xlabel('Hour')
plt.ylabel('Average Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()