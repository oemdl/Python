import os
os.system("cls")

unidades = int(input("Unidades : "))

precio = 23
if unidades <= 25 : precio = 27
elif unidades > 25 and unidades <= 50 : precio = 25

#precio = 25
#if unidades <= 25 : precio = 27
#elif unidades > 50 : precio = 23

#precio = 27 if unidades <= 25 else 23 if unidades > 50 else 25
 
compra = precio * unidades

if unidades > 50 : descuento = 0.15 * compra
else : descuento = 0.05 * compra

descuento = 0.05 * compra
if unidades > 50 : descuento = 0.15 * compra

decuento = ( 0.15 if unidades > 50 else 0.05 ) * compra

total = compra - descuento

print (f"Precio    = S/ {format(precio,'.2f')}")
print (f"Compra    = S/ {format(compra,'.2f')}")
print (f"Descuento = S/ {format(descuento,'.2f')}")
print (f"Total     = S/ {format(total,'.2f')}")
