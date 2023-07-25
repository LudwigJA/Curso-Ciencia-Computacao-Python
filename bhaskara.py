import math

a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))

delta = (b ** 2  -4 * a * c)


if delta == 0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz dupla desta equação é", x)

else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        x = (-b + math.sqrt(delta))/ (2 * a)
        x2 = (-b - math.sqrt(delta))/ (2 * a)
        if x < x2:
            print("as raízes da equação são", x, "e", x2)
        else:
            print("as raízes da equação são", x2, "e", x)


