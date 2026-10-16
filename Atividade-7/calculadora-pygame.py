import pygame
import sys

pygame.init()
LARGURA, ALTURA = 400, 550
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Calculadora - Pygame")

RELOGIO = pygame.time.Clock()

BRANCO = (255, 255, 255)
PRETO = (30, 30, 30)
CINZA_FUNDO = (240, 240, 240)
CINZA_BOTAO = (220, 220, 220)
CINZA_HOVER = (200, 200, 200)
LARANJA = (255, 140, 0)
LARANJA_HOVER = (255, 165, 0)
CINZA_ESCURO = (100, 100, 100)

fonte_visor = pygame.font.SysFont("Courier New", 36, bold=True)
fonte_botoes = pygame.font.SysFont("Times New Roman", 24, bold=True)

memoria = None
operador_atual = None
buffer_entrada = ""
visor_texto = "0"

botoes = [
    ("7", 20, 180, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("8", 105, 180, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("9", 190, 180, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("/", 275, 180, 105, 60, LARANJA, LARANJA_HOVER),
    
    ("4", 20, 250, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("5", 105, 250, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("6", 190, 250, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("*", 275, 250, 105, 60, LARANJA, LARANJA_HOVER),
    
    ("1", 20, 320, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("2", 105, 320, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("3", 190, 320, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("-", 275, 320, 105, 60, LARANJA, LARANJA_HOVER),
    
    ("C", 20, 390, 75, 60, (220, 100, 100), (240, 120, 120)), 
    ("0", 105, 390, 75, 60, CINZA_BOTAO, CINZA_HOVER),
    ("=", 190, 390, 75, 60, (100, 180, 100), (120, 200, 120)), 
    ("+", 275, 390, 105, 60, LARANJA, LARANJA_HOVER),
]

def processar_calculo(proximo_valor):
    global memoria, operador_atual
    if memoria is None:
        return proximo_valor
    
    if operador_atual == '+':
        return memoria + proximo_valor
    elif operador_atual == '-':
        return memoria - proximo_valor
    elif operador_atual == '*':
        return memoria * proximo_valor
    elif operador_atual == '/':
        if proximo_valor == 0:
            return "Erro"
        return memoria / proximo_valor
    return proximo_valor

def tratar_clique(texto_botao):
    global memoria, operador_atual, buffer_entrada, visor_texto
    
    if texto_botao.isdigit():
        if buffer_entrada == "0" or buffer_entrada == "Erro":
            buffer_entrada = texto_botao
        else:
            buffer_entrada += texto_botao
        visor_texto = buffer_entrada
        
    elif texto_botao in ['+', '-', '*', '/']:
        if buffer_entrada != "":
            numero_atual = float(buffer_entrada)
            if memoria is None:
                memoria = numero_atual
            else:
                memoria = processar_calculo(numero_atual)
            
            if memoria == "Erro":
                visor_texto = "Erro"
                buffer_entrada = ""
                return

            if memoria.is_integer():
                visor_texto = str(int(memoria))
            else:
                visor_texto = str(memoria)
            buffer_entrada = ""
            
        elif memoria is not None:
            visor_texto = str(int(memoria)) if memoria.is_integer() else str(memoria)
            
        operador_atual = texto_botao

    elif texto_botao == '=':
        if operador_atual is not None and buffer_entrada != "":
            numero_atual = float(buffer_entrada)
            resultado = processar_calculo(numero_atual)
            
            if resultado == "Erro":
                visor_texto = "Erro"
            else:
                if isinstance(resultado, float) and resultado.is_integer():
                    resultado = int(resultado)
                visor_texto = str(resultado)
                memoria = float(resultado) 
            
            buffer_entrada = ""
            operador_atual = None

    elif texto_botao == 'C':
        memoria = None
        operador_atual = None
        buffer_entrada = ""
        visor_texto = "0"

rodando = True
while rodando:
    janela.fill(CINZA_FUNDO)
    mouse_pos = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for texto, x, y, largura, altura, _, _ in botoes:
                    ret_botao = pygame.Rect(x, y, largura, altura)
                    if ret_botao.collidepoint(evento.pos):
                        tratar_clique(texto)

    ret_visor = pygame.Rect(20, 20, 360, 130)
    pygame.draw.rect(janela, BRANCO, ret_visor, border_radius=8)
    pygame.draw.rect(janela, CINZA_ESCURO, ret_visor, 2, border_radius=8)

    surf_visor = fonte_visor.render(visor_texto, True, PRETO)
    janela.blit(surf_visor, (ret_visor.right - surf_visor.get_width() - 20, ret_visor.centery - surf_visor.get_height() // 2))

    for texto, x, y, largura, altura, cor_base, cor_hover in botoes:
        ret = pygame.Rect(x, y, largura, altura)
        cor_atual = cor_hover if ret.collidepoint(mouse_pos) else cor_base
        
        pygame.draw.rect(janela, cor_atual, ret, border_radius=6)
        pygame.draw.rect(janela, (150, 150, 150), ret, 1, border_radius=6)
        
        surf_btn = fonte_botoes.render(texto, True, BRANCO if cor_base != CINZA_BOTAO else PRETO)
        janela.blit(surf_btn, (ret.centerx - surf_btn.get_width() // 2, ret.centery - surf_btn.get_height() // 2))

    pygame.display.flip()
    RELOGIO.tick(60)

pygame.quit()
sys.exit()