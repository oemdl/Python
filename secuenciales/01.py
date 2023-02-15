import os
os.system("cls")

varones = int(input("Varones : "))
mujeres = int(input("Mujeres : "))

total = varones + mujeres
pvarones = varones * 100.0 / total
pmujeres = mujeres * 100.0 / total

print(f"%Varones = { format(pvarones, '.2f')} %")
print(f"%Mujeres = { format(pmujeres, '.2f')} %")
print()
