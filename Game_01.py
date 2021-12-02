import random

print("Игра Угадайка. Версия 0.2")
print("="*20)

a = 1
b = int(input("До какого числа мне загадать число? "))

# Количество попыток
attempt = random.randint(1, b // 2)

# Загаданное число
x = random.randint(a, b)

print("Я загадал число от " + str(a) + " до " + str(b) + ". Попробуй отгадать!")
print("У тебя есть " + str(attempt) + " попыток!")

while True:
    y = input("Введи число: ")
    if int(y) == x:
        print("Молодец! Я загадал именно " + str(x))
        print("Ты заработал " + str(attempt * 10) + " очков!")
        break
    else:
        print("Нет! Не верно, попробуй еще раз!")
        attempt -= 1
        if attempt == 0:
            print("Игра закончена, у тебя не осталось ни одной попытки!")
            print("Я загадал число " + str(x))
            break
        else:
            print("Осталось попыток: " + str(attempt))

        if int(y) > x:
            print("Подсказка: моё число меньше")
        else:
            print("Подсказка: моё число больше")