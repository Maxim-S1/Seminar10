import requests
import json

def convert_val(mony1, mony2, sum):
    url = f"https://api.apilayer.com/fixer/convert?to={mony1}&from={mony2}&amount={sum}"

    payload = {}
    headers= {
      "apikey": "byC3EE2DWwWE5LhTQO3pCDweOYaZyfLV"
    }

    response = requests.request("GET", url, headers = headers, data = payload)

    status_code = response.status_code
    result = response.text
    val_sum = json.loads(result)
    res = round(val_sum['result'], 2)
    return res

    # print(val_sum['query'], sep=' ', end='\n')

    # print(f'В {amount} {y} {z} {x}')



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