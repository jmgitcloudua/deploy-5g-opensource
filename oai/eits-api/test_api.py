# upf_test.py - Test the traffic steering API
import requests

# UPF container IP address
container_ip = "192.168.72.134"

# UPF API endpoint to test
steer_endpoint = f"http://{container_ip}:8085/steer/v1"
health_endpoint = f"http://{container_ip}:8085/healthv/1"

def check_health(endpoint):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return True
    except requests.exceptions.RequestException:
        return False

def test_traffic_steering():
    if not check_health(health_endpoint):
        print("UPF API is not healthy. Exiting test.")
        return

    try:
        response = requests.get(steer_endpoint)
        response.raise_for_status()
        print("Steering:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to UPF: {e}")

if __name__ == "__main__":
    test_traffic_steering()
