import os
os.system("cls")

kilometros = int(input("Kilometros : "))
pies = int(input("Pies : "))
millas = int(input("Millas : "))

metros = kilometros * 1000 +  pies / 3.2808   + millas * 1609

print(f"Metros = {format(metros,'.2f')}")
print()
