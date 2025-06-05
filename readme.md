#Project Partners
	Shraddha Jagtap (23111019)
	Dipali Ubale (23111013)

# Data links

I] 2024 January :-

1] Yellow taxi
https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet

2] Green taxi
https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2024-01.parquet

3] For_hire_vehicle_trip
https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2024-01.parquet

	
#Problem Statement -: 

# NYC Taxi Data Analysis 

This project analyzes trip records from NYC taxi services including Yellow, Green, and FHVHV (For-Hire Vehicle High Volume). The goal is to compare different taxi types based on trip distance, duration, pickup/drop time, and pricing for finding efficient taxi for the customer.

---

## Dataset Used

- **Yellow Taxi**
- **Green Taxi**
- **FHVHV Taxi**

Each dataset contains:

- `dropoff_datetime` : drop time
- `pickup_datetime` : pickup time
- `trip_distance`: Total trip distance in miles
- `trip_duration_minutes`: Trip duration (derived from timestamps)
- `total_amount`: Total fare amount

---

##  Objectives

- Clean and filter data for meaningful analysis
- find common columns across all datasets
- Merge datasets based on common columns
- Calculate average amount per mile
- Calculate average speed mile/hour
- Visualize comparison between taxi types

---

## Tools Used

- Python 
- Pandas
- Matplotlib 

---

##  Key Visualizations

- Bar chart showing **average fare per mile** by taxi type
- Bar chart showing **average speed mile/hour** by taxi type

---

##Run the code

python3 taxi.py

---


