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
pygame.display.set_caption("Atividade 5 - Réplica da Casinha")

RELOGIO = pygame.time.Clock()




COR_CEU = (147, 204, 252)       
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
    print(f"Não foi possível carregar o áudio: {e}")

fonte_custom = pygame.font.SysFont("Times New Romans", 24, bold=True)
texto_surface = fonte_custom.render("Casinha famosa", True, COR_TEXTO)


nuvem_x = -250  
nuvem_y = 110
velocidade_nuvem = 1


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    
    nuvem_x += velocidade_nuvem
    if nuvem_x > LARGURA:
        nuvem_x = -260  

    
    janela.fill(COR_CEU) 
    pygame.draw.rect(janela, COR_GRAMA, (0, 485, LARGURA, 115)) 

    
    sol_cx, sol_cy = 120, 130
    raio_sol = 45
    pygame.draw.circle(janela, COR_SOL, (sol_cx, sol_cy), raio_sol) 
    
    
    num_raios = 8
    comprimento_raio = 30
    distancia_inicio = 12
    for i in range(num_raios):
        angulo = i * (2 * math.pi / num_raios)
        x1 = sol_cx + math.cos(angulo) * (raio_sol + distancia_inicio)
        y1 = sol_cy + math.sin(angulo) * (raio_sol + distancia_inicio)
        x2 = sol_cx + math.cos(angulo) * (raio_sol + distancia_inicio + comprimento_raio)
        y2 = sol_cy + math.sin(angulo) * (raio_sol + distancia_inicio + comprimento_raio)
        pygame.draw.line(janela, COR_SOL, (int(x1), int(y1)), (int(x2), int(y2)), 6) 

    
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

    
    janela.blit(texto_surface, (20, 20))  

    pygame.display.flip()
    RELOGIO.tick(60)

pygame.quit()
sys.exit()