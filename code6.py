n = float(input("Escribe un numero "))


if n == 0:
    v = 0

elif n > 0:
    v = "positivo"

elif n < 0:
    v = "negativo"

print("El número es: ",  v)