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

#
