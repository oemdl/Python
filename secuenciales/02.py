import os
os.system("cls")

metros = int(input("Metros : "))

centimetros = metros * 100.0
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print(f"Centimetros = {format(centimetros,'.2f')}")
print(f"Pulgadas    = {format(pulgadas,'.2f')}")
print(f"Pies        = {format(pies,'.2f')}")
print(f"Yardas      = {format(yardas,'.2f')}")
print()
