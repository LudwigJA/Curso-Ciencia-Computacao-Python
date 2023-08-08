n = int(input("Digite um número inteiro: "))
soma = 0

while n > 0:
    s = n % 10
    n = n // 10    
    soma += s    
print (soma)
    

