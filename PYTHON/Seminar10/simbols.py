import requests
import controller

url = "https://api.apilayer.com/fixer/symbols"

payload = {}
headers= {
  "apikey": "byC3EE2DWwWE5LhTQO3pCDweOYaZyfLV"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)