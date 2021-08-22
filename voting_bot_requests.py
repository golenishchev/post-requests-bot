import requests

data = {
    "action": "postratings",
    "pid": "1337",
    "rate": "1",
    "postratings_1337_nonce": "b7e58dcи16"
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

# To use socks proxies do this
# pip install -U requests[socks]
proxyDict = {
    "https": "socks4://130.193.39.79:5678"
}

while True:
    try:
        with requests.Session() as s:
            url = "https://domain.com/some-link.php" # DevTools --> Netvork --> Headers --> General --> Request URL: https://domain.com/some-link.php
            r = s.post(url, data=data, headers=headers, proxies=proxyDict)
            print(r.text)
    except:
        print("Proxy Connection Error")