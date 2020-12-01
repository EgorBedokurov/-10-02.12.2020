# как-то так, если я правильно понял задание
lines = ['первая строка', 'четвертая строка', 'третья строка', 'четвертая строка']
with open('home_work.txt', 'w', encoding='utf-8') as f:  #снова для кирилицы нужен "encoding='utf-8'"
    for line in lines:
        f.write(line + '\n')