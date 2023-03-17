number = 100
attempts = 1
while True:
    try:
        answer = int(input('введите число: '))

        if answer == number:
            print('вы угадали!')
            print(f'Кол-во попыток: {attempts}')
            break
        elif answer < number:
            print('ваше число меньше загаданного')
            attempts += 1
        else:
            print('Ваше число больше загаданного')
            attempts += 1


    except ValueError:
        print(f'[ERROR] Данные должны иметь числовой тип')

    except Exception as ex:
        print(repr(ex))