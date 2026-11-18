import pygame

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
