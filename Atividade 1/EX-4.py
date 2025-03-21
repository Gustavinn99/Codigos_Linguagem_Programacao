inteiro = int(input("Diga o valor em quilometros: "))
if inteiro > 100:
	valor_real = 90 + (inteiro * 12)
	print(f"O valor pago deverá ser {valor_real}")
else:
	print(f"O valor pago deverá ser {inteiro}")