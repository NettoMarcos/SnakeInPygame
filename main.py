import pygame
import random

pygame.init()
pygame.display.set_caption("Snake")
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

#cores
preta = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

#parametros snake
tamanhoQuadrado = 20
velocidade = 10

def gerarComida():
    comidaX = round(random.randrange(0, largura - tamanhoQuadrado) / tamanhoQuadrado) * tamanhoQuadrado
    comidaY = round(random.randrange(0, altura - tamanhoQuadrado) / tamanhoQuadrado) * tamanhoQuadrado
    return comidaX, comidaY

def desenharComida(tamanho, comidaX, comidaY):
    pygame.draw.rect(tela, verde, [comidaX, comidaY, tamanho, tamanho])

def desenharCobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])

def desenharPontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelho)
    tela.blit(texto,[1, 1])

def selecionarVelocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidadeX = 0
        velocidadeY = tamanhoQuadrado
    elif tecla == pygame.K_UP:
        velocidadeX = 0
        velocidadeY = -tamanhoQuadrado
    elif tecla == pygame.K_RIGHT:
        velocidadeX = tamanhoQuadrado
        velocidadeY = 0
    elif tecla == pygame.K_LEFT:
        velocidadeX = -tamanhoQuadrado
        velocidadeY = 0


    return velocidadeX, velocidadeY
def iniciarJogo():
    fimJogo = False

    x = largura / 2
    y = altura / 2

    velocidadeX = 0
    velocidadeY = 0

    tamanhoCobra = 1

    pixels = []

    comidaX, comidaY = gerarComida()

    while not fimJogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fimJogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidadeX, velocidadeY = selecionarVelocidade(evento.key)

        #desenhar comida
        desenharComida(tamanhoQuadrado, comidaX, comidaY)

        #atualizar posição snake

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fimJogo = True

        x += velocidadeX
        y += velocidadeY
        #desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanhoCobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fimJogo = True

        desenharCobra(tamanhoQuadrado, pixels)
        desenharPontuacao(tamanhoCobra - 1)

        pygame.display.update()
        #Criar nova comida
        if x == comidaX and y == comidaY:
            tamanhoCobra += 1
            comidaX, comidaY =  gerarComida()
        relogio.tick(velocidade)


iniciarJogo()