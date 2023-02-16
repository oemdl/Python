import os
os.system("cls")

numero = int(input("Número : "))
numeroSuma = numero

c1 = numero // 1000
c2 = (numero  % 1000) // 100
c3 = ((numero  % 1000) % 100) // 10
c4 = numero % 10
print(f"Suma -> {(c1+c2+c3+c4)}")
print(f"Suma -> {c1} {c2} {c3} {c4}")

c1 = numero // 1000
numero %= 1000        # numero = numero % 1000
c2 = numero  // 100
numero %= 100         # numero = numero % 100
c3 = numero  // 10
c4 = numero % 10
print(f"Suma -> {(c1+c2+c3+c4)}")
print(f"Suma -> {c1} {c2} {c3} {c4}")

numero = str(numeroSuma)
suma = 0
for x in numero : suma += int(x)
print(f"Suma -> {suma}")