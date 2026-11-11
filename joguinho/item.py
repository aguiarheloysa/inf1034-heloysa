import sys
import pygame

pygame.init()
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
imagem_fundo = pygame.image.load('assets/gotham.webp').convert_alpha()
img_fundo = pygame.transform.scale(imagem_fundo, (800, 600))
img_fundo.set_alpha(90)
pygame.display.set_caption("Batman 2D - Batman vs Coringa")

relogio = pygame.time.Clock()
FPS = 60

BRANCO = (255, 255, 255)
AZUL_ESCURO = (20, 20, 40)
VERMELHO = (220, 20, 60)
AMARELO = (255, 215, 0)
VERDE = (50, 205, 50)
ROXO = (128, 0, 128)

class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidade_x, cor=(255, 255, 255)):
        super().__init__()
        self.image = pygame.Surface((12, 6))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_x = velocidade_x

    def update(self):
        self.rect.x += self.velocidade_x
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
    

class Batman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/batman.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 65))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.velocidade_x = 5
        self.velocidade_y = 0
        self.gravidade = 0.8
        self.forca_pulo = -15
        self.no_chao = False
        self.vida = 100

    def update(self, teclas):
        movimento_x = 0
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            movimento_x = -self.velocidade_x
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            movimento_x = self.velocidade_x
        self.rect.x += movimento_x

        if self.rect.left < 0: 
            self.rect.left = 0
        if self.rect.right > LARGURA: 
            self.rect.right = LARGURA

        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y

        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.velocidade_y = 0
            self.no_chao = True

    def pular(self):
        if self.no_chao:
            self.velocidade_y = self.forca_pulo
            self.no_chao = False

    def atirar(self, grupo_projeteis):
        projetil = Projetil(self.rect.right, self.rect.y + 20, 10)
        grupo_projeteis.add(projetil)

class Coringa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/coringa.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 65))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direcao = 1
        self.tempo_tiro = 0

    def update(self, grupo_projeteis_coringa):
        self.rect.x += 2 * self.direcao
        if self.rect.x > 700 or self.rect.x < 500:
            self.direcao *= -1

        self.tempo_tiro += 1
        if self.tempo_tiro >= 90:
            self.atirar(grupo_projeteis_coringa)
            self.tempo_tiro = 0

    def atirar(self, grupo_projeteis_coringa):
        faca = Projetil(self.rect.left, self.rect.y + 20, -7, (255, 255, 255))
        grupo_projeteis_coringa.add(faca)

batman = Batman(100, 400)
coringa = Coringa(600, 440)

grupo_batman = pygame.sprite.GroupSingle(batman)
grupo_coringa = pygame.sprite.GroupSingle(coringa)
projeteis_batman = pygame.sprite.Group()
projeteis_coringa = pygame.sprite.Group()

fonte = pygame.font.SysFont(None, 24)
rodando = True
while rodando:
    relogio.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                batman.pular()
            if evento.key == pygame.K_f:  
                batman.atirar(projeteis_batman)

    teclas = pygame.key.get_pressed()

    grupo_batman.update(teclas)
    grupo_coringa.update(projeteis_coringa)
    projeteis_batman.update()
    projeteis_coringa.update()

    if pygame.sprite.spritecollide(batman, projeteis_coringa, True):
        batman.vida -= 20
        print(f"Batman atingido! Vida: {batman.vida}")
        if batman.vida <= 0:
            print("Game Over: O Coringa venceu.")
            rodando = False

    if pygame.sprite.spritecollide(coringa, projeteis_batman, True):
        print("Coringa atingido pela lâmina do Batman!")
        

    TELA.fill(AZUL_ESCURO)

    TELA.blit(img_fundo, (0, 0))
    pygame.draw.rect(TELA, (0, 0, 0), (0, 500, LARGURA, 100))

    grupo_batman.draw(TELA)
    grupo_coringa.draw(TELA)
    projeteis_batman.draw(TELA)
    projeteis_coringa.draw(TELA)
    texto_vida = fonte.render(f"Vida/XP do Batman: {batman.vida}", True, VERMELHO)

    pygame.display.flip()

pygame.quit()