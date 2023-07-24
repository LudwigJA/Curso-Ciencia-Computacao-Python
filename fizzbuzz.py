num = input(" Digite um numero: ")

fizz = int(num) % 3
buzz = int(num) % 5

fizzbuzz = fizz + buzz

if fizzbuzz == 0:
    print ("FizzBuzz")
else:
    print(num)