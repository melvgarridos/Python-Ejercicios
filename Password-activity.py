password = str(input("Crea tu contraseña: "))

password1 = str(input("Escribe tu contraseña: "))

a1 = list(password)
a2 =list(password1)

if len(a1) == len(a2):
    print("Las contraseñas coinciden")

else:
    contador = 0
    ciclo = []

    for i in a2:
        if i in a1 and i not in ciclo:
            contador += 1
            ciclo.append(i)

    print("Las contraseñas coinciden en: ", contador)
            
    



