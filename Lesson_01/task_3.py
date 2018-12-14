def find_word_in_circle(circle, word):
    unrolled_circle = ''
    for i in range(len(circle) - 1 + len(word)):
        unrolled_circle += circle[i % len(circle)]
    # print()
    # print('unrolled_circle =', unrolled_circle)
    # print('unrolled_anticircle =', unrolled_circle[::-1])
    # print()
    if word in unrolled_circle or word in unrolled_circle[::-1]:
        return 'YES'
    else:
        return 'NO'


# print()
# circle, word = 'corpse', 'ecorps'
# print(circle, word)
# print(find_word_in_circle(circle, word))
# print()
# circle, word = 'corpse', 'cespro'
# print(circle, word)
# print(find_word_in_circle(circle, word))
# print()
# circle, word = 'corpse', 'ecorpseco'
# print(circle, word)
# print(find_word_in_circle(circle, word))
# print()
# circle, word = 'corpse', 'por'
# print(circle, word)
# print(find_word_in_circle(circle, word))
# print()
# circle, word = 't', 't'
# print(circle, word)
# print(find_word_in_circle(circle, word))
# print()
# circle, word = 't', 'm'
# print(circle, word)
# print(find_word_in_circle(circle, word))

# Конечно, я бы хотел написать программу в следующем виде:

# def find_word_in_circle(circle, word):
    # unrolled_circle = str([circle[i % len(circle)] for i in range(len(circle) - 1 + len(word))])
    # if word in unrolled_circle or word in unrolled_circle[::-1]:
        # return 'YES'
    # else:
        # return 'NO'
        
# Но проклятые строчки рекомендованной длины слишком коротки, чтобы выразить красоту моего кода(((
