import pygame
import sys
import math
import os

try:
    pygame.mixer.init()
except pygame.error:
    os.environ['SDL_AUDIODRIVER'] = 'dummy'
    pygame.mixer.init()

pygame.init()

LARGURA, ALTURA = 800, 600
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("I'm Batman!")

RELOGIO = pygame.time.Clock()


COR_MANHA = (255, 170, 80)      
COR_TARDE = (147, 204, 252)     
COR_NOITE = (20, 24, 60)       

COR_GRAMA = (66, 142, 34)       
COR_TELHADO = (235, 128, 48)    
COR_PAREDE = (109, 110, 114)    
COR_JANELA = (10, 24, 105)      
COR_PORTA = (135, 83, 31)       
COR_MACANETA = (0, 0, 0)        
COR_SOL = (252, 238, 77)        
COR_ARVORE_FOLHAS = (49, 138, 25) 
COR_ARVORE_TRONCO = (117, 72, 24) 
COR_NUVEM = (255, 255, 255)     
COR_TEXTO = (20, 20, 20)        


try:
    pygame.mixer.music.load("batman_1966.mp3")
    pygame.mixer.music.play(-1)  
except pygame.error as e:
    print(f"Aviso: Música de fundo não encontrada: {e}")

def carregar_som(nome_arquivo):
    try:
        return pygame.mixer.Sound(nome_arquivo)
    except pygame.error:
        return None


som_manha = carregar_som("")
som_tarde = carregar_som("")
som_noite = carregar_som("")

fonte_custom = pygame.font.SysFont("Times New Romans", 24, bold=True)
texto_surface = fonte_custom.render("Casinha famosa", True, COR_TEXTO)


nuvem_x = 50  
nuvem_y = 110
velocidade_nuvem = 3


sol_cx, sol_cy = 120, 130
raio_sol = 45
comprimento_raio = 30
distancia_inicio = 12
raio_total_sol = raio_sol + distancia_inicio + comprimento_raio 
arrastando_sol = False
velocidade_sol = 5


def interpolar_cor(cor1, cor2, t):
    """Mistura duas cores com base em t (0.0 a 1.0)"""
    r = int(cor1[0] + (cor2[0] - cor1[0]) * t)
    g = int(cor1[1] + (cor2[1] - cor1[1]) * t)
    b = int(cor1[2] + (cor2[2] - cor1[2]) * t)
    return (r, g, b)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: 
                mouse_x, mouse_y = evento.pos
                
                porcentagem_dia = (sol_cx - raio_total_sol) / (LARGURA - 2 * raio_total_sol)
                if porcentagem_dia < 0.33:
                    print("Som da Manhã!")
                    if som_manha: som_manha.play()
                elif porcentagem_dia < 0.66:
                    print("Som da Tarde!")
                    if som_tarde: som_tarde.play()
                else:
                    print("Som da Noite!")
                    if som_noite: som_noite.play()

                
                distancia = math.hypot(mouse_x - sol_cx, mouse_y - sol_cy)
                if distancia <= raio_total_sol:
                    arrastando_sol = True

        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                arrastando_sol = False
                
        if evento.type == pygame.MOUSEMOTION:
            if arrastando_sol:
                sol_cx, sol_cy = evento.pos

    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  sol_cx -= velocidade_sol
    if teclas[pygame.K_RIGHT]: sol_cx += velocidade_sol
    if teclas[pygame.K_UP]:    sol_cy -= velocidade_sol
    if teclas[pygame.K_DOWN]:  sol_cy += velocidade_sol

    
    sol_cx = max(raio_total_sol, min(sol_cx, LARGURA - raio_total_sol))
    sol_cy = max(raio_total_sol, min(sol_cy, ALTURA - raio_total_sol))

    
    nuvem_x += velocidade_nuvem
    
    
    limite_esq_nuvem = nuvem_x + 2
    limite_dir_nuvem = nuvem_x + 226
    
    if limite_dir_nuvem >= LARGURA:
        nuvem_x = LARGURA - 226
        velocidade_nuvem = -abs(velocidade_nuvem) 
    elif limite_esq_nuvem <= 0:
        nuvem_x = -2
        velocidade_nuvem = abs(velocidade_nuvem)  

    
    porcentagem_x = (sol_cx - raio_total_sol) / (LARGURA - 2 * raio_total_sol) 
    
    if porcentagem_x < 0.5:
        
        t = porcentagem_x / 0.5
        cor_ceu_atual = interpolar_cor(COR_MANHA, COR_TARDE, t)
    else:
        
        t = (porcentagem_x - 0.5) / 0.5
        cor_ceu_atual = interpolar_cor(COR_TARDE, COR_NOITE, t)

    janela.fill(cor_ceu_atual) 

    pygame.draw.circle(janela, COR_SOL, (sol_cx, sol_cy), raio_sol) 
    num_raios = 8
    for i in range(num_raios):
        angulo = i * (2 * math.pi / num_raios)
        x1 = sol_cx + math.cos(angulo) * (raio_sol + distancia_inicio)
        y1 = sol_cy + math.sin(angulo) * (raio_sol + distancia_inicio)
        x2 = sol_cx + math.cos(angulo) * (raio_sol + distancia_inicio + comprimento_raio)
        y2 = sol_cy + math.sin(angulo) * (raio_sol + distancia_inicio + comprimento_raio)
        pygame.draw.line(janela, COR_SOL, (int(x1), int(y1)), (int(x2), int(y2)), 6) 

    
    pygame.draw.rect(janela, COR_GRAMA, (0, 485, LARGURA, 115)) 

    pygame.draw.circle(janela, COR_NUVEM, (nuvem_x + 40, nuvem_y), 38) 
    pygame.draw.circle(janela, COR_NUVEM, (nuvem_x + 90, nuvem_y - 8), 42) 
    pygame.draw.circle(janela, COR_NUVEM, (nuvem_x + 140, nuvem_y - 4), 40) 
    pygame.draw.circle(janela, COR_NUVEM, (nuvem_x + 190, nuvem_y), 36) 

    
    pygame.draw.rect(janela, COR_ARVORE_TRONCO, (580, 410, 50, 110))  
    pygame.draw.circle(janela, COR_ARVORE_FOLHAS, (605, 345), 75)       

    
    pygame.draw.rect(janela, COR_PAREDE, (203, 325, 195, 160)) 
    pygame.draw.polygon(janela, COR_TELHADO, [(203, 325), (300, 205), (398, 325)]) 
    pygame.draw.rect(janela, COR_JANELA, (222, 392, 50, 55)) 
    pygame.draw.rect(janela, COR_PORTA, (300, 375, 50, 110)) 
    pygame.draw.circle(janela, COR_MACANETA, (310, 432), 4) 

    
    if cor_ceu_atual[0] + cor_ceu_atual[1] + cor_ceu_atual[2] < 250: 
        texto_surface = fonte_custom.render("Casinha famosa", True, (240, 240, 240))
    else:
        texto_surface = fonte_custom.render("Casinha famosa", True, COR_TEXTO)
        
    janela.blit(texto_surface, (20, 20))  

    pygame.display.flip()
    RELOGIO.tick(60)

pygame.quit()
sys.exit()