#zadanie 1
import os
def change_directory(path):
    try:
        os.chdir(path)
        print("Zmieniono katalog na:", path)
        print("Zawartość katalogu:")
        for item in os.listdir():
            print(item)
    except FileNotFoundError:
        print("Błąd: taki katalog nie istnieje.")
    except NotADirectoryError:
        print("Błąd: podana ścieżka nie jest katalogiem.")
    except PermissionError:
        print("Błąd: brak uprawnień do otwarcia katalogu.")
    except Exception as e:
        print("Nieoczekiwany błąd:", e)
user_path = input("Podaj ścieżkę do katalogu: ")
change_directory(user_path)

#zadanie 2
import os

def change_directory(path):
    try:
        os.chdir(path)
        print("Zmieniono katalog na:", path)
        print("Zawartość katalogu:")
        for item in os.listdir():
            print(item)
    except Exception as e:
        print("Błąd:", e)
while True:
    answer = input("Czy mam zmienić katalog? (yes): ")
    if answer == "yes":
        break
    else:
        print("Musisz wpisać 'yes'.")
path = input("Podaj ścieżkę do katalogu: ")
change_directory(path)

#zadanie 3
import os
print("Wszystkie pliki w folderze roboczym:")
for item in os.listdir():
    print(item)
print("\nPliki .doc:")
for item in os.listdir():
    if item.endswith(".doc"):
        print(item)

#zadanie 4
import os
os.mkdir("StudentDoc")
os.mkdir("StudentObrazy")

with open("StudentDoc/plik1.txt", "w") as f:
    f.write("tekst")
with open("StudentDoc/plik2.txt", "w") as f:
    f.write("tekst2")

with open("StudentObrazy/obraz1.jpg", "wb") as f:
    f.write(b"123")
with open("StudentObrazy/obraz2.png", "wb") as f:
    f.write(b"456")

print("StudentDoc:")
for item in os.listdir("StudentDoc"):
    size = os.path.getsize("StudentDoc/" + item)
    print(item, "->", size, "bajtów")

print("\nStudentObrazy:")
for item in os.listdir("StudentObrazy"):
    size = os.path.getsize("StudentObrazy/" + item)
    print(item, "->", size, "bajtów")


#zadanie 5
import os
os.mkdir("StaryFolder")
os.rename("StaryFolder", "NowyFolder")

#zadanie 6
import pickle
import os
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista3 = [10.5, 20.5]
with open("listy.pkl", "wb") as f:
    pickle.dump((lista1, lista2, lista3), f)
del lista1
del lista2
del lista3
with open("listy.pkl", "rb") as f:
    l1, l2, l3 = pickle.load(f)

print(l1, l2, l3)

#zadanie 7
import struct

number = 123456789
with open("liczba.bin", "wb") as f:
    packed = struct.pack("I", number)
    f.write(packed)
with open("liczba.bin", "rb") as f:
    data = f.read()
    unpacked = struct.unpack("I", data)[0]
print("Odczytana liczba:", unpacked)
