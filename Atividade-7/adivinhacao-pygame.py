import pygame
import sys
import random

pygame.init()
LARGURA, ALTURA = 800, 600
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Adivinhação - Pygame")

RELOGIO = pygame.time.Clock()

BRANCO = (255, 255, 255)
PRETO = (30, 30, 30)
AZUL_FUNDO = (235, 242, 250)
AZUL_BOTAO = (70, 130, 180)
AZUL_HOVER = (100, 149, 237)
VERDE = (46, 139, 87)
VERMELHO = (178, 34, 34)
CINZA = (210, 210, 210)

fonte_titulo = pygame.font.SysFont("Times New Roman", 32, bold=True)
fonte_texto = pygame.font.SysFont("Times New Roman", 22, bold=True)
fonte_pequena = pygame.font.SysFont("Times New Roman", 18, bold=True)

estado_atual = "menu"

numero_secreto = 0
tentativas = 0
mensagem_dica = "Digite um número entre 1 e 1023 e aperte ENTER."
entrada_usuario = ""
jogo_acabou = False

limite_inferior = 1
limite_superior = 1023
palpite_pc = 0

def iniciar_modo_usuario():
    global numero_secreto, tentativas, mensagem_dica, entrada_usuario, jogo_acabou, estado_atual
    numero_secreto = random.randint(1, 1023)
    tentativas = 0
    mensagem_dica = "Computador escolheu! Tente adivinhar (1 a 1023)."
    entrada_usuario = ""
    jogo_acabou = False
    estado_atual = "usuario_joga"

def iniciar_modo_pc():
    global limite_inferior, limite_superior, palpite_pc, tentativas, mensagem_dica, jogo_acabou, estado_atual
    limite_inferior = 1
    limite_superior = 1023
    tentativas = 0
    palpite_pc = (limite_inferior + limite_superior) // 2
    mensagem_dica = f"Pense em um número. O PC chuta: {palpite_pc}"
    jogo_acabou = False
    estado_atual = "pc_joga"

btn_modo1 = pygame.Rect(250, 220, 300, 60)
btn_modo2 = pygame.Rect(250, 310, 300, 60)

btn_menos1 = pygame.Rect(180, 400, 120, 50)
btn_zero = pygame.Rect(340, 400, 120, 50)
btn_mais1 = pygame.Rect(500, 400, 120, 50)

btn_voltar = pygame.Rect(300, 500, 200, 45)

