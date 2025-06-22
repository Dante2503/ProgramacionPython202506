""""
Ingrese la base y la altura de un triangulo, luego realice el calculo del parea. Por último, muestre el resultado en pantalla
"""

#1.Ingreso de datos
base_triangulo = int(input('Ingrese la base del triangulo: '))
altura_triangulo = int(input('Ingrese la altura del triangulo: '))

print(type(base_triangulo))

#2. Calcular el area del triangulo

area_triangulo = base_triangulo * altura_triangulo /2

#3. Imprimir resultado

print(area_triangulo)

#Imprimiendo con "f" format string delante del texto

print(f'El area del triangulo con base {base_triangulo} y altura {altura_triangulo} es : {area_triangulo}')

print('Base {base}\nAltura {altura}\nArea {area}'.format(base=base_triangulo,altura=altura_triangulo, area=area_triangulo))