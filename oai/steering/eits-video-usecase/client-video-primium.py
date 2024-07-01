import requests
from threading import Thread
import time

def download_video(url, output_path='downloaded_video.mp4'):
    def download():
        start_time = time.time()
        r = requests.get(url, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        downloaded_size = 0

        with open(output_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    
                    # Calculate and print progress
                    progress = (downloaded_size / total_size) * 100
                    print(f"\rDownload progress: {progress:.2f}%", end="", flush=True)

        end_time = time.time()
        duration = end_time - start_time
        print(f"\nVideo downloaded successfully in {duration:.2f} seconds.")

    download_thread = Thread(target=download)
    download_thread.start()
    download_thread.join()

if __name__ == '__main__':
    video_url = 'http://127.0.0.1:5000/video/v1'  # Replace with your actual URL
    download_video(video_url)
