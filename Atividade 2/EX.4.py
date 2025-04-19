usuario = input("Digite seu usuário: ")
senha = input("Digie sua senha: ")
transacoes = []
while True:
    acao = input("O que deseja fazer?: ")
    if acao == "saque" or "deposito":
        transacoes.append(acao)
        print("suas transações são:", transacoes)
    else:
        break
