inteiro = int(input("Diga o valor em reais: "))
if inteiro > 500:
	valor_real = inteiro + (inteiro / 2)
	print(f"Você deverá pagar: {valor_real}")
else:
	print("Você não pagará impostos")
