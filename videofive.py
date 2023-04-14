#función permite ejecutar un codigo las veces que queramos menos codigo y mas rapido.
# de nombre de función y dos parentesis de parametros y dos puntos siempre.
# def nombre(parametros)
# hay dos tipos (la que devuelve valores que lleva el "return") (y la que no que no lleva "return")

def nombre():
    
    print("abdel")
    print("yasmine")
    print("amin")

nombre()
print("estoy entre dos llamadas de una fucion")
nombre()

# suma con una función.

def suma():
    num0=1
    num1=3
    print(num0+num1)
suma()


# suma con una función pero que sume diferentes valores en cada llamada.
# se utiliza parametros o argomentos.

def suma(num2, num3):
    print(num2+num3)
    
suma(3, 6)
suma(3, 3)

# ahora una funcion  con return como se fuese una maquina de patatas pones codigo te da producto.
# recibe parametros y te da resultado.
# tambien puedo poner una varibale y guardo la resta de dos numeros dentro de ella para un futuro poder-
# ejecutarla las veces que queramos.
# lo que esta con puntos rojos es la varibale que pose por mi cuneta para que esta pueda ser ejecutada
# con print cuando quiera.

def resta(num1, num2):
    resultado=num1-num2
    return resultado

print(resta(2, 1))
print(resta(10, 4))

almacena_por_tiempo=resta(5,4)
print(almacena_por_tiempo)


