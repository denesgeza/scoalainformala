# TEMA 4.
# Scrieti un program care sa valideze nr de telefon al unui utilizator scris de la tastatura.
def mobile_no_validator():
    phone_number = input("Introduceti un numar de telefon: ")
    # daca len(numar) != 10, numarul nu incepe cu 0, numarul nu continua cu 237
    if len(phone_number) == 10 and phone_number[0] == '0' and phone_number[1] in '237':
        # daca nu sunt toate numere
        for number in phone_number:
            if number not in '0123456789':
                print("Numarul introdus nu este un numar de telefon valid.")
        print(f"Numarul de telefon: {phone_number}, este un numar valid!")
    else:
        print("Numarul introdus nu este un numar de telefon valid.")


mobile_no_validator()
