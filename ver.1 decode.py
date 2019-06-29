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


code = input("Enter coded msg: ")
a(code)
