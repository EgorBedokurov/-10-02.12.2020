# первый вариант
some_world=str(input("введите слово - "))

def check_func(a):
    b=[str(letter) for letter in a]
    c=b[::-1]
    if b==c:
        print ('это "палидром"')
    else:
        print('это не "палидром"')
    return a

check_func(some_world)

# второй вариант
someword = input('чтото введи ')

def poligrame(word):
    if word == ''.join(reversed(word)):
        print(True)
    else:
        print(False)
    return word

poligrame(someword)