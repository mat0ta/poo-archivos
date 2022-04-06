import sys
sys.path.insert(1, './modules')
from modules import *
from src.totareadme import readme

array_ejercicios = {
  1: 'module.funtion()'
}

if __name__ == "__main__":
    readme('DIRECTORIO')
    start = input('Bienvenido a la plataforma de ejecución de ejercicios. Por favor, introduzca el número del ejercicio que quiere probar (1 a 10) o introduzca 0 para salir: ')
    while int(start) >= 1 and int(start) <= 10:
        eval(str(array_ejercicios[int(start)]))
        start = input('Por favor, introduzca el número del ejercicio que quiere probar (1 a 10) o introduzca 0 para salir: ')