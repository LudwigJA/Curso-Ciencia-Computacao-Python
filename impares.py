n = int(input("Digite o valor de n: "))
b =1 

while n >= 1:
    impar = 1 * b
    b += 1
    
    if impar % 2 > 0:
        print(impar)
        n -= 1

        