from random import randint

number = randint(1,10)
print('Введите число')


while True:
    try:
        guess = int(input('Введите число: '))
        if guess != number:
            print(f'Ай ай не угадали. Вы ввели {guess} а загадано было {number}')
        else:
            print(f'Ураа! вы угадали.')
            break
    except ValueError:
        print('Нужно обязательно ввести число')

