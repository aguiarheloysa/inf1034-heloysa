import pygame, sys

# 1. Inicialização do Pygame e Áudio
pygame.init()
pygame.mixer.init()

# Configuração da Janela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Casinha em Pygame")

# Cores (RGB)
CEU = (135, 206, 235)
GRAMA = (34, 139, 34)
CASA_PAREDE = (222, 184, 135)
CASA_TELHADO = (178, 34, 34)
PORTA = (101, 67, 33)
JANELA = (255, 255, 255)
JANELA_MARCO = (0, 0, 0)
SOL = (255, 223, 0)
NUVEM = (240, 248, 255)
TEXTO_COR = (20, 20, 20)

# 2. Carregar Fontes, Imagens e Áudio (COM REQUISITOS DO PRINCIPAL)
# Texto com fonte customizada (50XP)
try:
    fonte = pygame.font.Font("fonte_custom.ttf", 32)
except FileNotFoundError:
    # Fallback caso a fonte não exista na pasta
    fonte = pygame.font.SysFont("arial", 32)

texto_surface = fonte.render("Minha Casinha no Pygame", True, TEXTO_COR)

# Imagem para o cenário (50XP)
try:
    imagem_cenario = pygame.image.load("arvore.png").convert_alpha()
    imagem_cenario = pygame.transform.scale(imagem_cenario, (120, 150))
except FileNotFoundError:
    imagem_cenario = None

# Áudio de fundo em loop (50XP)
try:
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(-1)  # -1 faz o áudio tocar infinitamente
except pygame.error:
    pass

# Variáveis do EXTRA (Nuvem em movimento)
nuvem_x = -150
nuvem_y = 60
velocidade_nuvem = 2

clock = pygame.time.Clock()

# Loop Principal
rodando = True
while rodando:
    # Tratamento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # ----------------------------------------------------
    # LÓGICA / ATUALIZAÇÃO DE ESTADO
    # ----------------------------------------------------
    # EXTRA: Fazer a nuvem se mexer para a direita infinitamente (100XP)
    nuvem_x += velocidade_nuvem

    # EXTRA: Teleportar para a esquerda ao passar do limite da tela (100XP)
    if nuvem_x > LARGURA:
        nuvem_x = -150

    # ----------------------------------------------------
    # DESENHO / RENDERIZAÇÃO
    # ----------------------------------------------------
    # Fundo (Céu)
    tela.fill(CEU)

    # Chão (Grama)
    pygame.draw.rect(tela, GRAMA, (0, 400, LARGURA, 200))

    # Sol
    pygame.draw.circle(tela, SOL, (700, 90), 50)

    # Replicar a imagem da casinha com primitivas geométricas (350XP)
    # Corpo da casa
    pygame.draw.rect(tela, CASA_PAREDE, (300, 250, 200, 180))
    # Telhado (Triângulo)
    pygame.draw.polygon(tela, CASA_TELHADO, [(280, 250), (400, 150), (520, 250)])
    # Porta
    pygame.draw.rect(tela, PORTA, (340, 330, 45, 100))
    # Maçaneta
    pygame.draw.circle(tela, SOL, (378, 380), 4)
    # Janela
    pygame.draw.rect(tela, JANELA, (420, 290, 50, 50))
    pygame.draw.rect(tela, JANELA_MARCO, (420, 290, 50, 50), 2)
    pygame.draw.line(tela, JANELA_MARCO, (445, 290), (445, 340), 2)
    pygame.draw.line(tela, JANELA_MARCO, (420, 315), (470, 315), 2)

    # Nuvem em Movimento (Formada por círculos / primitivas)
    pygame.draw.circle(tela, NUVEM, (nuvem_x + 30, nuvem_y + 20), 25)
    pygame.draw.circle(tela, NUVEM, (nuvem_x + 50, nuvem_y + 10), 30)
    pygame.draw.circle(tela, NUVEM, (nuvem_x + 70, nuvem_y + 20), 25)
    pygame.draw.rect(tela, NUVEM, (nuvem_x + 30, nuvem_y + 15, 40, 20))

    # Desenhar Imagem Carregada (50XP)
    if imagem_cenario:
        tela.blit(imagem_cenario, (150, 280))

    # Desenhar Texto Customizado (50XP)
    tela.blit(texto_surface, (20, 20))

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()