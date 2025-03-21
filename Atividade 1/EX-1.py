inteiro = int(input("Diga o primeiro numero: "))
inteiro2 = int(input("Diga o segundo numero: "))
inteiro3 = int(input("Diga o terceiro numero: "))
media = inteiro + inteiro2 + inteiro3 / 3
media_ponderada = (inteiro * 2 + inteiro2 * 2 + inteiro3 * 3) / 7
media_ponderada2 = (inteiro * 1 + inteiro2 * 2 + inteiro3 * 3) / 5
print(f"A média aritmética é: {media}")
print(f"A média ponderada, considerando os pesos 2, 2 e 3, é: {media_ponderada}")
print(f"A média ponderada, considerando os pesos 1. 2, 2 é: {media_ponderada2}")