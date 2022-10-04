def countLet(txt):    
    list = []
    for i in range(0, 26):
        list.append(0)
    maxim = 0
    lmax = ""
    txt = txt.upper()
    txt = txt.replace(" ", "_")
    for i in txt:
        if i != "_":
            list[ord(i) - 65] = list[ord(i) - 65] + 1
            if maxim < list[ord(i) - 65]:
                maxim =list[ord(i) - 65]
                lmax = i
    return lmax
print(countLet("an apple is not a tomato"))