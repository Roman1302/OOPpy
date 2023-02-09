import sys

import os
clear = lambda: os.system('clear')
clear()

print('Калькулятор рациональных и комплексных чисел')

def type():
    type = input('С какими цифрами вы собираетесь работать? \n \
        поставьте 1 = Комплексные, 2 = Рациональный: ').lower()
    return type

