# TEMA 4.
# Scrieți un program care să valideze nr de telefon al unui utilizator scris de la tastatura.
def mobile_no_validator():
    phone_number = input("Introduceți un număr de telefon: ")
    # daca len(număr) != 10, numărul nu începe cu 0, numărul nu continuă cu 237
    if len(phone_number) == 10 and phone_number[0] == '0' and phone_number[1] in '237':
        # daca nu sunt toate numere
        for number in phone_number:
            if number not in '0123456789':
                print("Numărul introdus nu este un număr de telefon valid.")
        print(f"Numărul de telefon: {phone_number}, este un număr valid!")
    else:
        print("Numărul introdus nu este un număr de telefon valid.")


mobile_no_validator()
