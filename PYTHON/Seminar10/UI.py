def print_data(data, text=''):
  return print(f"{text} {data}")


# Функция для ввода данных
def input_data(data):
  return input(f"{data}")

# def input_mony():
#     y = input('Введите валюту, из которой хотите конвертировать (пример ввода: EUR, USD, GBP): ').strip()
#     x = input('Введите валюту, в которую хотите конвертировать (пример ввода: EUR, USD, GBP: ').strip()
#     amount = float(input('Введите сумму: '))
#     return f'Валюта 1: {y} Валюта 2: {x} Сумма: {amount}'

# import requests
# import json
#
#
# print('Программа предназначена для конверттации валют\n Список доступных валют:')
#
# url = "https://api.apilayer.com/fixer/symbols"
#
# payload = {}
# headers= {
#   "apikey": "byC3EE2DWwWE5LhTQO3pCDweOYaZyfLV"
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
# print(result)
#
# y = input('Введите валюту, из которой хотите конвертировать (пример ввода: EUR, USD, GBP): ').strip()
# x = input('Введите валюту, в которую хотите конвертировать (пример ввода: EUR, USD, GBP: ').strip()
# amount = float(input('Введите сумму: '))
#
#
# url = f"https://api.apilayer.com/fixer/convert?to={x}&from={y}&amount={amount}"
#
# payload = {}
# headers= {
#   "apikey": "byC3EE2DWwWE5LhTQO3pCDweOYaZyfLV"
# }
#
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
# val_sum = json.loads(result)
# z = round(val_sum['result'], 2)

# print(val_sum['query'], sep=' ', end='\n')

# print(f'В {amount} {y} {z} {x}')
# print(val_sum['result'])
def input_check(text):
  flag = False
  while flag == False:
    user_answer = input(text)
    try:
      int(user_answer)
      if 0 < int(user_answer) < 4:
        return int(user_answer)
      else:
        flag == False
    except ValueError:
      flag == False
