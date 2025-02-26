import requests
import time

# Updated Render service URLs
urls = [
    "https://blaze-python-compiler-uun1.onrender.com",
    "https://blaze-java-compiler-d9qx.onrender.com",
    "https://blaze-swift-compiler-js2c.onrender.com",
    "https://blaze-golang-compiler-u45o.onrender.com",
    "https://blaze-csharp-compiler-4wfe.onrender.com",
    "https://blaze-ruby-compiler-mgwh.onrender.com",
    "https://blazecompiler-r-5g3t.onrender.com",
    "https://blazecompiler-rust-ohp8.onrender.com",
    "https://blazecompiler-typescript-px8u.onrender.com",
    "https://blazecompiler-javascript-g8to.onrender.com",
    "https://blazecompiler-c-8eeb.onrender.com",
    "https://blazecompiler-cpp-0z64.onrender.com",
    "https://blazecompiler-php-pmzi.onrender.com"
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
