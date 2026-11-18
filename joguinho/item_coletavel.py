import pygame, os
import math

class ItemColetavel(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo):
        super().__init__()
        
        diretorio_atual = os.path.dirname(__file__)

        if tipo == "arma":
            caminho_imagem = os.path.join(diretorio_atual, 'assets', 'arma-batman.png')
        elif tipo == "armadura":
            caminho_imagem = os.path.join(diretorio_atual, 'assets', 'armadura-batman.png')
        else:
            caminho_imagem = os.path.join(diretorio_atual, 'assets', 'laminas-batman.png')
            
        try:
            self.image = pygame.image.load(caminho_imagem).convert_alpha()
            self.image = pygame.transform.scale(self.image, (30, 30)) 
        except (pygame.error, FileNotFoundError):
            self.image = pygame.Surface((30, 30))
            self.image.fill((255, 215, 0) if tipo == "arma" else (50, 205, 50))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.tipo = tipo
        
        self.y_inicial = y
        self.tempo = 0

    def update(self):
        self.tempo += 0.1
        self.rect.y = self.y_inicial + math.sin(self.tempo) * 5
