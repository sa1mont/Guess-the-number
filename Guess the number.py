import random
print("Добро пожаловать в числовую угадайку.")

def is_valid(num, numb):
    if num.isdigit() and 1 <= int(num) <= numb:
        return True
    else:
        return False

def is_valid_max(numb):
    if numb.isdigit() and int(numb) > 1:
        return True
    else:
        return False

flag_1 = False
while flag_1 == False:
    m = input("Введите правую границу для загадываемого числа(максимальное число)")
    if is_valid_max(m):
        m = int(m)
        flag_2 = True
        break
    else:
        print('Ввод некорректный. Введите правую границу для загадываемого числа(максимальное число)')

number = random.randint(1, m)

flag_2 = False
total = 0

while flag_2 == False:
    n = input(f"Введите число от 1 до {m}")
    if is_valid(n, m):
        n = int(n)
        total += 1
        if n > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            n = input()
        elif n < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n == number:
            print(f'Верно, Вы угадали с {total} попытки! Поздравляем!')
            flag_2 = True
            if flag_2 == True:
                a = input('Хотите сыграть ещё? Если да, то введите "да", если нет, то введите что угодно')
                if a.lower() == 'да':
                    flag_2 = False
                    total = 0
                else:
                    break
    else:
        print('Ввод некорректный. Введите число от 1 до 100')