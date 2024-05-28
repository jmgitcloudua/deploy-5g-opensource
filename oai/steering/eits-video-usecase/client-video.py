import requests
import psutil
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Function to measure bandwidth utilization
def measure_bandwidth(url, duration=10):
    start_time = time.time()
    start_bytes = psutil.net_io_counters().bytes_recv

    # Download the video file
    r = requests.get(url, stream=True)
    with open('downloaded_video.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    end_bytes = psutil.net_io_counters().bytes_recv
    end_time = time.time()

    # Calculate bandwidth utilization over time
    timestamps = []
    bandwidths = []
    while time.time() - start_time < duration:
        current_time = time.time()
        current_bytes = psutil.net_io_counters().bytes_recv
        duration_elapsed = current_time - start_time
        bytes_received = current_bytes - start_bytes
        bandwidth = (bytes_received / duration_elapsed) / 1024 / 1024  # in MB/s
        timestamps.append(duration_elapsed)
        bandwidths.append(bandwidth)
        time.sleep(1)  # Wait for 1 second before measuring again

    return timestamps, bandwidths

def confidence_interval(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    z_score = stats.t.ppf(0.975, len(data)-1)  # For 95% confidence interval
    margin_of_error = z_score * (std_dev / np.sqrt(len(data)))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound

if __name__ == '__main__':
    video_url = 'http://127.0.0.1:5000/video/v1'  # Change the URL if your server is running on a different address
    #duration = 90  # Duration of the bandwidth measurement in seconds
    timestamps, bandwidths = measure_bandwidth(video_url)

    # Calculate confidence interval for bandwidth data
    lower_bound, upper_bound = confidence_interval(bandwidths)

    # Plotting the bandwidth utilization over time using line graph with confidence interval
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, bandwidths, label='Bandwidth')
    plt.fill_between(timestamps, lower_bound, upper_bound, color='skyblue', alpha=0.4, label='95% Confidence Interval')
    plt.xlabel('Time (s) since start of download')
    plt.ylabel('Bandwidth (MB/s)')
    plt.title('Bandwidth Utilization Over Time with 95% Confidence Interval')
    plt.legend()
    plt.grid(True)
    plt.show()
