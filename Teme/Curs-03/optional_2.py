# TEMA 2.
# Scrieti un program ce va numara cate caractere are un sir de caractere
# dat de utilizator. Aceasta numarare sa se realizeze cu ajutorul unui for
# fara a utiliza len(). La final afisati rezultatul
text = input("Introdu un text oarecare: ")
lungime_text = 0
for _ in text:
    if _ != " ":
        lungime_text += 1

print(lungime_text)
