# def, if, print, return, type, comentario, else
# vamos a peacticar lo visto.

# SUMA DE DOS NUMEROS SI SON DIFERENTES, SI SON IGUALES QUE NO LO SUME 
# DEJANDO UN MENSAJE QUE DEJE CLARO AL USAURIO QUE SON IGUALES.

num1=6
num2=5
if num1==num2:
    print("el numero uno es igual que el numero 2")
else:
    print(num1+num2)


# LLAMAR UNA VARIABLE CON EL NOMBRE SUMA Y DESPUES HACER UN RESTURN A LA SUMA Y RETA ALMACENADA
# SEGUN LO QYE CUMPLA EL USUARIIO.
# NO OLVIDAR LLAMAR A LA VARIABLE AL FINAL Y PONERLE POR DETRAS EL PRINT PORQUE SE NO, NO IMPRIME NADA POR PANTALLA.
def suma(num1, num2):
    if num1==num2:
        suma_almacemada=num1+num2
        return suma_almacemada
    else:
        resta_almacenada=num1-num2
        return resta_almacenada

print(suma(5, 5))

# VAMOS A ENTENATR HACER VALORACION DE EDADES.
# LO HICE MAL PORQUE ME ME EMPRIME "TODO".
num1=2
if num1<=17:
    print("eres menor de edad")
if num1<=6:
    print("eres muy pequenio")
if num1<=2:
    print("eres bebe")
else:
    print("eres mayor de edad")

# practica hasta el ideo 9.

print ("practicando el lunes 17 de abril del 2023")

print("         LISTAS")
lista=[1, 2, 3, 4, 5]
print(lista[0:2])
print(lista[:])
print(lista[4])
print(17 in lista)
lista.append(6)
print(lista[:])
lista.insert(0, 8)
print(lista[:])
lista.extend([7, 9, 10, 11, 12])
print(lista[:])

lista.remove(12)
print(lista[:])

lista.pop()
print(lista[:])

lista1=[11, 12, 13, 14, 15]
lista2=lista+lista1
print(lista2)

lista1=[11, 12, 13, 14, 15] * 3
print(lista1[:])



