import pandas as pd
import operator as op
import colorama as color

numero_alumnos = 16

def crearDiccionarios():
    alumnos = []
    datos = pd.read_csv("./modules/calificaciones.csv", header=0 , sep =";")
    for i in range(numero_alumnos):
        alumnos.append({
            'Nombre': datos['Nombre'][i],
            'Apellidos': datos['Apellidos'][i],
            'Asistencia': datos['Asistencia'][i],
            'Parcial1': datos['Parcial1'][i],
            'Parcial2': datos['Parcial2'][i],
            'Ordinario1': datos['Ordinario1'][i],
            'Ordinario2': datos['Ordinario2'][i],
            'Practicas': datos['Practicas'][i],
            'OrdinarioPracticas': datos['OrdinarioPracticas'][i]
        })
    print(sorted(alumnos, key = op.itemgetter('Apellidos')))
    return sorted(alumnos, key = op.itemgetter('Apellidos'))

def notaMedia():
    alumnos_ = crearDiccionarios()
    alumnos = alumnos_
    for i in range(numero_alumnos):
        alumnos[i]['Parcial1'] = alumnos[i]['Parcial1'].replace(',', '.')
        alumnos[i]['Parcial2'] = alumnos[i]['Parcial2'].replace(',', '.')
        alumnos[i]['OrdinarioPracticas'] = str(alumnos[i]['OrdinarioPracticas']).replace(',', '.')
        alumnos[i]['Practicas'] = str(alumnos[i]['Practicas']).replace(',', '.')
        notas = [alumnos[i]['Parcial1'], alumnos[i]['Parcial2'], alumnos[i]['OrdinarioPracticas'], alumnos[i]['Practicas']]
        for j in range(len(notas)):
            if str(notas[j]) == 'nan':
                notas[j] = 0
        nota_media = (float(notas[0]) * 0.3) +  (float(notas[1]) * 0.3) + (float(notas[2]) * 0.6)
        alumnos[i]['NotaMedia'] = nota_media
    print(alumnos)
    return alumnos

def aprobadosSuspensos():
    alumnos = notaMedia()
    aprobados = []
    suspensos = []
    for i in range(numero_alumnos):
        if float(alumnos[i]['Parcial1']) >= 4 and float(alumnos[i]['Parcial2']) >= 4 and float(alumnos[i]['Practicas']) >= 4 and float(alumnos[i]['NotaMedia']) >= 5:
            aprobados.append(alumnos[i])
        else:
            suspensos.append(alumnos[i])
    print('Alumnos Aprobados\n')
    for j in range(len(aprobados)):
        print(color.Fore.GREEN + aprobados[j]['Nombre'])
    print(color.Style.RESET_ALL)
    print('\n')
    print('Alumnos Suspensos\n')
    for v in range(len(suspensos)):
        print(color.Fore.RED + suspensos[v]['Nombre'])
    print(color.Style.RESET_ALL)