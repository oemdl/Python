import os
os.system("cls")

numero = int( input("Número : ") )

#if numero > 0 : signo = "Positivo"
#elif numero == 0 : signo = "Cero"
#else : signo = "Negativo"

#signo = "Positivo"
#if numero == 0 : signo = "Cero"
#elif numero < 0 : signo = "Negativo"

#signo = "Positivo" if numero > 0 else "Cero" if numero == 0 else "Negativo"

print(f'Signo = { ("Positivo" if numero > 0 else "Cero" if numero == 0 else "Negativo") }')
print()