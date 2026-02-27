n1 = int(input("Escribe un numero "))
n2 = int(input("Escribe otro numero "))
n3 = int(input("Escribe otro numero "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

print(f"El número mayor de los tres es: {mayor}")