any_list = []

while True:
    a = input('enter some string: ')
    if a != '':
        any_list.append(a)
    if a == '':
        break

with open('home_work.txt', 'w', encoding='utf-8') as f:  # снова для кирилицы нужен "encoding='utf-8'"
    for line in any_list:
        f.write(line + '\n')


