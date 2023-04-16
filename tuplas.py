# una tupla tiene la musna sjbfaxjs que la lista pero con esya no podemos eliminar añadir elementos a ariables, 
# pro son buennas por el echo ed que se ejecutan mas rapido .

from cgi import print_arguments


tupla=(1, 2, 3, 4, 5)
print(tupla [:])


print("         CONERTIR UNA  TUPLA EN UMA LISTA . ")

Vtupla=(1, 2, 3, 4, 5)
LISTA=list(tupla)
print(LISTA)


print("         CONVERTIR LISTA EN TUPLA. ")

LISTA=[1, 2, 3,  4, 5, 6, 7]
TUPLA=tuple(LISTA)
print(TUPLA)

print("ER  SE UN ELEMENTO ESTA EN MI TUPLA. ")


tupla=(1,2,3,4,5)
print(1 in tupla)
print(12 in tupla)


print("         SABER CUANTAS ELEMENTAS ECES SE REPITE UN ELEMENTO DE NUESTRA TUPLA.  ")

tupla=(8,9,5,6,7,9)
print(tupla.count(12))
print(tupla.count(9))

 
print("            saber cuantos elementos hay dentro de la tupla completa.")
 
tupla=(1, 2, 4, 5)
print(len(tupla))
print(" que es trupla unitaria.")

tupla=("abdel",)
print(tupla)

print("         tupla sin parentesis pero mejor hazlo con parentesis. ")

tupla=1, 2, 3, 4
print(tupla)


print("         hacer el desempacitado de tuplas. ")


tupla=("abdel", 19, 1, 2004)
nombre, dia, mes, anio=tupla
print(nombre)
print(dia)
print(anio)
print(mes)