from random import randint as ri

number = ri(1,101)
print('Угадайте число от 1 то 100')

while True:
    guess = int(input('Введитие число: '))
    if guess < number:
        print('Ваше число меньше того, что загадано.')
    elif guess > number:
        print('Ваше число больше того, что загадано.')
    if guess == number:
        break
print('Отличная интуиция! Вы угадали число :)')