import requests
import json
import UI

y = input('Введите валюту, из которой хотите конвертировать (пример ввода: EUR, USD, GBP): ').strip()
x = input('Введите валюту, в которую хотите конвертировать (пример ввода: EUR, USD, GBP: ').strip()
amount = int(input('Введите сумму: '))

url = f"https://api.apilayer.com/fixer/convert?to={x}&from={y}&amount={amount}"

payload = {}
headers= {
  "apikey": "byC3EE2DWwWE5LhTQO3pCDweOYaZyfLV"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
val_sum = json.loads(result)

print(val_sum['query'], sep=' ', end='\n')
print(val_sum['result'])

# {
#   "date": "2018-02-22",
#   "historical": "",
#   "info": {
#     "rate": 148.972231,
#     "timestamp": 1519328414
#   },
#   "query": {
#     "amount": 25,
#     "from": "GBP",
#     "to": "JPY"
#   },
#   "result": 3724.305775,
#   "success": true
# }