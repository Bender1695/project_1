# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


def remove_exclamation_marks(s):
    s = s.replace("!", "")
    return s

print('Пункт А')
print(remove_exclamation_marks('Hi! Hello!'))
print(remove_exclamation_marks(''))
print(remove_exclamation_marks('Oh, no!!!'))




# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

print('Пункт B')
def remove_last_em(s):
    if s[-1] == '!':
        s = s[:-1]
    return s

print(remove_last_em("Hi!"))
print(remove_last_em("Hi!!!"))
print(remove_last_em("!Hi"))



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


def remove_word_with_one_em(s):
    new_s = []
    words = s.split(' ') # делим строку на слова
    for i in words:
        if i.count('!') != 1:
            new_s.append(i)
            new_s
            ' '.join(new_s) # собираем строку используя в качестве разделителя пробел
    return new_s
 
print('Пункт C')
print(remove_word_with_one_em("Hi!"))
print(remove_word_with_one_em("Hi! Hi!"))
print(remove_word_with_one_em("Hi! Hi! Hi!"))
print(remove_word_with_one_em("Hi Hi! Hi!"))
print(remove_word_with_one_em("Hi! !Hi Hi!"))
print(remove_word_with_one_em("Hi! Hi!! Hi!"))
print(remove_word_with_one_em("Hi! !Hi! Hi!"))
