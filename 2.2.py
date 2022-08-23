# 2.	1 Ściągnij, lub napisz dowolny tekst, ale postaraj się, żeby miał niemniej,
# niż 500 znaków. Postaraj się, aby tekst był choć odrobinę ciekawy

# l.	Funkcje przydatne w wykonaniu zadania: split(), set(), count(), zip(), dict(), replace(), len()

movie = 'Niezależnie od tego, jaki rodzaj lęku przed przyszłością pojawia się w większości science fiction - ograniczone zasoby, bezduszna technologia, rosnący w siłę "robotyczni" władcy - tym, co leży u podstaw, jest zazwyczaj nasza własna przestarzałość. Film Łabędzi śpiew śledzi losy Camerona Turnera (Mahershala Ali), śmiertelnie chorego mężczyzny, który postanawia się sklonować, by oszczędzić swojej ciężarnej żonie Poppy (Naomie Harris) i ich synowi Coreyowi (Dax Rey) traumy związanej z jego utratą. Historia stawia głównego bohatera przed egzystencjalnym i etycznym dylematem. Subtelne zabiegi reżysera pozwalają widzom płynnie wejść w tę rzeczywistość. Nie przytłaczają zmysłów, nie odwracają uwagi od głównego tematu filmu.'
clean_movie = movie.replace('.', '').replace(',', '').replace('(', '').replace(')', '')

# ------------------------------------------------------------------
# a.	Policz (automatycznie) ile jest znaków
length = len(clean_movie)
print(f'Description has {length} characters')

# ------------------------------------------------------------------
# b.	Używając odpowiednich funkcji podziel test na osobne wyrazy
splitted = clean_movie.split()
print(splitted)

# ------------------------------------------------------------------
# c.	Policz (automatycznie)  ile jest słów
counted = len(splitted)
print(f'Description has {counted} words')

# ------------------------------------------------------------------
# d.	Używając typu danych set sprawdź ile jest różnych wyrazów w tekście,
# oraz ile jest różnych znaków
word = set(splitted)  # all words
n_words = len(word)

signs = set(clean_movie)  # all characters
n_signs = len(signs)
print(f'Number of different words: {n_words}  Number of different signs: {n_signs}')

# ------------------------------------------------------------------
# e.	Policz ile razy dany wyraz występuje w tekście

words = {}
for w in word:
    words[w] = clean_movie.count(w)

print(f'Number of repeated words: {words}')

# ------------------------------------------------------------------
# f.	Zrób to samo z literami

characters = {}
for s in signs:
    characters[s] = movie.count(s)

print(characters)

# ------------------------------------------------------------------
# g.	Wypisz co trzecie słowo tekstu

index = list(range(0, len(splitted), 3))
# print(index)
for i in index:
    print(splitted[i])

# inne pomysły
# l = splitted
# for index, element in enumerate(l):
#     if index%3 == 0:
#         print(index, element)
#
#
# index = list(range(0, len(splitted), 3))
# print(index)
# nowa_lista = []
# for i in index:

# #     nowa_lista.append(splitted[i])
# # nowa_lista = [splitted[i] for i in index]

# ------------------------------------------------------------------
# h.	Wypisz co trzeci znak tekstu

index = list(range(0, len(clean_movie), 3))
# print(index)
for i in index:
    print(clean_movie[i])

# i.	Teraz stwórz słownik zawierający jako klucze słowa, a jako wartości liczbę wystąpień


# j.	Wypróbuj, jak działa polecenie slownik[‘słowo’]

print(words['widzom'])

# k.	Zastąp w oryginalnym tekście wszystkie litery o na ciąg znaków xyz,

oxyz = clean_movie.replace('o', 'xyz')
print(oxyz)

# oraz pięć pierwszych wystąpień litery a na ciąg znaków %$#
a = 0
listt = list(clean_movie)
print(listt)
for i in list(range(0, len(listt))):
    if a < 5 and listt[i] == 'a':
        listt[i] = '%$#'
        a += 1
print(listt)
