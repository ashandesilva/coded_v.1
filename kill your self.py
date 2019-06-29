def type_a(x):
    x = x.replace("a", "Z", 1000)
    x = x.replace("b", "Y", 1000)
    x = x.replace("c", "X", 1000)
    x = x.replace("d", "W", 1000)
    x = x.replace("e", "V", 1000)
    x = x.replace("f", "U", 1000)
    x = x.replace("g", "T", 1000)
    x = x.replace("h", "S", 1000)
    x = x.replace("i", "R", 1000)
    x = x.replace("j", "Q", 1000)
    x = x.replace("k", "P", 1000)
    x = x.replace("l", "O", 1000)
    x = x.replace("m", "N", 1000)
    print("a" + x)


def type_b(x):
    x = x.replace("a", "Y", 1000)
    x = x.replace("b", "X", 1000)
    x = x.replace("c", "W", 1000)
    x = x.replace("d", "V", 1000)
    x = x.replace("e", "U", 1000)
    x = x.replace("f", "T", 1000)
    x = x.replace("g", "S", 1000)
    x = x.replace("h", "R", 1000)
    x = x.replace("i", "Q", 1000)
    x = x.replace("j", "P", 1000)
    x = x.replace("k", "O", 1000)
    x = x.replace("l", "N", 1000)
    x = x.replace("m", "Z", 1000)
    print("b" + x)


def type_c(x):
    x = x.replace("a", "X", 1000)
    x = x.replace("b", "W", 1000)
    x = x.replace("c", "V", 1000)
    x = x.replace("d", "U", 1000)
    x = x.replace("e", "T", 1000)
    x = x.replace("f", "S", 1000)
    x = x.replace("g", "R", 1000)
    x = x.replace("h", "Q", 1000)
    x = x.replace("i", "P", 1000)
    x = x.replace("j", "O", 1000)
    x = x.replace("k", "N", 1000)
    x = x.replace("l", "Z", 1000)
    x = x.replace("m", "Y", 1000)
    print("c" + x)


msg = input("Enter Message: ")
typo = input("Enter type (a,b or c):")

if typo == "a":
    type_a(msg)
elif typo == "b":
    type_b(msg)
elif typo == "c":
    type_c(msg)




