# LISTAS NO PERMITE ALMACENAR A DIFERENCIA DE UBA VARIABLE ALMACENAR VARIOS VALORES.
# SITACSIS NOMBRE VARIBALE IGUAL ENTRE CORCHETES EL ELEMENTO SEPARADO CON COMAS.
# EL PRIMERO ELEEMNTO TIENE UN INDICE 0 TENIENDO ENCUNETA LOS NUMERO BINARIOS EMPEZAMOS SIEMPRE DESDE CERO.
print("Imprimir un elemento o varios en una lista")
lista=["maria", "amor", "jesus", "amir"]
print(lista[:])
print(lista[2])
# si ponemos -2 empieza a contar desde -1 no 0.
print(lista[-2])
# aquinos deja el 3 exluido no lo conta emprime hasta el 2 contando desde 0.
print(lista[0:3])
# nos va a imprimir solo 1 por quitamos el numero 2.
print(lista[1:2])
# en ests accede desde el 2 hasta el ultimo.
print(lista[2:])

print("         Agregar un elemento a la lista NOMBRELISTA.APPEND")
# pero append lo pone al final de lista.
lista=[1, 2, 3, 4]
print(lista[:])
lista.append(5)
print(lista[:])

print("         Aniadir un elemento pero en el indice que queramos.")

print(lista[:])

lista.insert(2, 6)
print(lista[:])

print("         Agrigar varios elementos a una lista es como concatenar una otra lista, en este caso utilizaremos .extend . ")

lista=["a", "b", "c"]
print(lista[:])
lista.extend(["d", "e", "f"])
print(lista[:])

print(lista.index("b"))

print("         Comprobar si una lista existe un elemento o no.")
lista=[10, 11, 12, 13]
print(lista[:])
print(16 in lista)

print("         ELIMINANDO UN ELEMENTO EN LA SIGUIENTE LISTA.")
lista=[10, 11, 12, 13]
print(lista[:])
lista.remove(10)
print(lista[:])


print("         ELIMINAR EL ULTIMO ELMENTO EN LA LISTA.")

lista=[0, "abdel", "moha", 2, 3]
print(lista[:])
lista.pop()
print(lista[:])

print("         unir dos los listas en una tercera.")
lista=[0, "abdel", "moha", 2, 3]
print(lista[:])
lista1=[4, 5, 6]
print(lista1[:])
lista2=lista+lista1
print(lista2[:])

print("         Multiplicar la lista las veces que queremos.")

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 3
print(lista[:])

coment="""           LO APRENDIDO SOBRE LISTAS EN ESTE ARCHIVO.PY
APPEND : se utiliza para añadir unelemnto a una lista.
insert : insertar un elemento en el indice que tu quieras.
extend : insertar un nueva lista dento de tu lista.
index  : saber en que indece se incuentra cada elemento.
in ... : sirve para comprobar si en mi lista existe el elemento o no (true o false).
remove : sirve para eliminar un elemento de la lista.
pop    : sireve para eliminar el ultimo elemnto de la lista.
*      : sirve para multiplicar un lista las veces que queramos *3 *4 etc... ."""

print(coment)

