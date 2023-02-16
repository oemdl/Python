import os
import math

os.system("cls")

radio = int( input("Radio : ") )
altura = int( input("Altura : ") )

area = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * math.pow(radio,2) * altura

print ( f"Área = { format(area,'.2f')} u2" )
print ( f"Volúmen = { format(volumen,'.2f')} u3" )
print()
