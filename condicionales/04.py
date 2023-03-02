import os
os.system("cls")

N1 = int(input("N1 : "))
N2 = int(input("N2 : "))
N3 = int(input("N3 : "))

if N3 >= 10 and N3 <= 18 : N3 += 2  # N3=N3 + 2
promedio = (N1+N2+N3)/3.0

print(f"Promedio = { format(promedio,'.2f') }")
print()