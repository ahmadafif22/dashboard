import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
# Aktifkan mode interaktif
plt.ion()
sns.set(style='dark')
def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='order_date').agg({
        "order_id": "nunique",
        "total_price": "sum"
    })
    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df.rename(columns={
        "order_id": "order_count",
        "total_price": "revenue"
    }, inplace=True)
    
    return daily_orders_df
def create_sum_order_items_df(df):
    sum_order_items_df = df.groupby("product_name").quantity_x.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df
def create_bygender_df(df):
    bygender_df = df.groupby(by="gender").customer_id.nunique().reset_index()
    bygender_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    
    return bygender_df
def create_byage_df(df):
    byage_df = df.groupby(by="age_group").customer_id.nunique().reset_index()
    byage_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    byage_df['age_group'] = pd.Categorical(byage_df['age_group'], ["Youth", "Adults", "Seniors"])
    
    return byage_df
def create_bystate_df(df):
    bystate_df = df.groupby(by="state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    
    return bystate_df
def create_rfm_df(df):
    rfm_df = df.groupby(by="customer_id", as_index=False).agg({
        "order_date": "max", #mengambil tanggal order terakhir
        "order_id": "nunique",
        "total_price": "sum"
    })
    rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]
    
    rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
    recent_date = df["order_date"].dt.date.max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
    
    return rfm_df
all_df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\afif submision\dashboard\all_data.csv")
day_df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\afif submision\dashboard\all_data.csv")

hour_df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\afif submision\dashboard\all_data.csv")

season_counts = hour_df.groupby('season')['cnt'].mean()
#convert data
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

day_df['day_of_week'] = day_df['dteday'].dt.day_name()

rentals_by_day = day_df.groupby('day_of_week')['cnt'].mean()
day_df.head()
hour_df.head()

#grafik 1
import pandas as pd
import numpy as np
import matplotlib
import multiprocessing
matplotlib.use('agg')
import matplotlib.pyplot as plt
matplotlib.pyplot.ion()
plt.pause(0.01)
# Aktifkan mode interaktif
plt.ion()

# Buat dan tampilkan plot
plt.figure(figsize=(8,6))
# ... kode plotting ...
plt.show()

# Membaca file CSV dengan menentukan tipe data yang tepat
all_df = pd.read_csv(r'/dashboard/all_data.csv', 
                     low_memory=False)

import pandas as pd

# Load data
df = pd.read_csv(r'C:\Users\ASUS\OneDrive\Documents\afif submision\data\day.csv')

# Group by weekday and count the number of rentals
weekday_rentals = df.groupby('weekday')['cnt'].sum()

# Print the result
print(weekday_rentals)
hari_dict = {0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'}

weekday_rentals.index = weekday_rentals.index.map(hari_dict)


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Plot the data
plt.plot(weekday_rentals.values)

# Set title and labels
plt.title('Daily Bike Rentals in Washington D.C.')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Rentals')

# Set x-axis tick labels
plt.xticks(range(7), weekday_rentals.index)

plt.ion()
# ... kode plotting Anda ...
plt.savefig('chart1.png')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Plot the data
plt.bar(weekday_rentals.index, weekday_rentals.values)

# Set title and labels
plt.title('Daily Bike Rentals in Washington D.C.')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Rentals')

plt.ion()
# ... kode plotting Anda ...
plt.savefig('line1.png')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Plot the data
plt.pie(weekday_rentals.values, labels=weekday_rentals.index, autopct='%1.1f%%')

# Set title
plt.title('Daily Bike Rentals in Washington D.C.')

plt.ion()
# ... kode plotting Anda ...
plt.savefig('pie1.png')


# Set x-axis tick labels
plt.xticks(range(7), weekday_rentals.index)

    
#chart2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Muat data
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\afif submision\data\day.csv")

# Eksplorasi data
print(df.head())
print(df.info())
print(df.describe())

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Cuaca vs. Jumlah Penyewaan Sepeda
plt.figure(figsize=(8,6))
sns.countplot(x='weathersit', data=df)
plt.title('Cuaca vs. Jumlah Penyewaan Sepeda')
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Penyewaan')
plt.ion()
# ... kode plotting Anda ...
plt.savefig('chart2.png')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Group by weathersit_x and count the number of rentals
weather_rentals = df.groupby('weathersit')['cnt'].sum()

# Plot the data
plt.figure(figsize=(8,6))
plt.plot(weather_rentals.index, weather_rentals.values)
plt.xlabel('Weather Situation')
plt.ylabel('Number of Rentals')
plt.title('Weather Situation vs. Bike Rentals')
plt.ion()
# ... kode plotting Anda ...
plt.savefig('line2.png')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Group by weathersit_x and count the number of rentals
weather_rentals = df.groupby('weathersit')['cnt'].sum()

# Plot the data
plt.figure(figsize=(8,6))
plt.pie(weather_rentals.values, labels=weather_rentals.index, autopct='%1.1f%%')
plt.title('Weather Situation vs. Bike Rentals')
plt.ion()
# ... kode plotting Anda ...
plt.savefig('pie2.png')
