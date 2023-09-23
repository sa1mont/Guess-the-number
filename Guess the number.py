import random
number = random.randint(1, 101)
print("Добро пожаловать в числовую угадайку")

def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

flag = False

while flag == False:
    n = input("Введите число от 1 до 100")
    if is_valid(n):
        n = int(n)
        flag = True
        break
    else:
        print('Ввод некорректный. Введите число от 1 до 100')

