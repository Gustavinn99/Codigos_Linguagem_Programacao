item = []
preco = []
while True:
    acao = input("Qual a sua acao?: ")
    if acao == "adicionar":
        iten = input("Quais os itens?: ")
        item.append(iten.split(","))
        prec = input("Quais são os preços de seus itens?: ")
        preco.append(prec.split(","))
    elif acao == "consultar":
        print("Seus itens são: ", item)
        print("Seus preçoes são:", preco)
    else:
        break