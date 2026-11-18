import random
import pygame
from item_coletavel import ItemColetavel

class GerenciadorItens:
    def __init__(self, largura):
        self.grupo_itens = pygame.sprite.Group()
        self.todos_coletados = False
        self.largura = largura
        locais_possiveis = [
            (300, 450), (400, 380), (500, 450), 
            (600, 280), (700, 350), (200, 320)
        ]
        
        locais_escolhidos = random.sample(locais_possiveis, 3)
        
        for x, y in locais_escolhidos:
            self.grupo_itens.add(ItemColetavel(x, y, "evidencia"))

    def atualizar(self, batman):

        self.grupo_itens.update()

        itens_coletados = pygame.sprite.spritecollide(batman, self.grupo_itens, True)
        
        for item in itens_coletados:
            print(f"{item.tipo} coletada! Restam: {len(self.grupo_itens)}")

        if len(self.grupo_itens) == 0 and not self.todos_coletados:
            self.todos_coletados = True
            print("Todas as evidências coletadas! Coringa liberado!")

    def desenhar(self, tela):
        self.grupo_itens.draw(tela)

    def itens_restantes(self):
        return len(self.grupo_itens)