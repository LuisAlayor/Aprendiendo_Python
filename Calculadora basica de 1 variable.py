print("====================")
print("Calculadora basica")
print("====================\n")

print("Seleciona 1 para suma")
print("Seleciona 2 para resta")
print("Seleciona 3 para multiplic.")
print("Seleciona 4 para division")
print("Seleciona 5 para exponente\n")

elección = int(input("introduce su elección"))

if elección == 1: 
    num = float(input("introduce el num deseado: "))
    num += float(input("introduce el num deseado: "))
    print(num)
elif elección == 2: 
    num = float(input("introduce el num deseado: "))
    num -= float(input("introduce el num deseado: "))
    print(num)
elif elección == 3: 
    num = float(input("introduce el num deseado: "))
    num *= float(input("introduce el num deseado: "))
    print(num)
elif elección == 4: 
    num = float(input("introduce el num deseado: "))
    num /= float(input("introduce el num deseado: "))
    print(num)
elif elección == 5: 
    num = float(input("introduce el num deseado: "))
    num **= float(input("introduce el num deseado: "))
    print(num)
else:
    print("\nsleccion no valida, intentare meter un while.")