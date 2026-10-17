import pygame
import sys
import random
import os

pygame.init()
LARGURA, ALTURA = 800, 600
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Forca com Pygame")

RELOGIO = pygame.time.Clock()

BRANCO = (255, 255, 255)
PRETO = (20, 20, 20)
VERMELHO = (220, 60, 60)
VERDE = (60, 160, 60)

fonte_palavra = pygame.font.SysFont("Courier New", 44, bold=True)
fonte_texto = pygame.font.SysFont("Times New Roman", 26, bold=True)
fonte_aviso = pygame.font.SysFont("Times New Roman", 20, bold=True)

lista_palavras = [
    "vermelho", "amarelo", "piscina", "janela", 
    "laranja", "musica", "viagem", "futebol", 
    "basquete", "praia", "roxo", "azul", "verde"
]

def reiniciar_jogo():
    global palavra_secreta, palavra_oculta, letras_certas, letras_erradas_ordem, vidas_atuais, jogo_acabou, mensagem_status
    palavra_secreta = random.choice(lista_palavras).lower()
    palavra_oculta = ["_" for _ in palavra_secreta]
    letras_certas = set()
    letras_erradas_ordem = [] 
    vidas_atuais = 6
    jogo_acabou = False
    mensagem_status = ""

reiniciar_jogo()

def desenhar_texto_multilinhas(superficie, texto, x, y, cor, fonte, espacamento=4):
    linhas = texto.split('\n')
    altura_linha = fonte.get_linesize() + espacamento
    for i, linha in enumerate(linhas):
        superficie_texto = fonte.render(linha, True, cor)
        superficie.blit(superficie_texto, (x, y + (i * altura_linha)))

def desenhar_boneco(erros):
    pygame.draw.line(janela, PRETO, (100, 500), (300, 500), 6) 
    pygame.draw.line(janela, PRETO, (180, 500), (180, 150), 6) 
    pygame.draw.line(janela, PRETO, (180, 150), (320, 150), 6) 
    pygame.draw.line(janela, PRETO, (320, 150), (320, 200), 4) 

    if erros >= 1:
        pygame.draw.circle(janela, PRETO, (320, 230), 30, 4)
    if erros >= 2: 
        pygame.draw.line(janela, PRETO, (320, 260), (320, 380), 4)
    if erros >= 3: 
        pygame.draw.line(janela, PRETO, (320, 290), (270, 340), 4)
    if erros >= 4: 
        pygame.draw.line(janela, PRETO, (320, 290), (370, 340), 4)
    if erros >= 5: 
        pygame.draw.line(janela, PRETO, (320, 380), (280, 460), 4)
    if erros >= 6: 
        pygame.draw.line(janela, PRETO, (320, 380), (360, 460), 4)

rodando = True
while rodando:
    janela.fill(BRANCO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN and jogo_acabou:
                reiniciar_jogo()
            
            elif not jogo_acabou:
                if evento.key >= pygame.K_a and evento.key <= pygame.K_z:
                    letra = pygame.key.name(evento.key).lower()
                    
                    if letra not in letras_certas and letra not in letras_erradas_ordem:
                        if letra in palavra_secreta:
                            letras_certas.add(letra)
                            for i, l in enumerate(palavra_secreta):
                                if l == letra:
                                    palavra_oculta[i] = letra
                            
                            if "_" not in palavra_oculta:
                                jogo_acabou = True
                                mensagem_status = "Voce venceu! Pressione ENTER \npara reiniciar"
                        else:
                            letras_erradas_ordem.append(letra) 
                            vidas_atuais -= 1
                            
                            if vidas_atuais <= 0:
                                jogo_acabou = True
                                palavra_oculta = list(palavra_secreta)
                                mensagem_status = "Voce perdeu! Pressione ENTER \npara reiniciar"

    desenhar_boneco(6 - vidas_atuais)

    texto_palavra = fonte_palavra.render(" ".join(palavra_oculta).upper(), True, PRETO)
    janela.blit(texto_palavra, (420, 250))

    erros_str = ", ".join(letras_erradas_ordem).upper()
    texto_erros = fonte_texto.render(f"Letras erradas: {erros_str}", True, VERMELHO)
    janela.blit(texto_erros, (420, 340))

    texto_vidas = fonte_texto.render(f"Vidas restantes: {vidas_atuais}/6", True, PRETO)
    janela.blit(texto_vidas, (420, 400))

    if jogo_acabou:
        cor_status = VERDE if "_" not in palavra_oculta else VERMELHO
        desenhar_texto_multilinhas(janela, mensagem_status, 420, 460, cor_status, fonte_aviso)
    else:
        surf_instrucao = fonte_aviso.render("Digite uma letra no teclado para jogar", True, PRETO)
        janela.blit(surf_instrucao, (420, 460))

    pygame.display.flip()
    RELOGIO.tick(60)

pygame.quit()
sys.exit()