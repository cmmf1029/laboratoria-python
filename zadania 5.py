#zadanie 1
def check_password(password):
    if len(password) < 4 or len(password) > 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False

    for ch in password:
        if ch >= 'a' and ch <= 'z':
            has_lower = True
            continue
        if ch >= 'A' and ch <= 'Z':
            has_upper = True
            continue
        if ch >= '0' and ch <= '9':
            has_digit = True
            continue
        break
    return has_lower and has_upper and has_digit

password = input("Podaj hasło: ")
result = check_password(password)
with open("wynik.txt", "w") as f:
    if result:
        f.write("Hasło jest poprawne.\n")
    else:
        f.write("Hasło jest niepoprawne.\n")

#zadanie 2
    import pickle
    def find_numbers(x, y):
        result = []

        for n in range(x, y + 1):
            if n % 7 == 0:
                if n % 5 != 0:
                    result.append(n)
        return result

    try:
        x = int(input("Podaj x: "))
        y = int(input("Podaj y: "))
        numbers = find_numbers(x, y)
        print(",".join(str(n) for n in numbers))
        with open("wynik.pkl", "wb") as f:
            pickle.dump(numbers, f)
        print("Wynik zapisano do pliku wynik.pkl")
    except ValueError:
        print("Błąd: podaj liczby całkowite.")
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", e)

#zadanie 3
def power_sequence(*numbers):
    if len(numbers) > 100:
        raise ValueError("Błąd: za dużo argumentów (maksymalnie 100).")
    result = []
    for n in numbers:
        value = n ** n
        result.append(value)
    return result

try:
    user_input = input("Podaj liczby oddzielone przecinkami: ")
    parts = user_input.split(",")
    nums = []
    for p in parts:
        nums.append(int(p))
    output = power_sequence(*nums)
    print("Wyniki:", output)
except ValueError:
    print("Błąd: podaj poprawne liczby całkowite.")
except Exception as e:
    print("Wystąpił nieoczekiwany błąd:", e)





