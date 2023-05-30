from ProjetoGrafos1 import *

def LerArquivo(Grafo):

    #Lê o arquivo
    
    with open('GrafoProjeto.txt') as f:

        Lista = [line.strip() for line in f.readlines()]

    for i in range(int(Lista[1])):

        Numero, Nome = Lista[i + 2].split(",")

        #Insere os Prédios no Grafo
        Grafo.InserirVertice(int(Numero), Nome)

    for i in range(int(Lista[int(Lista[1]) + 2])):

        Saida, Entrada, Valor = Lista[int(Lista[1]) + 3 + i].split(",")

        #Insere as Arestas no Grafo
        Grafo.InserirAresta(int(Saida), int(Entrada), int(Valor))

    return Grafo

def MostrarArquivo():

    #Mostra o conteúdo do arquivo

    with open('GrafoProjeto.txt') as f:

        Lista = [line.strip() for line in f.readlines()]

        print(end="\n")

        for i in range(len(Lista)):
            
            print(Lista[i])

        print(end="\n")

def GravarArquivo(Grafo):

    #Grava o conteúdo do Grafo no Arquivo

    f = open("backupGrafoProjeto.txt", "w")
    
    f.write("6\n")
    
    f.write(str(Grafo.G.number_of_nodes()) + "\n")

    for vertice in Grafo.G.nodes():

        f.write(str(vertice) + "," + Grafo.listaNomes[vertice] + "\n")
        
    f.write(str(Grafo.G.number_of_edges()) + "\n")

    for u, v, weight in Grafo.G.edges(data='weight'):

        f.write(str(u) + "," + str(v) + "," + str(weight) + "\n")
    
    f.close()

def InputInt(mensagem):

    #Função que pede ao usuário digitar um número do tipo int positivo

    while(True):

        retorno = input(mensagem)

        try:

            if int(retorno) == float(retorno) and int(retorno) > 0:

                return int(retorno)
            
        except:

            print("Entrada Invalida!, tente novamente\n")

def MostrarMenu():
    print("                   Menu                   ")
    print("+----------------------------------------+")
    print("|1) Ler dados do arquivo .txt            |")
    print("|----------------------------------------|")
    print("|2) Gravar dados no arquivo .txt         |")
    print("|----------------------------------------|")
    print("|3) Inserir vértice                      |")
    print("|----------------------------------------|")
    print("|4) Inserir aresta                       |")
    print("|----------------------------------------|")
    print("|5) Remove vértice                       |")
    print("|----------------------------------------|")
    print("|6) Remove aresta                        |")
    print("|----------------------------------------|")
    print("|7) Mostrar conteúdo do arquivo          |")
    print("|----------------------------------------|")
    print("|8) Mostrar grafo                        |")
    print("|----------------------------------------|")
    print("|9) Mostrar a conexidade do grafo        |")
    print("+----------------------------------------+")
    print("|10) Menor Caminho                       |")
    print("+----------------------------------------+")
    print("|11) Encerrar a aplicação                |")
    print("+----------------------------------------+")

Run = True

g = Grafo()

while Run:

    MostrarMenu()

    #Pede ao usuário digitar qual opção ele vai querer fazer
    Escolha = InputInt("O que vamos fazer? ")        

    #1) Ler dados do arquivo grafo.txt
    if Escolha == 1:

        g = LerArquivo(g)

    #2) Gravar dados no arquivo .txt
    elif Escolha == 2:

        GravarArquivo(g)
        
    #3) Inserir vértice
    elif Escolha == 3:

        Num = InputInt("Qual o numero do predio que estamos adicionando? ")

        Name = input("Qual o nome do predio que estamos adicionando? ")

        if g.InserirVertice(Num, Name):

            print("Predio Inserido com sucesso!\n")

        else:

            print("Falha ao inserir o Predio!, ele ja foi inserido\n")

    #4) Inserir aresta
    elif Escolha == 4:

        Saida = InputInt("De qual vertice a aresta sai? ")

        Entrada = InputInt("Qual o destino da aresta? ")

        Valor = InputInt("Qual o Valor da Aresta? ")

        if g.InserirAresta(Saida, Entrada, Valor):

            print("Aresta Inserido com sucesso!\n")

        else:

            print("Falha ao inserir a Aresta!, ela ja foi inserida\n")

    #5) Remove vértice
    elif Escolha == 5:

        Vert = InputInt("Qual o numero do predio que estamos removendo? ")

        if g.RemoverVertice(Vert):

            print("Predio Removido com sucesso!\n")

        else:

            print("Falha ao Remover o Predio!, ele nao consta no Grafo\n")
            
    #6) Remove aresta
    elif Escolha == 6:

        Saida = InputInt("De qual vertice a aresta sai? ")

        Entrada = InputInt("Qual o destino da aresta? ")

        if g.RemoverAresta(Saida, Entrada):

            print("Aresta Removida com sucesso!\n")

        else:

            print("Falha ao Remover a Aresta!, ela nao consta no Grafo\n")
            
    #7) Mostrar conteúdo do arquivo
    elif Escolha == 7:

        MostrarArquivo()

    #8) Mostrar grafo
    elif Escolha == 8:

        g.MostrarGrafo()

    #9) Mostrar a conexidade do grafo
    elif Escolha == 9:

        g.Conexidade()

    #10) Menor Caminho
    elif Escolha == 10:

        Saida = InputInt("De qual vertice a aresta sai? ")

        Entrada = InputInt("Qual o destino da aresta? ")

        #Verifica se a Saida e a Entrada pertencem ao Grafo
        if Saida in g.G.nodes() and Entrada in g.G.nodes():

            g.Dijkstra(Saida, Entrada)

        else:

            print("Algum desses Predios não consta no Grafo!\n")

    #11) Encerrar a aplicação
    elif Escolha == 11:

        break

    else:

        print("Escolha um Numero entre 1 e 11!\n")
