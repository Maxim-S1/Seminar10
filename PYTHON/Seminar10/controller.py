import UI
import converter
import simbols


def button_click():
    UI.print_data("\nПрограмма предназначена для конверттации валют\nВы можете выполнить следующие действия со списком: ")
    answer = UI.input_check_choice("1. Конвертировать валюту.\n2. Вывод список валют.\n")
    if answer == 1:
        converter.result
        button_click()
    elif answer == 2:
        simbols.result
        button_click()