# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

n = int(input ('Введите номер месяца: '))

if n == 1:
    print ('Вы ввели январь. 31 дней')
elif n == 2:
    print ('Вы ввели февраль. 28 дней')
elif n == 3:
    print ('Вы ввели март. 31 дней')
elif n == 4:
    print ('Вы ввели апрель. 30 дней')
elif n == 5:
    print ('Вы ввели май. 31 дней')
elif n == 6:
    print ('Вы ввели июнь. 30 дней')
elif n == 7:
    print ('Вы ввели июль. 31 дней')
elif n == 8:
    print ('Вы ввели август. 31 дней')
elif n == 9:
    print ('Вы ввели сентябрь. 30 дней')
elif n == 10:
    print ('Вы ввели октябрь. 31 дней')
elif n == 11:
    print ('Вы ввели ноябрь. 30 дней')
elif n == 12:
    print ('Вы ввели декабрь. 31 дней')
else:
    print ('Такого месяца нет!')

