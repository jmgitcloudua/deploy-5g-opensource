import requests
import psutil
import time
import matplotlib.pyplot as plt

# Function to measure latency and bandwidth utilization
def measure_latency_and_bandwidth(url, duration=10):
    start_time = time.time()
    start_bytes = psutil.net_io_counters().bytes_recv

    # Download the video file and measure latency
    r = requests.get(url, stream=True)
    latencies = []
    timestamps = []
    bandwidths = []

    with open('downloaded_video.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                chunk_start_time = time.time()
                f.write(chunk)
                chunk_end_time = time.time()

                # Calculate latency for this chunk
                latency = chunk_end_time - chunk_start_time
                latencies.append(latency)

                # Calculate bandwidth utilization up to this point
                current_bytes = psutil.net_io_counters().bytes_recv
                duration_elapsed = chunk_end_time - start_time
                bytes_received = current_bytes - start_bytes
                bandwidth = (bytes_received / duration_elapsed) / 1024 / 1024  # in MB/s

                timestamps.append(duration_elapsed)
                bandwidths.append(bandwidth)

                # Stop after the specified duration
                if duration_elapsed >= duration:
                    break

    return timestamps, latencies, bandwidths

if __name__ == '__main__':
    video_url = 'http://127.0.0.1:5000/video//v1'  # Change the URL if your server is running on a different address
    #duration = 90  # Duration of the measurement in seconds
    timestamps, latencies, bandwidths = measure_latency_and_bandwidth(video_url)

    # Plotting latency over time
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, latencies, label='Latency')
    plt.xlabel('Time (s) since start of download')
    plt.ylabel('Latency (s)')
    plt.title('Latency Over Time')
    plt.legend()
    plt.grid(True)

    # Plotting bandwidth utilization over time
    plt.subplot(2, 1, 2)
    plt.plot(timestamps, bandwidths, label='Bandwidth', color='orange')
    plt.xlabel('Time (s) since start of download')
    plt.ylabel('Bandwidth (MB/s)')
    plt.title('Bandwidth Utilization Over Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

