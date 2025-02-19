import requests
import time

# Updated Render service URLs
urls = [
    "https://blazecompiler-cpp.onrender.com",
    "https://blazecompiler-c.onrender.com",
    "https://blazecompiler-csharp.onrender.com",
    "https://blazecompiler-java.onrender.com",
    "https://blazecompiler-javascript.onrender.com",
    "https://blazecompiler-typescript.onrender.com",
    "https://blazecompiler-r.onrender.com",
    "https://blazecompiler-rust.onrender.com",
    "https://blazecompiler-ruby.onrender.com",
    "https://blazecompiler-python.onrender.com",
    "https://blazecompiler-php.onrender.com",
    "https://blazecompiler-golang.onrender.com"
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
