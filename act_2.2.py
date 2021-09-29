'''1.2 Realizar un programa que sea capaz de convertir
los grados centígrados em grados Farenheit y
viceversa.ºF = 1,8 x ºC + 32'''

print("dime los grados")
grado = input()
grado_float = float(grado)
farenheit = 1.8 * grado_float + 32
