import pygame
import sys
import random

pygame.init()
LARGURA, ALTURA = 800, 600
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pedra, Papel e Tesoura - Pygame")

RELOGIO = pygame.time.Clock()

BRANCO = (255, 255, 255)
PRETO = (30, 30, 30)
AZUL_FUNDO = (230, 240, 250)
AZUL_BOTAO = (70, 130, 180)
AZUL_BOTAO_HOVER = (100, 149, 237)
VERDE = (46, 139, 87)
VERMELHO = (178, 34, 34)
CINZA_CLARO = (210, 210, 210)

fonte_titulo = pygame.font.SysFont("Times New Roman", 36, bold=True)
fonte_texto = pygame.font.SysFont("Times New Roman", 24, bold=True)
fonte_botoes = pygame.font.SysFont("Times New Roman", 22, bold=True)

opcoes = ["pedra", "papel", "tesoura"]
escolha_jogador = ""
escolha_computador = ""
resultado_texto = "Faça sua escolha clicando nos botões abaixo!"
cor_resultado = PRETO

pontos_jogador = 0
pontos_computador = 0
empates = 0

botao_pedra = pygame.Rect(150, 420, 150, 60)
botao_papel = pygame.Rect(325, 420, 150, 60)
botao_tesoura = pygame.Rect(500, 420, 150, 60)

def jogar(escolha):
    global escolha_jogador, escolha_computador, resultado_texto, cor_resultado
    global pontos_jogador, pontos_computador, empates
    
    escolha_jogador = escolha
    escolha_computador = random.choice(opcoes)
    
    if escolha_jogador == escolha_computador:
        resultado_texto = f"Empate! Ambos escolheram {escolha_jogador.upper()}"
        cor_resultado = PRETO
        empates += 1
    elif (
        (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
        (escolha_jogador == "tesoura" and escolha_computador == "papel") or
        (escolha_jogador == "papel" and escolha_computador == "pedra")
    ):
        resultado_texto = f"Você Venceu! {escolha_jogador.capitalize()} ganha de {escolha_computador}."
        cor_resultado = VERDE
        pontos_jogador += 1
    else:
        resultado_texto = f"Você Perdeu! {escolha_computador.capitalize()} ganha de {escolha_jogador}."
        cor_resultado = VERMELHO
        pontos_computador += 1

def reiniciar_placar():
    global pontos_jogador, pontos_computador, empates, escolha_jogador, escolha_computador, resultado_texto
    pontos_jogador = 0
    pontos_computador = 0
    empates = 0
    escolha_jogador = ""
    escolha_computador = ""
    resultado_texto = "Placar reiniciado! Faça sua escolha."

rodando = True
while rodando:
    janela.fill(AZUL_FUNDO)

    mouse_pos = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: 
                if botao_pedra.collidepoint(evento.pos):
                    jogar("pedra")
                elif botao_papel.collidepoint(evento.pos):
                    jogar("papel")
                elif botao_tesoura.collidepoint(evento.pos):
                    jogar("tesoura")

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r: 
                reiniciar_placar()

    surf_titulo = fonte_titulo.render("Pedra, Papel e Tesoura", True, PRETO)
    janela.blit(surf_titulo, (LARGURA // 2 - surf_titulo.get_width() // 2, 40))

    placar_str = f"Placar >> Você: {pontos_jogador}  |  Computador: {pontos_computador}  |  Empates: {empates}"
    surf_placar = fonte_texto.render(placar_str, True, PRETO)
    janela.blit(surf_placar, (LARGURA // 2 - surf_placar.get_width() // 2, 100))

    if escolha_jogador and escolha_computador:
        texto_escolhas = f"Você: {escolha_jogador.upper()}   vs   Computador: {escolha_computador.upper()}"
        surf_escolhas = fonte_texto.render(texto_escolhas, True, PRETO)
        janela.blit(surf_escolhas, (LARGURA // 2 - surf_escolhas.get_width() // 2, 200))

    surf_resultado = fonte_texto.render(resultado_texto, True, cor_resultado)
    janela.blit(surf_resultado, (LARGURA // 2 - surf_resultado.get_width() // 2, 260))

    surf_instrucao = fonte_botoes.render("Pressione a tecla 'R' para resetar o placar", True, (100, 100, 100))
    janela.blit(surf_instrucao, (LARGURA // 2 - surf_instrucao.get_width() // 2, 340))

    cor_pedra = AZUL_BOTAO_HOVER if botao_pedra.collidepoint(mouse_pos) else AZUL_BOTAO
    pygame.draw.rect(janela, cor_pedra, botao_pedra, border_radius=8)
    texto_pedra = fonte_botoes.render("PEDRA", True, BRANCO)
    janela.blit(texto_pedra, (botao_pedra.centerx - texto_pedra.get_width()//2, botao_pedra.centery - texto_pedra.get_height()//2))

    cor_papel = AZUL_BOTAO_HOVER if botao_papel.collidepoint(mouse_pos) else AZUL_BOTAO
    pygame.draw.rect(janela, cor_papel, botao_papel, border_radius=8)
    texto_papel = fonte_botoes.render("PAPEL", True, BRANCO)
    janela.blit(texto_papel, (botao_papel.centerx - texto_papel.get_width()//2, botao_papel.centery - texto_papel.get_height()//2))

    cor_tesoura = AZUL_BOTAO_HOVER if botao_tesoura.collidepoint(mouse_pos) else AZUL_BOTAO
    pygame.draw.rect(janela, cor_tesoura, botao_tesoura, border_radius=8)
    texto_tesoura = fonte_botoes.render("TESOURA", True, BRANCO)
    janela.blit(texto_tesoura, (botao_tesoura.centerx - texto_tesoura.get_width()//2, botao_tesoura.centery - texto_tesoura.get_height()//2))

    pygame.display.flip()
    RELOGIO.tick(60)

pygame.quit()
sys.exit()