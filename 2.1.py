
# 1.Napisz program, który wczyta od użytkownika ciąg znaków.
# Sprawdź czy ciąg ten jest palindromem. Np. kot – nie, kajak – tak.


word = input('Insert freely word and check, if it is a palindrom ')
length = len(word) - 1  # 5
r_word = word[::-1]
i = str('')
j = 0


# longer with loops
for i in word:
    if i != word[length]:
        print('This word is not a palindrom!')
        print(f'{i} and {word[length]}')
        exit()
    elif j == length and i == word[length]:
        print('This word is a palindrom!')
        print(f'{j} vs {length}; {i} and {word[length]}')
        exit()
    else:
        print(f'{j} vs {length}; {i} and {word[length]}')
        length -= 1
        j += 1

# faster way
if word == r_word:
    print('This word is a palindrom!')
else:
    print('This word is not a palindrom!')