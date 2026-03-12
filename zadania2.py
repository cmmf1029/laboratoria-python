# #a
# print("zadanie 1 a")
# set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                  'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                  'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                  'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
#                  'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
#                  'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
#                  'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])
#
# print(set_gene1 & set_gene2 & set_gene3)
#
# #b
# print("zadanie 1 b")
# common_12 = set_gene1 & set_gene2
# common_13 = set_gene1 & set_gene3
# common_23 = set_gene2 & set_gene3
#
# print("Wspólne 1 i 2:", common_12)
# print("Wspólne 1 i 3:", common_13)
# print("Wspólne 2 i 3:", common_23)
#
# #c
# print("zadanie 1 c")
# print("Geny występujące w pierwszej chorobie: ", set_gene1)
# print("Geny występujące w drugiej chorobie: ", set_gene2)
# print("Geny występujące w trzeciej chorobie: ", set_gene3)
#
# #zadanie2
# print("zadanie 2 ")
# lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                 'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
# geny = ['FGFR4', 'FGERA4']
#
# for gen in geny:
#     if gen in lista_gene1:
#         print(f"Gen {gen} znajduje się na indeksie: {lista_gene1.index(gen)}")
#     else:
#         print(f"Gen {gen} nie występuje w liście.")
#
# #zadanie 3 a
# print("zadanie 3 a")
# tekst = "Emma rzeczywiście była szybka – \ndane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. \nFakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu \n(choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby \nniezwykle korzystne dla brytyjskiej gospodarki)."
# print(tekst)
#
# ile = tekst.count("Emma")
# print(ile)
# #zadanie 3 b
# print("zadanie 3 b")
# duze = tekst.upper()
# print(duze)
# #zadanie 3 c, niedokończone
# print("zadanie 3 c")
# lista_wyrazow = tekst.split()
# print(lista_wyrazow)
# #zadanie 3 d
# print("zadanie 3 d")
# sentences = [s for s in tekst.replace("!", ".").replace("?", ".").split(".") if s.strip()]
# print(len(sentences))
#zadanie 4
# print("zadanie 4")
# k = int(input("podaj liczbe:  "))
# if k%2 == 0:
#     print("Liczba jest parzysta")
# else:
#     print("Liczba jest nieparzysta")
# #zadanie 5
# print("zadanie 5")
# punkty_studenci = [5, 8, 10, 12, 14, 15]
# MAX = 15
#
# for pkt in punkty_studenci:
#     procent = int(pkt / MAX * 100)
#
#     match procent:
#         case p if 50 <= p <= 60:
#             ocena = 3.0
#         case p if 61 <= p <= 70:
#             ocena = 3.5
#         case p if 71 <= p <= 80:
#             ocena = 4.0
#         case p if 81 <= p <= 90:
#             ocena = 4.5
#         case p if 91 <= p <= 100:
#             ocena = 5.0
#         case _:
#             ocena = "brak zaliczenia"
#
#     print(f"Punkty: {pkt:2d}  →  {procent:3d}%  →  ocena: {ocena}")
# zadanie 6
# print("zadanie 6")
# m = int(input("Podaj wartość m: "))
# suma = 0.0
# for i in range(1, m + 1):
#     suma += 1 / i
# print("Suma ciągu 1 + 1/2 + ... + 1/m wynosi:", suma)

#zadanie 7
# i = 1
#
# while i <= 10:
#     print(f"Pierwiastek z {i} = {i ** 0.5}")
#     i += 1
#
# #zadanie8
# import math
#
# a = float(input("Podaj a: "))
# b = float(input("Podaj b: "))
# c = float(input("Podaj c: "))
#
# if a == 0:
#     # Równanie liniowe bx + c = 0
#     if b != 0:
#         x = -c / b
#         print("To jest równanie liniowe. Rozwiązanie:", x)
#     else:
#         print("Brak rozwiązania (a = 0 i b = 0).")
# else:
#     # Równanie kwadratowe
#     delta = b**2 - 4*a*c
#
#     if delta > 0:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         print("Dwa pierwiastki rzeczywiste:")
#         print("x1 =", x1)
#         print("x2 =", x2)
#     elif delta == 0:
#         x = -b / (2*a)
#         print("Jeden pierwiastek podwójny:")
#         print("x =", x)
#     else:
#         print("Brak pierwiastków rzeczywistych (delta < 0).")

#zadanie 9
# wyniki = []
#
# for liczba in range(1, 1001):
#     tekst = str(liczba)
#     if all(int(cyfra) % 2 == 0 for cyfra in tekst):
#         wyniki.append(tekst)
#
# print(",".join(wyniki))
#zadanie 10
# while True:
#     x = input("Podaj pierwszą liczbę całkowitą (x): ")
#     y = input("Podaj drugą liczbę całkowitą (y): ")
#
#     # Sprawdzenie, czy dane są liczbami całkowitymi
#     if not (x.lstrip("-").isdigit() and y.lstrip("-").isdigit()):
#         print("Błąd: podaj liczby całkowite!")
#         continue  # wracamy do początku pętli
#
#     x = int(x)
#     y = int(y)
#
#     # Warunek zakończenia programu
#     if x == 0 or y == 0:
#         print("Wprowadzono 0. Program zakończony.")
#         break
#
#     # Obliczenie iloczynu
#     wynik = x * y
#     print("Iloczyn:", wynik)
#zadanie 11
# Krotka z dwoma poprawnymi hasłami
# hasla = ("python123", "hasloABC")
#
# wpisane = input("Podaj hasło: ")
#
# if wpisane in hasla:
#     print("Dostęp przyznany.")
#     print("Twoje imię i nazwisko: Jan Kowalski")
# else:
#     print("Błędne hasło. Brak dostępu.")

#zadanie 12
# import random
# lista = [random.randint(1, 1000) for _ in range(100)]
# nieparzyste = [x for x in lista if x % 2 != 0]
# nieparzyste.sort()
# print("Liczby nieparzyste posortowane rosnąco:")
# print(nieparzyste)

#zadanie 13
# hasla = ("python123", "hasloABC")
#
# wpisane = input("Podaj hasło: ")
#
# print("Dostęp przyznany. Twoje imię i nazwisko: Jan Kowalski") if wpisane in hasla else print("Błędne hasło. Brak dostępu.")




