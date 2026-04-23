import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_traffic_data(num_sensors=10, duration_hours=24, time_interval_minutes=5):
    """
    Generates synthetic traffic monitoring data for a WSN.

    Args:
        num_sensors (int): Number of simulated WSN sensors.
        duration_hours (int): Total duration of data generation in hours.
        time_interval_minutes (int): Time interval between data points in minutes.

    Returns:
        pd.DataFrame: A DataFrame containing synthetic traffic data.
    """
    start_time = datetime(2025, 8, 21, 8, 0, 0) # Start at 8 AM
    end_time = start_time + timedelta(hours=duration_hours)

    data = []
    sensor_ids = [f'Sensor_{i+1:02d}' for i in range(num_sensors)]

    current_time = start_time
    while current_time <= end_time:
        for sensor_id in sensor_ids:
            # Simulate traffic volume (e.g., vehicles per interval)
            # Higher volume during peak hours (e.g., 7-9 AM, 4-6 PM)
            hour = current_time.hour
            if 7 <= hour <= 9 or 16 <= hour <= 18:
                traffic_volume = np.random.randint(50, 200) # Peak hours
            else:
                traffic_volume = np.random.randint(10, 100) # Off-peak hours

            # Simulate average speed (km/h)
            # Lower speed during peak hours
            if 7 <= hour <= 9 or 16 <= hour <= 18:
                avg_speed = np.random.randint(10, 40) # Peak hours
            else:
                avg_speed = np.random.randint(30, 70) # Off-peak hours

            # Simulate occupancy (percentage of time a lane is occupied)
            occupancy = np.random.uniform(0.1, 0.8) # Varies

            # Simulate temperature (for environmental sensing, optional)
            temperature = np.random.uniform(20, 35)

            data.append({
                'Timestamp': current_time,
                'Sensor_ID': sensor_id,
                'Traffic_Volume': traffic_volume,
                'Average_Speed_kmh': avg_speed,
                'Occupancy_percent': round(occupancy * 100, 2),
                'Temperature_C': round(temperature, 2)
            })
        current_time += timedelta(minutes=time_interval_minutes)

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    traffic_df = generate_traffic_data()
    print(traffic_df.head())
    traffic_df.to_csv('synthetic_traffic_data.csv', index=False)
    print("\nSynthetic traffic data saved to synthetic_traffic_data.csv")


