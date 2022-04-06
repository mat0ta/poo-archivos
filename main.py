import sys
sys.path.insert(1, './modules')
from modules import archivos
from src.totareadme import readme

array_ejercicios = {
  1: 'archivos.crearDiccionarios()',
  2: 'archivos.notaMedia()',
  3: 'archivos.aprobadosSuspensos()'
}

if __name__ == "__main__":
    readme('C:/Users/marti/Documents/GitHub/poo-archivos')
    start = input('Bienvenido a la plataforma de ejecución de ejercicios. Por favor, introduzca el número del ejercicio que quiere probar (1 a 3) o introduzca 0 para salir: ')
    while int(start) >= 1 and int(start) <= 3:
        eval(str(array_ejercicios[int(start)]))
        start = input('Por favor, introduzca el número del ejercicio que quiere probar (1 a 3) o introduzca 0 para salir: ')