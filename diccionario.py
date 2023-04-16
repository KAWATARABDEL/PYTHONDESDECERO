print("         mostrar la edad de cada persona con la clae de un deccionario. ")
diccionario={"abdel":18, "amin":1, "yasmine":10, "najat":39, "mohamed":49}
print(diccionario["abdel"])

print("         mostrar todo el deccionario. ")
print(diccionario)

print("         agregar mas elementos a un deccionario.")

diccionario={"abdel":18, "amin":1}
diccionario["mohamed"]= 49
print(diccionario)

print("         corregir una  clave donde me he equiocado.")
diccionario={"abdel":18, "amin":1, "mohamed":49}
diccionario["mohamed"]=50
print(diccionario)


print("         como elimin ar un elemento en un diccionario.")

diccionario={"abdel":18, "amin":1, "yasmiine":10}
del diccionario["abdel"]
print(diccionario)



print("         clave con una tupla y le asgnamos alor con un diccionario. ")

tupla=["abdel", "amin", "yasmine", "najat", "mohamed"]
diccionario={tupla[0]:19, tupla[1]:1, tupla[2]:10, tupla[3]:39, tupla[4]:49}
print(diccionario)
print(diccionario["amin"])

print("         almacenar una tupla de elementos dentro de una clave de un diccionario.")

diccionario={"abdel":19, "es tudios":"FP", "anillos":[2020, 2021, 2022, 2023]}
print(diccionario)
print(diccionario["anillos"])

print(diccionario["anillos"][0])


print("         almacenar un diccionario dentro de otro diccioario. ")

diccionario={"a":1, "b":2, "c":3, "c":{"d":[1, 2, 3, 4, 5]}}
print(diccionario)
print(diccionario["c"])


print("         imprimir las claes que pertenecen a un diccionario.")

diccionario={"abdel":18, "amin":1, "yasmine":10, "najat":39, "mohamed":49}
print(diccionario.keys())


print("         imprimir los valores de un diccionario .")

diccionario={"abdel":18, "amin":1, "yasmine":10, "najat":39, "mohamed":49}
print(diccionario.values())


print("         imprimir la lungitud o conjuntos de un diccionario.")

diccionario={"abdel":18, "amin":1, "yasmine":10, "najat":39, "mohamed":49}
print(len(diccionario))