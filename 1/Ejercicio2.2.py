print("Ingrese tres números que serán ordenados por el sistema: ")

numero1=input("Número 1: ")
numero2=input("Número 2: ")
numero3=input("Número 3: ")

maximo=max(numero1,numero2,numero3)

print("el numero mayor es "+maximo)

if maximo==numero1 and numero2>=numero3:
    print(numero3,numero2,numero1)
elif maximo==numero1 and numero3>=numero2:
    print(numero2,numero3,numero1)
elif maximo==numero2 and numero1>=numero3:
    print(numero3,numero1,numero2)
elif maximo == numero2 and numero3 >= numero1:
    print(numero1, numero3, numero2)
elif maximo == numero3 and numero1 >= numero2:
    print(numero2, numero1, numero3)
else:
    print(numero1, numero2, numero3)