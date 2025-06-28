#Genere una estructura de datos que permita contener un listado de notas por alumno

# codigo: codigo_alumno
# nombres: nombres
# apellidos: apellidos 


# curso: nombre_curso
# credito: num_creditos
# nota: 

diccionario_notas_alumno = {
    "codigo": "21120337",
    "nombre": "Dante",
    "apellido": "Pacheco",
    "cursos": [
        {"curso": "Matematica para economistas", "num_creditos": 5, "nota": 18},
        {"curso": "Econometria", "num_creditos": 15, "nota": 15}
    ]
}

#quiero agregar un curso más en el listado
diccionario_notas_alumno['cursos'].append(
    {"curso": "Finanzas Internacionales", "num_creditos": 4, "nota": 15}
)

#Eliminando un curso del listado por posicion
diccionario_notas_alumno['cursos'].remove(0)

#Quiero saber cuantos cursos está llevando este alumno
len(diccionario_notas_alumno['cursos'])

#Cual es el codigo de este alumno
diccionario_notas_alumno['codigo']

#Supongamos que queremos tener la nota de 3 alumnos

listado_alumnos = [
    diccionario_notas_alumno,
    diccionario_notas_alumno2,
    diccionario_notas_alumno3
]





