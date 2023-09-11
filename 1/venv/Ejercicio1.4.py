numero=input("Ingrese un número de 4 dígitos: ")

par1=numero[2]
par2=numero[0]

impar1=numero[3]
impar2=numero[1]

sumaPares=int(par1)+int(par2)
sumaImpares=int(impar1)+int(impar2)

if sumaPares>=10 or sumaImpares>=10:
    sumaPares=str(sumaPares)
    sumaImpares=str(sumaImpares)
    sumaPares=sumaPares[-1]
    sumaImpares=sumaImpares[-1]

numeroFinal=str(sumaImpares)+str(sumaPares)


print(numeroFinal)