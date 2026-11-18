import pygame
import os
from projetil import Projetil

class Batman(pygame.sprite.Sprite):
    def __init__(self, x, y, largura):
        super().__init__()
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, 'assets', 'batman.png')
        self.image = pygame.image.load(path).convert_alpha()
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
        self.largura = largura

    def update(self, teclas):
        movimento_x = 0
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            movimento_x = -self.velocidade_x
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            movimento_x = self.velocidade_x
        self.rect.x += movimento_x

        if self.rect.left < 0: 
            self.rect.left = 0
        if self.rect.right > self.largura: 
            self.rect.right = self.largura

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
