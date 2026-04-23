import pandas as pd
import matplotlib.pyplot as plt

def analyze_traffic_data(file_path="synthetic_traffic_data.csv"):
    """
    Analyzes the synthetic traffic monitoring data and generates visualizations.

    Args:
        file_path (str): Path to the CSV file containing the traffic data.
    """
    try:
        df = pd.read_csv(file_path)
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    print("\n--- Data Overview ---")
    print(df.info())
    print("\n--- Descriptive Statistics ---")
    print(df.describe())

    # Plotting Traffic Volume over time for a few sensors
    plt.figure(figsize=(12, 6))
    for sensor_id in df["Sensor_ID"].unique()[:3]: # Plot first 3 sensors
        sensor_data = df[df["Sensor_ID"] == sensor_id]
        plt.plot(sensor_data["Timestamp"], sensor_data["Traffic_Volume"], label=sensor_id)
    plt.title("Traffic Volume Over Time (Selected Sensors)")
    plt.xlabel("Time")
    plt.ylabel("Traffic Volume")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/traffic_monitoring_project/simulation/traffic_volume_over_time.png")
    plt.close()
    print("Traffic volume plot saved to traffic_volume_over_time.png")

    # Plotting Average Speed distribution
    plt.figure(figsize=(8, 6))
    plt.hist(df["Average_Speed_kmh"], bins=15, edgecolor="black")
    plt.title("Distribution of Average Speed")
    plt.xlabel("Average Speed (km/h)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/traffic_monitoring_project/simulation/average_speed_distribution.png")
    plt.close()
    print("Average speed distribution plot saved to average_speed_distribution.png")

    # Plotting Occupancy distribution
    plt.figure(figsize=(8, 6))
    plt.hist(df["Occupancy_percent"], bins=15, edgecolor="black")
    plt.title("Distribution of Occupancy")
    plt.xlabel("Occupancy (%)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/traffic_monitoring_project/simulation/occupancy_distribution.png")
    plt.close()
    print("Occupancy distribution plot saved to occupancy_distribution.png")

    # Daily average traffic volume
    df["Date"] = df["Timestamp"].dt.date
    daily_avg_volume = df.groupby("Date")["Traffic_Volume"].mean()
    plt.figure(figsize=(10, 5))
    daily_avg_volume.plot(kind=\


"bar")
    plt.title("Daily Average Traffic Volume")
    plt.xlabel("Date")
    plt.ylabel("Average Traffic Volume")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/traffic_monitoring_project/simulation/daily_average_traffic_volume.png")
    plt.close()
    print("Daily average traffic volume plot saved to daily_average_traffic_volume.png")

if __name__ == "__main__":
    analyze_traffic_data()


