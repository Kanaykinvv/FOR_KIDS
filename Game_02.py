import random

check = 0

print("Привет, эта игра 'Больше-меньше'. Версия 0.1")
print("="*20)
print("""Я буду показывать два числа, а тебе нужно написать ответ.
Ты победишь, если верно ответишь на все вопросы и заработаешь 5 очков!
Готов? Тогда начали!""")
print("="*20)

while True:
    while True:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if a != b: break

    x = random.randint(1, 2)

    if x == 1:
        answer = input("Что больше " + str(a) + " или " + str(b) + "? : ")
        if ((a > b) and (a == int(answer))) or ((a < b) and (b == int(answer))):
            print("Верно! Вот тебе 1 очко!")
            check += 1
        else:
            print("Не правильно. Снимем с тебя 1 очко!")
            check -= 1
    else:
        answer = input("Что меньше " + str(a) + " или " + str(b) + "? : ")
        if ((a > b) and (b == int(answer))) or ((a < b) and (a == int(answer))):
            print("Верно! Вот тебе 1 очко!")
            check += 1
        else:
            print("Не правильно. Снимем с тебя 1 очко!")
            check -= 1
    print("Твой счет равен: " + str(check))
    print("-"*20)

    if check == 5:
        print("Ты набрал 5 очков и победил! Поздравляю!")
        break