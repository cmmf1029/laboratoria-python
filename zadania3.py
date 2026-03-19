# #zadanie 1
# letters = ['M', 'a', 'g', 'd', 'a']
# join_name = lambda lst: ''.join(lst)
# result = join_name(letters)
# print(result)
# #zadanie 2
# full_name = "Magda Filewicz"
# split_words = lambda text: text.split()
# split_letters = lambda words: [list(word) for word in words]
# words = split_words(full_name)
# letters = split_letters(words)
# print(words)
# print(letters)
# #zadanie 3
# find_letter = lambda word, letter: letter in word
# print(find_letter("Python", "y"))
# print(find_letter("Magda","X"))
# #zadanie 4
# logins = []
# passwords = []
# while True:
#     login = input("Podaj login (lub STOP): ")
#     if login == "STOP":
#         break
#     if login == "":
#         continue
#
#     password = input("Podaj hasło: ")
#     if password == "":
#         continue
#
#     logins.append(login)
#     passwords.append(password)
# users = {}
# for i, login in enumerate(logins):
#     users[login] = passwords[i]
# print(users)
# # zadanie 5
# def Poziom(n):
#     print("*" * n)
#
# def Pion(n):
#     for _ in range(n):
#         print("*")
#
# print("Litera E:")
# Poziom(5)
# Pion(3)
# Poziom(4)
# Pion(3)
# Poziom(5)
#
# print("\nLitera L:")
# Pion(6)
# Poziom(5)
# #zadanie 6
# silnia = lambda n: 1 if n == 0 else n * silnia(n - 1)
# n = int(input("Podaj n: "))
# k = int(input("Podaj k: "))
# symbol_newtona = silnia(n) // (silnia(k) * silnia(n - k))
# print(f"Symbol Newtona C({n},{k}) = {symbol_newtona}")
# #zadanie 7
# numbers = list(range(1, 101))
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(", ".join(map(str, even_numbers)))
# #zadanie 8
# from functools import reduce
# result = reduce(lambda x, y: x * y, range(1, 100))
# print("Wynik mnożenia liczb z zakresu 1–99 to:")
# print(result)
# # zadanie 9
# numbers = range(2000, 3201)
# result = list(filter(lambda x: x % 7 == 0 and x % 5 != 0, numbers))
# print(", ".join(map(str, result)))
# #zadanie 10
# numbers = range(2000, 3201)
# result = list(filter(lambda x: x % 7 == 0 and x % 5 != 0, numbers))
# print(", ".join(map(str, result)))
# # zadanie 11
# Poziom = lambda n: print("*" * n)
# Pion = lambda n: list(map(lambda _: print("*"), range(n)))
# lit = input("Podaj literę (E lub L): ").upper()
# if lit == "E":
#     Poziom(5)
#     Pion(3)
#     Poziom(4)
#     Pion(3)
#     Poziom(5)
#
# elif lit == "L":
#     Pion(6)
#     Poziom(5)
#
# else:
#     print("Nieznana litera.")
#
