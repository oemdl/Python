import os
os.system("cls")

codigo = int(input("Código : "))

#if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0 : tipo = "Administrativo"
#elif not codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0 : tipo = "Directivo"
#elif codigo % 2 == 0 and not codigo % 3 == 0 and not codigo % 5 == 0 : tipo = "Vendedor"
#elif not codigo % 2 == 0 and not codigo % 3 == 0 and not codigo % 5 == 0 : tipo = "Seguridad"
#else : tipo = "Error"

d2 = codigo % 2 == 0
d3 = codigo % 3 == 0
d5 = codigo % 5 == 0

if       d2 and     d3 and     d5 : tipo = "Administrativo"
elif not d2 and     d3 and     d5 : tipo = "Directivo"
elif     d2 and not d3 and not d5 : tipo = "Vendedor"
elif not d2 and not d3 and not d5 == 0 : tipo = "Seguridad"
else : tipo = "Error"

print(f"Tipo = {tipo}")
print()