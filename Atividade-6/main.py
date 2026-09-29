import pygame
import sys
import math
import os

# Determina o diretório base para carregar os arquivos sem erro de caminho
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    pygame.mixer.init()
except pygame.error:
    os.environ['SDL_AUDIODRIVER'] = 'dummy'
    pygame.mixer.init()

pygame.init()

LARGURA, ALTURA = 800, 600
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Casinha do Batman")

RELOGIO = pygame.time.Clock()

# Cores
COR_MANHA = (255, 170, 80)     # Laranja/Manhã
COR_TARDE = (147, 204, 252)    # Azul claro/Tarde
COR_NOITE = (20, 24, 60)       # Azul escuro/Noite

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

# Carregamento de Sons
try:
    pygame.mixer.music.load(os.path.join(BASE_DIR, "batman_1966.mp3"))
    pygame.mixer.music.play(-1)  
except pygame.error as e:
    print(f"Aviso: Música de fundo não encontrada: {e}")

def carregar_som(nome_arquivo):
    try:
        return pygame.mixer.Sound(os.path.join(BASE_DIR, nome_arquivo))
    except pygame.error:
        return None

som_manha = carregar_som("manha.mp3")
som_tarde = carregar_som("tarde.mp3")
som_noite = carregar_som("batman_1966.mp3")

# Carregamento do Batman
img_batman = None
caminho_batman = os.path.join(BASE_DIR, "batman.png")
if os.path.exists(caminho_batman):
    try:
        img_batman = pygame.image.load(caminho_batman).convert_alpha()
        img_batman = pygame.transform.scale(img_batman, (80, 120))
    except pygame.error as e:
        print(f"Aviso: Erro ao carregar imagem do Batman: {e}")

fonte_custom = pygame.font.SysFont("Times New Roman", 28, bold=True)
mensagem_clique = ""

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
    # Porcentagem de 0.0 (esquerda) a 1.0 (direita) para controlar o horário do dia
    porcentagem_dia = (sol_cx - raio_total_sol) / (LARGURA - 2 * raio_total_sol)
    porcentagem_dia = max(0.0, min(1.0, porcentagem_dia))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: 
                mouse_x, mouse_y = evento.pos
                
                # Exibe a frase e toca o som dependendo de onde o sol está
                if porcentagem_dia < 0.33:
                    mensagem_clique = "Bom dia"
                    if som_manha: som_manha.play()
                elif porcentagem_dia < 0.66:
                    mensagem_clique = "Boa tarde"
                    if som_tarde: som_tarde.play()
                else:
                    mensagem_clique = "I'm batman"
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

    # Animação da Nuvem
    nuvem_x += velocidade_nuvem
    if nuvem_x + 226 >= LARGURA:
        nuvem_x = LARGURA - 226
        velocidade_nuvem = -abs(velocidade_nuvem) 
    elif nuvem_x + 2 <= 0:
        nuvem_x = -2
        velocidade_nuvem = abs(velocidade_nuvem)  

    # Transição suave: 0.0 a 0.5 (Manhã -> Tarde) e 0.5 a 1.0 (Tarde -> Noite)
    if porcentagem_dia < 0.5:
        t = porcentagem_dia / 0.5
        cor_ceu_atual = interpolar_cor(COR_MANHA, COR_TARDE, t)
    else:
        t = (porcentagem_dia - 0.5) / 0.5
        cor_ceu_atual = interpolar_cor(COR_TARDE, COR_NOITE, t)

    janela.fill(cor_ceu_atual) 

    # Desenho do Sol e seus Raios
    pygame.draw.circle(janela, COR_SOL, (sol_cx, sol_cy), raio_sol) 
    num_raios = 8
    for i in range(num_raios):
        angulo = i * (2 * math.pi / num_raios)
        x1 = sol_cx + math.cos(angulo) * (raio_sol + distancia_inicio)
        y1 = sol_cy + math.sin(angulo) * (raio_sol + distancia_inicio)
        x2 = sol_cx + math.cos(angulo) * (raio_sol + distancia_inicio + comprimento_raio)
        y2 = sol_cy + math.sin(angulo) * (raio_sol + distancia_inicio + comprimento_raio)
        pygame.draw.line(janela, COR_SOL, (int(x1), int(y1)), (int(x2), int(y2)), 6) 

    # Gramado
    pygame.draw.rect(janela, COR_GRAMA, (0, 485, LARGURA, 115)) 

    # Nuvem
    pygame.draw.circle(janela, COR_NUVEM, (nuvem_x + 40, nuvem_y), 38) 
    pygame.draw.circle(janela, COR_NUVEM, (nuvem_x + 90, nuvem_y - 8), 42) 
    pygame.draw.circle(janela, COR_NUVEM, (nuvem_x + 140, nuvem_y - 4), 40) 
    pygame.draw.circle(janela, COR_NUVEM, (nuvem_x + 190, nuvem_y), 36) 

    # Árvore
    pygame.draw.rect(janela, COR_ARVORE_TRONCO, (580, 410, 50, 110))  
    pygame.draw.circle(janela, COR_ARVORE_FOLHAS, (605, 345), 75)      

    # Casa
    pygame.draw.rect(janela, COR_PAREDE, (203, 325, 195, 160)) 
    pygame.draw.polygon(janela, COR_TELHADO, [(203, 325), (300, 205), (398, 325)]) 
    pygame.draw.rect(janela, COR_JANELA, (222, 392, 50, 55)) 
    pygame.draw.rect(janela, COR_PORTA, (300, 375, 50, 110)) 
    pygame.draw.circle(janela, COR_MACANETA, (310, 432), 4) 

    # Desenhar o Batman próximo à casa
    if img_batman:
        janela.blit(img_batman, (410, 370))

    # Exibição do Texto no topo ao clicar
    if mensagem_clique:
        cor_fonte = (255, 255, 255) if sum(cor_ceu_atual) < 300 else COR_TEXTO
        texto_surface = fonte_custom.render(mensagem_clique, True, cor_fonte)
        janela.blit(texto_surface, (20, 20))  

    pygame.display.flip()
    RELOGIO.tick(60)

pygame.quit()
sys.exit()