import time

def direcaoCima(estadoAtual, labirinto, visitados):
    proximoEstado = labirinto[estadoAtual[0]-1][estadoAtual[1]]
    coordenadas = [estadoAtual[0]-1, estadoAtual[1]]
    if coordenadas not in visitados and proximoEstado == 1:
        return proximoEstado, coordenadas
    else:
        return 0, 0

def direcaoBaixo(estadoAtual, labirinto, visitados):
    proximoEstado = labirinto[estadoAtual[0]+1][estadoAtual[1]]
    coordenadas = [estadoAtual[0]+1, estadoAtual[1]]
    if coordenadas not in visitados and proximoEstado == 1:
        return proximoEstado, coordenadas
    else:
        return 0, 0

def direcaoEsquerda(estadoAtual, labirinto, visitados):
    proximoEstado = labirinto[estadoAtual[0]][estadoAtual[1]-1]
    coordenadas = [estadoAtual[0], estadoAtual[1]-1]
    if coordenadas not in visitados and proximoEstado == 1:
        return proximoEstado, coordenadas
    else:
        return 0, 0

def direcaoDireita(estadoAtual, labirinto, visitados):
    proximoEstado = labirinto[estadoAtual[0]][estadoAtual[1]+1]
    coordenadas = [estadoAtual[0], estadoAtual[1]+1]
    if coordenadas not in visitados and proximoEstado == 1:
        return proximoEstado, coordenadas
    else:
        return 0, 0

def possiveisDirecoes(estadoAtual, labirinto):
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    cima, baixo, esquerda, direita = True, True, True, True
    if estadoAtual[0] == 0:
        cima = False
    if estadoAtual[0] == linhas - 1:
        baixo = False
    if estadoAtual[1] == 0:
        esquerda = False
    if estadoAtual[1] == colunas -1:
        direita = False
    
    return cima, baixo, esquerda, direita

def buscaEmLargura(estadoAtual, objetivo, labirinto):
    fila = []
    visitados = []
    passos = 0
    estadoAtual = [estadoAtual[0], estadoAtual[1]]
    fila.append(estadoAtual)
    while estadoAtual != objetivo:
        passos += 1
        visitados.append(fila[0])
        cima, baixo, esquerda, direita = possiveisDirecoes(estadoAtual, labirinto)
        if cima:
            proximoEstado, coordenadas = direcaoCima(estadoAtual, labirinto, visitados)
            if proximoEstado == 1:
                fila.append(coordenadas)
        if esquerda:
            proximoEstado, coordenadas = direcaoEsquerda(estadoAtual, labirinto, visitados)
            if proximoEstado == 1:
                fila.append(coordenadas)
        if direita:
            proximoEstado, coordenadas = direcaoDireita(estadoAtual, labirinto, visitados)
            if proximoEstado == 1:
                fila.append(coordenadas)
        if baixo:
            proximoEstado, coordenadas = direcaoBaixo(estadoAtual, labirinto, visitados)
            if proximoEstado == 1:
                fila.append(coordenadas)

        fila.pop(0)
        estadoAtual = fila[0]

    visitados.append(estadoAtual)
    return visitados, passos+1

def buscaEmProfundidade(estadoInicial, objetivo, labirinto):
    pilha = []
    visitados = []
    passos = 0
    estadoAtual = []
    pilha.append([estadoInicial[0], estadoInicial[1]])
    while estadoAtual != objetivo:
        passos += 1
        estadoAtual = pilha[-1]
        visitados.append(pilha[-1])
        pilha.pop(-1)
        cima, baixo, esquerda, direita = possiveisDirecoes(estadoAtual, labirinto)
        if cima:
            proximoEstado, coordenadas = direcaoCima(estadoAtual, labirinto, visitados)
            if proximoEstado == 1:
                pilha.append(coordenadas)
        if esquerda:
            proximoEstado, coordenadas = direcaoEsquerda(estadoAtual, labirinto, visitados)
            if proximoEstado == 1:
                pilha.append(coordenadas)
        if direita:
            proximoEstado, coordenadas = direcaoDireita(estadoAtual, labirinto, visitados)
            if proximoEstado == 1:
                pilha.append(coordenadas)
        if baixo:
            proximoEstado, coordenadas = direcaoBaixo(estadoAtual, labirinto, visitados)
            if proximoEstado == 1:
                pilha.append(coordenadas)

    visitados.append(estadoAtual)
    return visitados, passos

def fluxo(labirinto, objetivo):
    linhas, colunas = len(labirinto), len(labirinto[0])
    listaDistancias = [[float("inf")] * colunas for _ in range(linhas)]
    listaDirecoes = [[None] * colunas for _ in range(linhas)]

    direcoes = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    fila = []
    fila.append(objetivo)
    listaDistancias[objetivo[0]][objetivo[1]] = 0

    while len(fila) > 0:
        x, y = fila.pop(0)
        for dx, dy in direcoes:
            nx, ny = x + dx, y +dy
            if 0 <= nx < linhas and 0 <= ny < colunas and labirinto[nx][ny] == 1:
                distancia = listaDistancias[x][y] + 1
                if distancia < listaDistancias[nx][ny]:
                    listaDistancias[nx][ny] = distancia
                    listaDirecoes[nx][ny] = (-dx, -dy)
                    fila.append((nx, ny))

    return listaDistancias, listaDirecoes

def buscaPorFluxo(estadoInicial, objetivo, labirinto):
    visitados = []
    passos = 0
    distancias, direcoes = fluxo(labirinto, objetivo)
    estadoAtual = estadoInicial
    while estadoAtual != objetivo:
        visitados.append(estadoAtual)
        passos += 1
        x, y = estadoAtual
        direcao = direcoes[x][y]
        if not direcao:
            break
        estadoAtual = x + direcao[0], y + direcao[1]

        time.sleep(0.05)
        
    return visitados, passos