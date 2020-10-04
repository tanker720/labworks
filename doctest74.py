import random
def testmod():
    print(str('Введите число от 10 до 15'))
    c = int(input("Ваше число: "))
    d = random.randint(10, 15)
    if c == d:
        print('Победа, ', d)
    else:
        print('Повторите ещё раз')


