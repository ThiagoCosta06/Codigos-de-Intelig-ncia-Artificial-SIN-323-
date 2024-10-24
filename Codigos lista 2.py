import networkx as nx 

def criar_grafo():
    grafo = nx.Graph()

    grafo.add_node("A", pos=(0,0))
    grafo.add_node("B", pos=(1,0))
    grafo.add_node("C", pos=(0,1))
    grafo.add_node("D", pos=(1,1))
    grafo.add_node("E", pos=(0,2))
    grafo.add_node("F", pos=(1,2))

    grafo.add_edge("A", "B", weight=1)
    grafo.add_edge("A", "C", weight=4)
    grafo.add_edge("B", "D", weight=2)
    grafo.add_edge("C", "D", weight=1)
    grafo.add_edge("C", "E", weight=5)
    grafo.add_edge("D", "F", weight=3)
    grafo.add_edge("E", "F", weight=2)

    return grafo

def a_star(grafo, start, goal, heuristic):
    custo_total = 0
    abertos = {start: 0}
    fechados = set()
    coordenadas = nx.get_node_attributes(grafo, 'pos')

    while abertos:
        atual = min(abertos, key=abertos.get)
        
        if atual == goal:
            print(f"Caminho encontrado: {atual}")
            return custo_total
        
        del abertos[atual]
        fechados.add(atual)
        
        for vizinho in grafo.neighbors(atual):
            if vizinho in fechados:
                continue

            x1, y1 = coordenadas[vizinho]
            x2, y2 = coordenadas[goal]
            manhattan = heuristic(x1, y1, x2, y2)
            
            peso_aresta = grafo[atual][vizinho]['weight']
            custo_total = peso_aresta + manhattan
            
            if vizinho not in abertos or custo_total < abertos[vizinho]:
                abertos[vizinho] = custo_total

    print("Caminho não encontrado")
    return 

def heuristic(x1, y1, x2, y2):
    dist_manhattan = abs(x1 - x2) + abs(y1 - y2)
    return dist_manhattan

grafo = criar_grafo()
resposta = a_star(grafo, "A", "F", heuristic)
print(resposta)

