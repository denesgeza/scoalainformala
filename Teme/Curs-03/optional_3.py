# TEMA 3.
# Creați un program in care utilizatorul sa introducă o adresa de email
# de formatul litere_sau_cifre@litere_sau_cifre.litere.
# Validați acest sir de caractere si informați utilizatorul de răspuns.
# @ sau .(punct) trebuie sa exista o singură data in șirul de caractere


def email_validator():
    email = input("Introduceți o adresa de email valida: ")

    tested_email = ""
    for char in email:
        if char.isalnum():
            tested_email += char
        elif char == "@":
            tested_email += char
        elif char == ".":
            tested_email += char
        else:
            tested_email += '@@'

    if tested_email.count('@') == 1 and tested_email.count('.') == 1 and tested_email.index('@') < tested_email.index('.'):
        print(f"Adresa de mail: {tested_email} este valida!")
    else:
        print("Nu este o adresa de email valida!")


email_validator()
