def repeat_or_no(): # функция проверки продолжения работы
    # user_choice = 'N'
    # while user_choice != 'Y' or user_choice != 'N':
    user_choice = input('Вы хотите продолжить работу? (Y или N): ')
    if user_choice == 'N':
        return False
    elif user_choice == 'Y':
        return True
    else:
        print('Неверный ответ! Вы хотите продолжить работу? Вставить Y или N: ')
