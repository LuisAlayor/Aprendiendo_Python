print("==========================")
print("*    Menu de opciones  *")
print("==========================\n")

print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")
print("5.division entera")
print("6.exponente")
print("7.modulo o resto \n")


numero = int(input("Introduce tu opcion deseada:"))
if numero == 1:
    print("\nElegiste suma.\n")

    numero = float(input("Introduce el primer numero: "))
    numero += float(input("Introduce el segundo numero: "))
    print("\nEl resultado de la operación es: ", numero)


elif numero == 2:
    print("\nElegiste resta.\n")

    numero = float(input("Introduce el primer numero: "))
    numero -= float(input("Introduce el segundo numero: "))
    print("El resultado de la operación es: ", numero)

    
elif numero == 3:
    print("\nElegiste mutiplicacion.\n")

    numero = float(input("Introduce el primer numero: "))
    numero *= float(input("Introduce el segundo numero: "))
    print("El resultado de la operación es: ", numero)

    
elif numero == 4:
    print("\nElegiste division.\n")
    
    numero = float(input("Introduce el primer numero: "))
    numero /= float(input("Introduce el segundo numero: "))
    print("El resultado de la operación es: ", numero)

    
elif numero == 5:
    print("\nElegiste devision entera.\n")

    numero = float(input("Introduce el primer numero: "))
    numero //= float(input("Introduce el segundo numero: "))
    print("El resultado de la operación es: ", numero)

    
elif numero == 6:
    print("\nElegiste exponente.\n")

    numero = float(input("Introduce el primer numero: "))
    numero **= float(input("Introduce el segundo numero: "))
    print("El resultado de la operación es: ", numero)

    
elif numero == 7:
    print("\nElegiste modulo o resto. \n")

    numero = float(input("Introduce el primer numero: "))
    numero %= float(input("Introduce el segundo numero: "))
    print("El resultado de la operación es: ", numero)

    
else:
    print("Opcion no valida")

print("\nFIN.")



















