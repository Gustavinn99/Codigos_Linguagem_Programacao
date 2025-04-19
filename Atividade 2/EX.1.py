tarefas = []
prazo = []
while True:
    acao = input("Qual a sua acao?: ")
    if acao == "adicionar":
        atv = input("Qual suas tarefas?: ")
        tarefas.append(atv.split(","))
        praz = input("Quais são os prazos de suas tarefas?: ")
        prazo.append(praz.split(","))
    elif acao == "consultar":
        print("Suas tarefas são: ", tarefas)
        print("Seus prazos são:", prazo)
    elif acao == "concluir":
        tarefa = int(input("Qual tarefa deve ser concluida?: "))
        tarefas.pop(tarefa)
    else:
        break
