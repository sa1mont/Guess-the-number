import random
number = random.randint(1, 101)
print("Добро пожаловать в числовую угадайку. Мной было загадано число, попробуй ка отгадать.")

def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

flag_1 = False
total = 0
while flag_1 == False:
    n = input("Введите число от 1 до 100")
    if is_valid(n):
        n = int(n)
        total += 1
        if n > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            n = input()
        elif n < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n == number:
            print(f'Верно, Вы угадали с {total} попытки! Поздравляем!')
            flag_1 = True
            if flag_1 == True:
                a = input('Хотите сыграть ещё? Если да, то введите "да", если нет, то введите что угодно')
                if a.lower() == 'да':
                    flag_1 = False
                    total = 0
                else:
                    break
    else:
        print('Ввод некорректный. Введите число от 1 до 100')