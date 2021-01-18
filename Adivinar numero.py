#jugador piensa un numero y haga preguntas para saber el numero elegido // "incluir codigo: try/except"

print ("Piensa un numero")

numero_uno = input("si pensaste el numero presiona Y en caso contrario N: ")
numero_uno = numero_uno.lower()

  
if numero_uno == "y":
    numero_pensado = input("agregale un 0 al numero pensado y presiona 'Y': ")
    
    if numero_pensado == "y":
        numero_pensado_restado = input("ahora restale un numero multiplo de 9: y presiona 'Y': ")

        if numero_pensado_restado == "y":
            print("introduce el numero en la siguiente linea: ")
            numero_preparado = int(input())
            nueva_fun = int(repr(numero_preparado)[0:-1])
            nueva_fun_2 = int(str(numero_preparado)[-1])
            print("El numero que pensaste es: ", nueva_fun + nueva_fun_2)

else:
    print ("Piensalo, es gratis ...")



