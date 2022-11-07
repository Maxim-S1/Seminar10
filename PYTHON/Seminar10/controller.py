import UI
import converter
import logger
import simbols


def button_click():
    UI.print_data("\nВы можете выполнить следующие действия по списку: ")
    answer = UI.input_check("1. Конвертировать валюту.\n2. Вывести список валют.\n3. Для завершения работы.\nВведите номер действия: ")
    if answer == 1:
        y = str(UI.input_data('Введите валюту, из которой хотите конвертировать (пример ввода: EUR, USD, GBP): ')).strip()
        x = str(UI.input_data('Введите валюту, в которую хотите конвертировать (пример ввода: EUR, USD, GBP: ')).strip()
        amount = float(UI.input_data('Введите сумму: '))
        res = converter.convert_val(x, y, amount)
        UI.print_data(f'В {amount} {y} {res} {x}')
        logger.result_loger(f'При конвертации {amount} {y} получено {res} {x}')
        button_click()
    elif answer == 2:
        result = simbols.simbols_val()
        UI.print_data(f'{result}\nВы можете выбрать любую из предложенных валют для конвертации.')
        button_click()
    elif answer == 3:
        exit()
    else:
        print("Неверный ввод")
        button_click()