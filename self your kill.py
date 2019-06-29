def a(x):
    x = x.replace("Z", "a", 1000)
    x = x.replace("Y", "b", 1000)
    x = x.replace("X", "c", 1000)
    x = x.replace("W", "d", 1000)
    x = x.replace("V", "e", 1000)
    x = x.replace("U", "f", 1000)
    x = x.replace("T", "g", 1000)
    x = x.replace("S", "h", 1000)
    x = x.replace("R", "i", 1000)
    x = x.replace("Q", "j", 1000)
    x = x.replace("P", "k", 1000)
    x = x.replace("O", "l", 1000)
    x = x.replace("N", "m", 1000)
    print(x)


def b(x):
    x = x.replace("Z", "m", 1000)
    x = x.replace("Y", "a", 1000)
    x = x.replace("X", "b", 1000)
    x = x.replace("W", "c", 1000)
    x = x.replace("V", "d", 1000)
    x = x.replace("U", "e", 1000)
    x = x.replace("T", "f", 1000)
    x = x.replace("S", "g", 1000)
    x = x.replace("R", "h", 1000)
    x = x.replace("Q", "i", 1000)
    x = x.replace("P", "j", 1000)
    x = x.replace("O", "k", 1000)
    x = x.replace("N", "l", 1000)
    print(x)


def c(x):
    x = x.replace("Z", "l", 1000)
    x = x.replace("Y", "m", 1000)
    x = x.replace("X", "a", 1000)
    x = x.replace("W", "b", 1000)
    x = x.replace("V", "c", 1000)
    x = x.replace("U", "d", 1000)
    x = x.replace("T", "e", 1000)
    x = x.replace("S", "f", 1000)
    x = x.replace("R", "g", 1000)
    x = x.replace("Q", "h", 1000)
    x = x.replace("P", "i", 1000)
    x = x.replace("O", "j", 1000)
    x = x.replace("N", "k", 1000)
    print(x)


code = input("Enter coded msg: ")

if code[0] == "a":
    real = code[1:]
    a(real)
elif code[0] == "b":
    real = code[1:]
    b(real)
elif code[0] == "c":
    real = code[1:]
    c(real)

