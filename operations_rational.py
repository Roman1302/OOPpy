import operations_rational as op
import sys
from datetime import datetime as dt
import repeat_or_no as RON

def x():
    firstnum = float(input('Выберите первое число с плавающей точкой: ').replace(',', '.'))
    return firstnum

def selectoperation():
    global operation
    operation = (input(f'Выберите операцию: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Недопустимый символ')

def y():
    secondnum = float(input('Выберите второе число с плавающей точкой: ').replace(',', '.'))
    return secondnum

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('Недопустимый символ')

def mainterminal():
    x = op.x()
    # while True:
    oper = op.selectoperation()
    y = op.y()
    res = op.res(x, y)
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open('results.json', 'a') as data:
        data.write(f'{time} Результат {x} {oper} {y} = {res}\n')
    print(f'Результат {x} {oper} {y} = {res}\n' )

def repeat_or_no():

    if RON.repeat_or_no() == True:
        mainterminal()
    else:
        return False

        # again = input('Вы хотите рассчитать другие числа? Y/N: ')
        # if again == 'Y':
        #     useresult = input('Вы хотите использовать результат последней операции? (Y/N): ')
        #     if useresult == 'Y':
        #         x = res
        #         continue
        #     elif useresult == 'N':
        #         break
        #     else:
        #         return
        #         # sys.exit()           
        # else:   
        #     return
            # sys.exit()
