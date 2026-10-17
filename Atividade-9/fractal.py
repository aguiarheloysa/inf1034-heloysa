import pygame
import math
import sys

pygame.init()
LARGURA, ALTURA = 900, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Trabalho de Desenhos Recursivos e Fractais")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (30, 144, 255)
VERDE = (34, 139, 34)
VERMELHO = (220, 20, 60)
ROXO = (138, 43, 226)

FONTE = pygame.font.SysFont("arial", 20)

def desenhar_linha_base(superficie, cor, p1, p2, espessura=1):
    pygame.draw.line(superficie, cor, p1, p2, espessura)

def desenhar_recursivo_facil(superficie, x, y, tamanho, nivel):
    
    if nivel == 0 or tamanho < 4:
        return
    
    x1, y1 = x - tamanho / 2, y
    x2, y2 = x + tamanho / 2, y
    desenhar_linha_base(superficie, AZUL, (x1, y1), (x2, y2), 2)
    
    desenhar_recursivo_facil(superficie, x1, y1, tamanho / 2, nivel - 1)
    desenhar_recursivo_facil(superficie, x2, y2, tamanho / 2, nivel - 1)

def desenhar_koch_segmento(superficie, p1, p2, nivel, cor):
    
    if nivel == 0:
        desenhar_linha_base(superficie, cor, p1, p2, 1)
        return
    
    x1, y1 = p1
    x2, y2 = p2
    
    dx = x2 - x1
    dy = y2 - y1
    
    p3 = (x1 + dx / 3, y1 + dy / 3)
    p4 = (x2 - dx / 3, y2 - dy / 3)
    
    angulo = math.radians(60)
    
    x_pico = p3[0] + (p4[0] - p3[0]) * math.cos(angulo) - (p4[1] - p3[1]) * math.sin(angulo)
    y_pico = p3[1] + (p4[0] - p3[0]) * math.sin(angulo) + (p4[1] - p3[1]) * math.cos(angulo)
    p_topo = (x_pico, y_pico)
    
    desenhar_koch_segmento(superficie, p1, p3, nivel - 1, cor)
    desenhar_koch_segmento(superficie, p3, p_topo, nivel - 1, cor)
    desenhar_koch_segmento(superficie, p_topo, p4, nivel - 1, cor)
    desenhar_koch_segmento(superficie, p4, p2, nivel - 1, cor)

def desenhar_arvore_3_ramos(superficie, x, y, comprimento, angulo, nivel, fator_escala):
    if nivel == 0 or comprimento < 4:
        return
    
    rad = math.radians(angulo)
    x_fim = x + comprimento * math.sin(rad)
    y_fim = y - comprimento * math.cos(rad)
    
    espessura = max(1, int(nivel * 1.2))
    cor_galho = VERDE if nivel < 3 else PRETO
    
    desenhar_linha_base(superficie, cor_galho, (x, y), (x_fim, y_fim), espessura)
    
    novo_comprimento = comprimento * fator_escala
    
    desenhar_arvore_3_ramos(superficie, x_fim, y_fim, novo_comprimento, angulo - 25, nivel - 1, fator_escala)
    desenhar_arvore_3_ramos(superficie, x_fim, y_fim, novo_comprimento, angulo, nivel - 1, fator_escala)
    desenhar_arvore_3_ramos(superficie, x_fim, y_fim, novo_comprimento, angulo + 25, nivel - 1, fator_escala)

class Slider:
    def __init__(self, x, y, w, h, min_val, max_val, val_inicial, texto):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.val = val_inicial
        self.texto = texto
        self.arrastando = False

    def desenhar(self, superficie):
        pygame.draw.rect(superficie, (180, 180, 180), self.rect, border_radius=4)
        
        pos_x = self.rect.x + (self.val - self.min_val) / (self.max_val - self.min_val) * self.rect.w
        botao_rect = pygame.Rect(pos_x - 6, self.rect.y - 4, 12, self.rect.h + 8)
        pygame.draw.rect(superficie, AZUL, botao_rect, border_radius=4)
        
        txt_surface = FONTE.render(f"{self.texto}: {self.val:.2f}", True, PRETO)
        superficie.blit(txt_surface, (self.rect.x, self.rect.y - 25))

    def atualizar(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos) or pygame.Rect(self.rect.x - 6, self.rect.y - 4, self.rect.w + 12, self.rect.h + 8).collidepoint(evento.pos):
                self.arrastando = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            self.arrastando = False
        elif evento.type == pygame.MOUSEMOTION and self.arrastando:
            rel_x = max(self.rect.x, min(evento.pos[0], self.rect.x + self.rect.w))
            percentual = (rel_x - self.rect.x) / self.rect.w
            self.val = self.min_val + percentual * (self.max_val - self.min_val)


def executar_fractais():
    relogio = pygame.time.Clock()
    modo_desenho = 3  
    
    slider_escala = Slider(50, 630, 300, 10, 0.5, 0.8, 0.67, "Fator de Escala da Árvore")

    while True:
        TELA.fill(BRANCO)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    modo_desenho = 1
                elif evento.key == pygame.K_2:
                    modo_desenho = 2
                elif evento.key == pygame.K_3:
                    modo_desenho = 3
                elif evento.key == pygame.K_ESCAPE:
                    return 
            
            slider_escala.atualizar(evento)
            
        instrucoes = FONTE.render("[1] Fácil | [2] Médio (Koch) | [3] Difícil (Árvore 3 Ramos) | [ESC] Voltar", True, PRETO)
        TELA.blit(instrucoes, (50, 20))
        
        if modo_desenho == 1:
            titulo = FONTE.render("Desenho Recursivo Fácil (H-Tree)", True, AZUL)
            TELA.blit(titulo, (50, 60))
            desenhar_recursivo_facil(TELA, LARGURA // 2, ALTURA // 2, 250, 4)
            
        elif modo_desenho == 2:
            titulo = FONTE.render("Desenho Recursivo Médio (Floco de Neve de Koch)", True, VERDE)
            TELA.blit(titulo, (50, 60))
            p1 = (300, 480)
            p2 = (600, 480)
            p3 = (450, 220)
            desenhar_koch_segmento(TELA, p1, p2, 3, VERDE)
            desenhar_koch_segmento(TELA, p2, p3, 3, VERDE)
            desenhar_koch_segmento(TELA, p3, p1, 3, VERDE)
            
        elif modo_desenho == 3:
            titulo = FONTE.render("Desenho Recursivo Difícil (Árvore com 3 Ramos + Slider Extra)", True, ROXO)
            TELA.blit(titulo, (50, 60))
            desenhar_arvore_3_ramos(TELA, LARGURA // 2, 580, 140, 0, 7, slider_escala.val)
            slider_escala.desenhar(TELA)
            
        pygame.display.flip()
        relogio.tick(30)

if __name__ == "__main__":
    executar_fractais()