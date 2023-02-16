import os, math
os.system("cls")

radio = int(input("Radio : "))
altura = int(input("Altura : "))

areaBase = math.pi * math.pow(radio,2)
areaLateral = 2 * math.pi * radio * altura
areaTotal = 2 * areaBase * areaLateral

print(f"Área Base = {areaBase} u2")
print(f"Área Lateral = {areaLateral} u2")
print(f"Área Total = {areaTotal} u2")
print()