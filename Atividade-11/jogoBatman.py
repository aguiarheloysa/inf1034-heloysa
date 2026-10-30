import pygame, sys
from pygame.locals import QUIT

pygame.init()

def carregar_mapa(caminho):
    mapa = []
    try:
        with open(caminho, 'r') as arquivo:
            for linha in arquivo:
                mapa.append(linha.strip())
        return mapa
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho} não foi encontrado.")
        pygame.quit()
        sys.exit()

mapa_joguinho = carregar_mapa("Atividade-11/mapa.txt")

tile_size = 64
pos_x = 100
pos_y = 100
velocidade_y = 0
gravidade = 0.5       
forca_pulo = -10    
no_chao = False
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Batman")

batman = pygame.image.load("Atividade-11/batman.png")
batman = pygame.transform.scale(batman, (64, 64))

background_img = pygame.image.load("Atividade-11/joguinho.jpg")
background_img = pygame.transform.scale(background_img, (2000, 600))

propriedades_tiles = {
    "X": {"solido": False},
    "A": {"solido": False},
    "G": {"solido": True},
    "T": {"solido": True},
    "P": {"solido": True},
    "B": {"solido": True},
    "E": {"solido": True},
    "C": {"solido": True}
}

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    clock.tick(60)
    dt = clock.get_time()

    old_pos_x = pos_x
    old_pos_y = pos_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        pos_x = pos_x + 0.2 * dt
    elif keys[pygame.K_LEFT]:
        pos_x = pos_x - 0.2 * dt

    if keys[pygame.K_UP] and no_chao:
        velocidade_y = forca_pulo
        no_chao = False

    velocidade_y += gravidade * (dt / 16)
    pos_y += velocidade_y

    camera_x = pos_x - 300
    if camera_x < 0:
        camera_x = 0

    screen.blit(background_img, (-camera_x, 0))

    collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64)

    no_chao = False

    for i in range(len(mapa_joguinho)):
        for j in range(len(mapa_joguinho[i])):
            letra = mapa_joguinho[i][j]
            
            if letra in propriedades_tiles and propriedades_tiles[letra]["solido"]:
                bloco_rect = pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size)
                
                if collider_jogador.colliderect(bloco_rect):
                    if velocidade_y > 0:
                        pos_y = bloco_rect.top - 64
                        velocidade_y = 0
                        no_chao = True
                    elif velocidade_y < 0:
                        pos_y = bloco_rect.bottom
                        velocidade_y = 0
                    
                    collider_jogador.y = pos_y

    screen.blit(batman, (pos_x - camera_x, pos_y))

    pygame.display.update()