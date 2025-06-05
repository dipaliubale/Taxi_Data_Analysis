import pandas as pd
import matplotlib
matplotlib.use('GTK3Agg')

import matplotlib.pyplot as plt


green_columns = ['lpep_pickup_datetime', 'lpep_dropoff_datetime', 'PULocationID', 'DOLocationID', 'trip_distance', 'total_amount', 'congestion_surcharge']


yellow_columns = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'PULocationID', 'DOLocationID','trip_distance', 'total_amount', 'congestion_surcharge']


fhvhv_columns = ['pickup_datetime', 'dropoff_datetime', 'PULocationID', 'DOLocationID','trip_miles', 'base_passenger_fare','congestion_surcharge']

df_green = pd.read_parquet("green_tripdata_2024-01.parquet",columns = green_columns)
df_yellow = pd.read_parquet("yellow_tripdata_2024-01.parquet",columns = yellow_columns)
df_fhvhv = pd.read_parquet("fhvhv_tripdata_2024-01.parquet",columns = fhvhv_columns)
#df_fhv = pd.read_parquet("fhv_tripdata_2024-01.parquet")

#Number of rows
print(" Yellow Taxi rows:", len(df_yellow))
print("Total Green rows:", len(df_green))
print("fhvhv rows:",len(df_fhvhv))

df_fhv = pd.read_parquet("fhv_tripdata_2024-01.parquet")
df_fhvhv['trip_distance'] = df_fhvhv['trip_miles']

#calculating trip duration
df_green["trip_duration_minutes"] = (df_green["lpep_dropoff_datetime"] - df_green["lpep_pickup_datetime"]).dt.total_seconds() / 60

df_yellow["trip_duration_minutes"] = (df_yellow["tpep_dropoff_datetime"] - df_yellow["tpep_pickup_datetime"]).dt.total_seconds() / 60

df_fhvhv["trip_duration_minutes"] = (df_fhvhv["dropoff_datetime"] - df_fhvhv["pickup_datetime"]).dt.total_seconds() / 60

df_fhvhv["total_amount"] = df_fhvhv["base_passenger_fare"] 

#getting common columns
common_columns = set(df_yellow.columns) & set(df_green.columns) & set(df_fhvhv.columns)
print("Common Columns in All Three DataFrames:", common_columns)

common_columns = ['total_amount', 'DOLocationID', 'PULocationID', 'trip_duration_minutes', 'congestion_surcharge', 'trip_distance']


df_yellow_common = df_yellow[common_columns].copy()
df_green_common = df_green[common_columns].copy()
df_fhvhv_common = df_fhvhv[common_columns].copy()  

df_yellow_common["taxi_type"] = "yellow"
df_green_common["taxi_type"] = "green"
df_fhvhv_common["taxi_type"] = "fhvhv"

df_all = pd.concat([df_yellow_common,df_green_common,df_fhvhv_common])

summary = df_all.groupby("taxi_type")[["total_amount", "trip_distance","trip_duration_minutes"]].sum()

summary["avg_amount_per_mile"] = summary["total_amount"] / summary["trip_distance"]
summary["avg_speed"] = summary["trip_distance"] / summary["trip_duration_minutes"]

summary = summary.sort_values("avg_amount_per_mile")

print(summary)

# bar plot for speed
#summary['avg_speed'].plot(kind='bar',title = "Average Speed Mile/h by Taxi type")
#plt.savefig("taxi_avg_speed_per_milehour_plot.png")
#plt.show()

#bar plot for fair amount
summary['avg_amount_per_mile'].plot(kind='bar',title = "Average Speed Mile/h by Taxi type")
plt.savefig("taxi_avg_amount_per_mile_plot.png")
print("Plot saved ")

plt.show()


