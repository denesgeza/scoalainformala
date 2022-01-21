# TEMA 3.
# Creati un program in care utilizatorul sa introduca o adresa de email
# de formatul litere_sau_cifre@litere_sau_cifre.litere.
# Validati acest sir de caractere si informati utilizatorul de raspuns.
# @ sau .(punct) trebuie sa exista o singura data in sirul de caractere


def email_validator():
    email = input("Introduceti o adresa de email valida: ")

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
