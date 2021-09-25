#!/usr/bin/env python3

dic = {}

for i in range(3):
    alum = str(input("ingrese el nombre del alumno: ")).lower
    notas = int(input("Ingrese la nota: "))
    if notas < 0 or notas > 10:
        print("reingrese la nota")
        notas = int(input("Ingrese la nota: "))
    dic[alum] = notas

print(dic)