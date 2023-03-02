import os
os.system("cls")

numero = int(input("Número : "))

#if numero == 1 : dia = "Lunes"
#elif numero == 2 : dia = "Martes"
#elif numero == 3 : dia = "Miércoles"
#elif numero == 4 : dia = "Jueves"
#elif numero == 5 : dia = "Viernes"
#elif numero == 6 : dia = "Sábado"
#elif numero == 7 : dia = "Domingo"
#else : numero = "error"
#print(f"Día = {dia}")

dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

if numero >= 1 and numero <= 7 : 
    print(f"Día = {dias[numero-1]}")
else : print("Error")
print()