rodando = True
while rodando:
    janela.fill(AZUL_FUNDO)
    mouse_pos = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if estado_atual == "menu":
                    if btn_modo1.collidepoint(evento.pos):
                        iniciar_modo_usuario()
                    elif btn_modo2.collidepoint(evento.pos):
                        iniciar_modo_pc()
                
                elif estado_atual == "usuario_joga" and jogo_acabou:
                    if btn_voltar.collidepoint(evento.pos):
                        estado_atual = "menu"

                elif estado_atual == "pc_joga":
                    if not jogo_acabou:
                        if btn_menos1.collidepoint(evento.pos):
                            
                            if limite_inferior <= palpite_pc - 1:
                                limite_superior = palpite_pc - 1
                                tentativas += 1
                                palpite_pc = (limite_inferior + limite_superior) // 2
                                mensagem_dica = f"O PC chuta: {palpite_pc} (Tentativas: {tentativas})"
                        elif btn_mais1.collidepoint(evento.pos):
                            
                            if palpite_pc + 1 <= limite_superior:
                                limite_inferior = palpite_pc + 1
                                tentativas += 1
                                palpite_pc = (limite_inferior + limite_superior) // 2
                                mensagem_dica = f"O PC chuta: {palpite_pc} (Tentativas: {tentativas})"
                        elif btn_zero.collidepoint(evento.pos):
                            
                            tentativas += 1
                            jogo_acabou = True
                            mensagem_dica = f"0 (O PC acertou em {tentativas} tentativas!)"
                    elif jogo_acabou and btn_voltar.collidepoint(evento.pos):
                        estado_atual = "menu"

        if evento.type == pygame.KEYDOWN and estado_atual == "usuario_joga" and not jogo_acabou:
            if evento.key == pygame.K_RETURN:
                if entrada_usuario.isdigit():
                    chute = int(entrada_usuario)
                    tentativas += 1
                    if numero_secreto < chute:
                        mensagem_dica = f"-1 (O número é MENOR que {chute})"
                    elif numero_secreto > chute:
                        mensagem_dica = f"1 (O número é MAIOR que {chute})"
                    else:
                        mensagem_dica = f"0 (ACERTOU! Feito em {tentativas} tentativas)"
                        jogo_acabou = True
                    entrada_usuario = ""
            elif evento.key == pygame.K_BACKSPACE:
                entrada_usuario = entrada_usuario[:-1]
            else:
                if evento.unicode.isdigit():
                    entrada_usuario += evento.unicode
    
    if estado_atual == "menu":
        surf_titulo = fonte_titulo.render("JOGO DE ADIVINHAÇÃO (1 a 1023)", True, PRETO)
        janela.blit(surf_titulo, (LARGURA // 2 - surf_titulo.get_width() // 2, 100))

        cor_m1 = AZUL_HOVER if btn_modo1.collidepoint(mouse_pos) else AZUL_BOTAO
        pygame.draw.rect(janela, cor_m1, btn_modo1, border_radius=8)
        t1 = fonte_texto.render("1. Você Adivinha", True, BRANCO)
        janela.blit(t1, (btn_modo1.centerx - t1.get_width()//2, btn_modo1.centery - t1.get_height()//2))

        cor_m2 = AZUL_HOVER if btn_modo2.collidepoint(mouse_pos) else AZUL_BOTAO
        pygame.draw.rect(janela, cor_m2, btn_modo2, border_radius=8)
        t2 = fonte_texto.render("2. O Computador Adivinha", True, BRANCO)
        janela.blit(t2, (btn_modo2.centerx - t2.get_width()//2, btn_modo2.centery - t2.get_height()//2))

    elif estado_atual == "usuario_joga":
        surf_titulo = fonte_titulo.render("MODO: Você Adivinha", True, PRETO)
        janela.blit(surf_titulo, (LARGURA // 2 - surf_titulo.get_width() // 2, 60))

        surf_tentativas = fonte_texto.render(f"Tentativas: {tentativas}", True, PRETO)
        janela.blit(surf_tentativas, (100, 140))

        surf_dica = fonte_texto.render(mensagem_dica, True, VERMELHO if not jogo_acabou else VERDE)
        janela.blit(surf_dica, (100, 200))

        if not jogo_acabou:
            surf_instrucao = fonte_pequena.render("Digite seu palpite e aperte ENTER:", True, PRETO)
            janela.blit(surf_instrucao, (100, 280))
            
            ret_caixa = pygame.Rect(100, 310, 250, 50)
            pygame.draw.rect(janela, BRANCO, ret_caixa, border_radius=5)
            pygame.draw.rect(janela, PRETO, ret_caixa, 2, border_radius=5)
            surf_entrada = fonte_titulo.render(entrada_usuario, True, PRETO)
            janela.blit(surf_entrada, (ret_caixa.x + 10, ret_caixa.centery - surf_entrada.get_height()//2))
        else:
            
            cor_v = AZUL_HOVER if btn_voltar.collidepoint(mouse_pos) else AZUL_BOTAO
            pygame.draw.rect(janela, cor_v, btn_voltar, border_radius=8)
            tv = fonte_texto.render("Menu Principal", True, BRANCO)
            janela.blit(tv, (btn_voltar.centerx - tv.get_width()//2, btn_voltar.centery - tv.get_height()//2))

    elif estado_atual == "pc_joga":
        surf_titulo = fonte_titulo.render("MODO: Computador Adivinha", True, PRETO)
        janela.blit(surf_titulo, (LARGURA // 2 - surf_titulo.get_width() // 2, 60))

        surf_dica = fonte_texto.render(mensagem_dica, True, VERDE if jogo_acabou else PRETO)
        janela.blit(surf_dica, (100, 180))

        if not jogo_acabou:
            surf_guia = fonte_pequena.render("Responda ao palpite do computador:", True, PRETO)
            janela.blit(surf_guia, (100, 280))

            for rect, texto, cor in [(btn_menos1, "-1 (Menor)", VERMELHO), (btn_zero, "0 (Acertou)", VERDE), (btn_mais1, "1 (Maior)", AZUL_BOTAO)]:
                cor_atual = AZUL_HOVER if rect.collidepoint(mouse_pos) else cor
                pygame.draw.rect(janela, cor_atual, rect, border_radius=8)
                t_btn = fonte_pequena.render(texto, True, BRANCO)
                janela.blit(t_btn, (rect.centerx - t_btn.get_width()//2, rect.centery - t_btn.get_height()//2))
        else:
            cor_v = AZUL_HOVER if btn_voltar.collidepoint(mouse_pos) else AZUL_BOTAO
            pygame.draw.rect(janela, cor_v, btn_voltar, border_radius=8)
            tv = fonte_texto.render("Menu Principal", True, BRANCO)
            janela.blit(tv, (btn_voltar.centerx - tv.get_width()//2, btn_voltar.centery - tv.get_height()//2))

    pygame.display.flip()
    RELOGIO.tick(60)

pygame.quit()
sys.exit()