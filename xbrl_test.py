import requests
import json

headers = {
    "User-Agent": "your_email@example.com"
}

url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json"

response = requests.get(url, headers=headers)

print(response.status_code)

data = response.json()

print(data.keys())