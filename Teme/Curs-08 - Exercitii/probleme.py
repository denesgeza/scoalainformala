string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]


def text_replacer(patch):
    global string
    for i in patches:
        string[i[0]:i[1]] = i[2]
    return string

print(string[5:14])
text_replacer(patches)



print(x)