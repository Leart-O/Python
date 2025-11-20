import requests

uri = "https://www.ebay.com/sch/i.html?_nkw=laptop"

response = requests.get(uri)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to take the content from {uri}")