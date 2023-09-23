import random
number = random.randint(1, 101)
print("Добро пожаловать в числовую угадайку")

def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

flag_1 = False

while flag_1 == False:
    n = input("Введите число от 1 до 100")
    if is_valid(n):
        n = int(n)
        if n > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            n = input()
        elif n < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Верно, Вы угадали! Поздравляем!')
            flag_1 = True
            break       
    else:
        print('Ввод некорректный. Введите число от 1 до 100')