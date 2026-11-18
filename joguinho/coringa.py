import pygame
import os
from projetil import Projetil

class Coringa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, 'assets', 'coringa.png')
        self.image = pygame.image.load(path).convert_alpha()
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

