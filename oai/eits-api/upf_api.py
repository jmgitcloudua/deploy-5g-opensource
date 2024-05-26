# upf_api.py - API to steer traffic to the site with the best combined score of network and computing metrics
from flask import Flask, jsonify
import requests
import statistics
import time
import yaml
import os

app = Flask(__name__)

# Get the absolute path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the metrics.yaml file
metrics_yaml_path = os.path.join(current_dir, 'metrics.yaml')

# Load metrics from the YAML file
with open(metrics_yaml_path) as file:
    metrics = yaml.safe_load(file)

# Addresses to steer traffic
site1_address = "192.168.73.134"
site2_address = "192.168.74.134"

# Define weights for network and computing metrics
network_weights = {
    "bandwidth_utilization": 0.4,
    "throughput": 0.3,
    "latency": 0.2,
    "packet_loss": 0.05,
    "jitter": 0.05
}

computing_weights = {
    "cpu_usage": 0.3,
    "memory_usage": 0.3,
    "disk_io": 0.2,
    "gpu_utilization": 0.2
}

@app.route('/steer/v1', methods=['GET'])
def steer_traffic():
    try:
        # Calculate combined score for each site
        site1_score = calculate_combined_score(metrics['site1'])
        site2_score = calculate_combined_score(metrics['site2'])

        # Choose the site with higher combined score
        if site1_score > site2_score:
            return jsonify({'message': f"Steering traffic to {site1_address}, score:{site1_score} - [site1]"})
        else:
            return jsonify({'message': f"Steering traffic to {site2_address}, score:{site2_score} - [site2]"})
    except Exception as e:
        return jsonify({'error': f"Failed to steer traffic: {e}"}), 500

@app.route('/health/v1', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

def calculate_combined_score(site_metrics):
    # Calculate combined score for a site based on weighted sum of metrics
    network_score = sum(site_metrics['network_metrics'][metric] * weight for metric, weight in network_weights.items())
    computing_score = sum(site_metrics['computing_metrics'][metric] * weight for metric, weight in computing_weights.items())
    return network_score + computing_score

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)
