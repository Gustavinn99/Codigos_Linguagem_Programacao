numero = int(input("Diga um número: "))
numero2 = int(input("Diga um número: "))
numero3 = int(input("Diga um número: "))

if numero > numero2 and numero3:
    print(f"O maior número é: {numero}")
elif numero2 > numero and numero3:
    print(f"O maior número é: {numero2}")
elif numero3 > numero and numero2:
    print(f"O maior número é: {numero3}")
if numero < numero2 and numero3:
     print(f"O menor número é: {numero}")
elif numero2 < numero and numero3:
    print(f"O menor número é: {numero2}")
elif numero3 < numero and numero2:
    print(f"O menor número é: {numero3}")
else:
    print("Não existe um número maior")