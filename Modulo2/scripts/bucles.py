#Imprime la palabra "Hola" 10 veces

print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")

print('Fin proceso ....')

#Existen estructuras que me facilitan realizar una tarea multiples veces
#for / while
#for -> sirve para realizar una tarea cierto numero de veces

#for una_variable in ITERABLE:
#Para cada elemento en el agrupador de elementos (lista, tupla, diccionario, conjuntos), realizo una tarea
for _ in range(10):
    print("Hola")
print('Fin Bucle For ....')

#white -> sirve para realizar una tarea hasta que se cumpla una condicion
contador = 1
#Mientras algo sea verdad, realizo la tarea
while contador <= 10:
    print("Hola")
    contador += 1
print('Fin Bucle While ....')

#Control + X -> para matar proceso en bucle infinito 
#realizarlo sobre el terminal