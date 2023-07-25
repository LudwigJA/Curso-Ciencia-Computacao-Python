import math

x = int(input("digite a primeira coordenada: "))
y = int(input("digite a segunda coordenada: "))
x2 = int(input("digite a primeira coordenada: "))
y2 = int(input("digite a segunda coordenada: "))

distancia = math.sqrt(((x - x2)**2) + ((y - y2)**2))

if distancia >= 10:
    print("longe")
else:
    print("perto")

