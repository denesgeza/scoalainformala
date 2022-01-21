# TEMA 2.
# Scrieți un program ce va număra câte caractere are un șir de caractere
# dat de utilizator. Această numărare să se realizeze cu ajutorul unui for
# fără a utiliza len(). La final afișați rezultatul
text = input("Introdu un text oarecare: ")
lungime_text = 0
for _ in text:
    if _ != " ":
        lungime_text += 1

print(lungime_text)
