import pandas as pd

numero_alumnos = 16

def crearDiccionarios():
    alumnos = []
    datos = pd.read_csv("./modules/calificaciones.csv", header=0 , sep =";")
    for i in range(numero_alumnos):
        alumnos.append({
            'Nombre': datos['Nombre'][i],
            'Apellidos': datos['Apellidos'][i],
            'Asistencia': datos['Asistencia'][i],
            'Primer Parcial': datos['Parcial1'][i],
            'Segundo Parcial': datos['Parcial2'][i],
            'Primer Ordinario': datos['Ordinario1'][i],
            'Segundo Ordinario1': datos['Ordinario2'][i],
            'Practicas': datos['Practicas'][i],
            'Ordinario Practicas': datos['OrdinarioPracticas'][i],
        })
    return alumnos

def notaMedia():
    alumnos = crearDiccionarios()

notaMedia()