valor = int(input("Digite um número: "))

result = valor

if valor > 0: 
    while valor > 1:
        result = result *( valor -1 )
        valor = valor - 1    
    print(result)
else: 
    print (1)

