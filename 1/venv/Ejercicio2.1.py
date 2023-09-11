numero=input("Ingrese un número a ser validado como capicúa o no: ")

digito1 = numero[0]
digito2=numero[1]
digito3=numero[2]
digito4=numero[3]

if digito1==digito4 and digito3==digito2:
    print ("Su número es capicúa")
else:
    print ("Su número no es capicúa")