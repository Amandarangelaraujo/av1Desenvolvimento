inicial = 0
listaTarefas = []
while(inicial==0):
    menu = int(input("digite : \n 1 para adicionar uma tarefa \n 2 para listar tarefa \n 3 para marcar como concluída \n 4 para sair \n"))

    if (menu==1):
        tarefa = input("digite uma tarefa \n")
        listaTarefas.append(tarefa)
        
    elif (menu==2):
        for i in range (len(listaTarefas)):
            print(listaTarefas[i])
        print(" ")

    elif (menu==3):
        for i in range (len(listaTarefas)):
            print(listaTarefas[i])
        x = int(input("digite a posição da tarefa que você quer concluir"))
        listaTarefas.pop(x+1)
        for i in range (len(listaTarefas)):
            print(listaTarefas[i])
    elif(menu==4):
        break;




