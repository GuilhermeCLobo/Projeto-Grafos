import networkx as nx
import matplotlib.pyplot as plt

class Grafo:

    def __init__(self):

        self.G = nx.Graph()

        self.listaNomes = [None] * 250

    def InserirVertice(self, Numero, Nome):

        if Numero not in self.G.nodes():

            self.G.add_node(Numero)

            self.listaNomes[Numero] = Nome

            return True

        return False

    def RemoverVertice(self, Numero):

        if Numero in self.G.nodes():

            self.G.remove_node(Numero)

            self.listaNomes[Numero] = None

            return True

        return False

    def InserirAresta(self, Saida, Entrada, Valor):

        if (Saida,Entrada) not in self.G.edges():
            
            self.G.add_edge(Saida, Entrada, weight=Valor)

            return True

        return False
        
    def RemoverAresta(self, Saida, Entrada):

        if (Saida,Entrada) in self.G.edges():

            self.G.remove_edge(Saida, Entrada)

            return True

        return False
           
    def MostrarGrafo(self):

        positionX = 10

        pos = {
            1: (31, 57),
            2: (35, 59),
            3: (40, 61),
            4: (44, 64),
            5: (48, 67),
            6: (53, 60),
            7: (50, 56),
            8: (37, 55),
            9: (40, 46),
            10: (48, 53),
            11: (43, 41),
            12: (42, 36),
            13: (44, 32),
            14: (46, 34),
            15: (39, 32),
            16: (50, 36),
            17: (46, 71),
            18: (58, 34),
            19: (54, 44),
            20: (60, 47),
            21: (72, 22),
            22: (90, 29),
            23: (57, 64),
            24: (61, 59),
            25: (64, 55),
            26: (97, 73),
            28: (67, 49),
            29: (75, 48),
            30: (75, 55),
            31: (70, 58),
            33: (76, 61),
            35: (87, 60),
            37: (80, 64),
            38: (80, 71),
            40: (86, 65),
            41: (92, 77),
            43: (50, 21),
            44: (55, 25),
            45: (66, 39),
            46: (66, 26),
            48: (76, 28),
            49: (84, 28),
            50: (87, 38),
            52: (76, 36)
        }

        for vertex in self.G.nodes():
            
            if vertex not in pos:

                pos[vertex] = (positionX, 10)

                positionX = positionX + 5
                
        nx.draw(self.G, pos=pos, with_labels=True)
        
        plt.show()
    
    def Conexidade(self):

        conexo = nx.is_connected(self.G)

        if conexo:
            
            print("Grafo conexo!\n")
            
        else:
            
            print("Grafo desconexo.\n")

    def Dijkstra(self, Saida, Entrada):

        positionX = 10

        peso_aresta = 0

        caminho_mais_curto = nx.dijkstra_path(self.G, Saida, Entrada)

        caminhos = [(caminho_mais_curto[i], caminho_mais_curto[i+1]) for i in range(len(caminho_mais_curto)-1)]

        pos = {
            1: (31, 57),
            2: (35, 59),
            3: (40, 61),
            4: (44, 64),
            5: (48, 67),
            6: (53, 60),
            7: (50, 56),
            8: (37, 55),
            9: (40, 46),
            10: (48, 53),
            11: (43, 41),
            12: (42, 36),
            13: (44, 32),
            14: (46, 34),
            15: (39, 32),
            16: (50, 36),
            17: (46, 71),
            18: (58, 34),
            19: (54, 44),
            20: (60, 47),
            21: (72, 22),
            22: (90, 29),
            23: (57, 64),
            24: (61, 59),
            25: (64, 55),
            26: (97, 73),
            28: (67, 49),
            29: (75, 48),
            30: (75, 55),
            31: (70, 58),
            33: (76, 61),
            35: (87, 60),
            37: (80, 64),
            38: (80, 71),
            40: (86, 65),
            41: (92, 77),
            43: (50, 21),
            44: (55, 25),
            45: (66, 39),
            46: (66, 26),
            48: (76, 28),
            49: (84, 28),
            50: (87, 38),
            52: (76, 36)
        }

        for vertex in self.G.nodes():
            
            if vertex not in pos:

                pos[vertex] = (positionX, 10)

                positionX = positionX + 5

        default_node_color = 'blue'

        selected_node_color = 'red'

        default_edge_color = 'black'

        node_colors = [selected_node_color if node in caminho_mais_curto else default_node_color for node in self.G.nodes]

        edge_colors = [selected_node_color if node in caminhos else default_edge_color for node in self.G.edges]
                
        nx.draw(self.G, pos=pos, node_color=node_colors, edge_color=edge_colors, with_labels=True)

        print("Distancia total: ", caminho_mais_curto, "\n")

        for i in range(len(caminho_mais_curto) - 1):

            peso_aresta = peso_aresta + self.G.get_edge_data(caminho_mais_curto[i], caminho_mais_curto[i + 1])['weight']
            
        print("Distancia total: ", peso_aresta, "\n")
        
        plt.show()
