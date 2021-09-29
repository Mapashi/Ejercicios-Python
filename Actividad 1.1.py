#1.1 Introduciendo la hora del día en horas, minutos y segundos, calcular cuántos segundos han transcurrido desde el comienzo del día
horas = int(input("Introduce la hora: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))
total = segundos + minutos * 60 + horas * 3600
