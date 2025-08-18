import requests
import time

# Updated Render service URLs
urls = [
    "https://blazecompiler-python-cf80.onrender.com",
    "https://blazecompiler-cpp-6kk2.onrender.com",
]

while True:
    for url in urls:
        try:
            # Send a GET request
            response = requests.get(url)
            print(f"Pinged {url} - Status Code: {response.status_code}")
        except Exception as e:
            print(f"Failed to ping {url}: {e}")
    
    time.sleep(60)
