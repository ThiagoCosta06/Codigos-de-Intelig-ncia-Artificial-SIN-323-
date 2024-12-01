import pygame
from algorithms import buscaEmLargura, buscaEmProfundidade, buscaPorFluxo

pygame.init()
largura, altura = 600, 800
tamCelula = 50
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Trabalho de Inteligência Artificial")

labirinto = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,0,0,0,1,0],
    [0,0,0,1,0,1,1,1,1,0,1,0],
    [0,1,1,1,1,0,0,0,1,0,1,1],
    [0,0,0,0,1,0,1,0,1,0,1,0],
    [0,1,1,0,1,0,1,0,1,0,1,0],
    [0,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,1,0,0,0,1,0],
    [1,1,1,1,1,1,1,0,1,1,1,0],  
    [0,0,0,0,0,0,0,0,0,0,0,0],
]

#fontes e sprites utilizadas na interface
posicaoInicialAgente = [4, 11]
objetivo = [10, 0]

spriteAgente = pygame.image.load(r"D:\Downloads\Inteligencia Artificial 2024-2\Trabalho 1\ImagemSoldadinho-removebg-preview.png")
spriteAgente = pygame.transform.scale(spriteAgente, (tamCelula, tamCelula))
spriteAgente = pygame.transform.flip(spriteAgente, flip_x=True, flip_y=False)

corFundo = (0, 0, 0)
corDoCaminho = (255, 255, 255)
corDaParede = (0, 0, 139)

alturaDoLabirinto = len(labirinto) * tamCelula

fonteTexto = pygame.font.Font(r"D:\Downloads\Inteligencia Artificial 2024-2\Trabalho 1\fontZombie.TTF", 25)
texto = "Bem vindo! Escolha uma das opcoes abaixo!"
fundoDoTexto = fonteTexto.render(texto, True, (255, 255, 0))
xTexto = (largura - fundoDoTexto.get_width()) // 2
yTexto = alturaDoLabirinto + 20

fonteCaixas = pygame.font.Font(r"D:\Downloads\Inteligencia Artificial 2024-2\Trabalho 1\fontZombie.TTF", 10)
corCaixas = (50, 150, 255)
corCaixaEscolhida = (0, 200, 100)
opcoes = ["Busca em Largura", "Busca em Profundidade", "Busca por Fluxograma"]
caixas = []
espacoEntreAsCaixas = 20
larguraDasCaixas = 150
alturaDasCaixas = 50
posicao = largura // 2 - (len(opcoes) * (larguraDasCaixas + espacoEntreAsCaixas)) // 2
yCaixas = yTexto + 60 

fontePassos = pygame.font.Font(r"D:\Downloads\Inteligencia Artificial 2024-2\Trabalho 1\fontZombie.TTF", 20)
corTextoPassos = (255, 255, 255)

#funções para desenho da interface
def desenhaLabirinto():
    for i, linhas in enumerate(labirinto):
        for j, celulas in enumerate(linhas):
            x = j * tamCelula
            y = i * tamCelula
            if celulas == 0:
                pygame.draw.rect(tela, corDaParede, (x, y, tamCelula, tamCelula))
            else:
                pygame.draw.rect(tela, corDoCaminho, (x, y, tamCelula, tamCelula))

def desenhaNumeroDePassos():
    textoPassos = f"Passos dados - {numeroDePassos}"
    renderPassos = fontePassos.render(textoPassos, True, corTextoPassos)
    xTextoPassos = (largura - renderPassos.get_width()) // 2
    yTextoPassos = yCaixas + alturaDasCaixas + 20
    tela.blit(renderPassos, (xTextoPassos, yTextoPassos))

#variaveis de controle
numeroDePassos = 0
passos = None
rodando = True
opcaoEscolhida = None
caminho = None
passoAtual = 0
posicaoDoAgente = list(posicaoInicialAgente)

for i, option in enumerate(opcoes):
    xCaixas = posicao + i * (larguraDasCaixas + espacoEntreAsCaixas)
    caixas.append(pygame.Rect(xCaixas, yCaixas, larguraDasCaixas, alturaDasCaixas))

#While da Interface grafica
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, caixa in enumerate(caixas):
                if caixa.collidepoint(event.pos):
                    opcaoEscolhida = opcoes[i]
                    if opcaoEscolhida == "Busca em Largura":
                        caminho, passos = buscaEmLargura(posicaoInicialAgente, objetivo, labirinto)
                    elif opcaoEscolhida == "Busca em Profundidade":
                        caminho, passos = buscaEmProfundidade(posicaoInicialAgente, objetivo, labirinto)
                    elif opcaoEscolhida == "Busca por Fluxograma":
                        caminho, passos = buscaPorFluxo(posicaoInicialAgente, objetivo, labirinto)
                    posicaoDoAgente = list(posicaoInicialAgente)
                    passoAtual = 0

    tela.fill(corFundo)

    desenhaLabirinto()
    xAgente = posicaoDoAgente[1] * tamCelula
    yAgente = posicaoDoAgente[0] * tamCelula
    tela.blit(spriteAgente, (xAgente, yAgente))

    tela.blit(fundoDoTexto, (xTexto, yTexto))

    for i, caixa in enumerate(caixas):
        cor = corCaixaEscolhida if opcaoEscolhida == opcoes[i] else corCaixas
        pygame.draw.rect(tela, cor, caixa)
        texto = fonteCaixas.render(opcoes[i], True, (0, 0, 0))
        tela.blit(texto, (caixa.x + (larguraDasCaixas - texto.get_width()) // 2, caixa.y + (alturaDasCaixas - texto.get_height()) // 2))        

    if caminho and passoAtual < len(caminho):
        posicaoDoAgente = caminho[passoAtual]
        passoAtual += 1
        numeroDePassos = passos

    desenhaNumeroDePassos()

    pygame.display.flip()
    pygame.time.delay(300)

print(f"Caminho percorrido: {caminho}\nPassos dados: {passos}")

pygame.quit()