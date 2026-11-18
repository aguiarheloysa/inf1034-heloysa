import pygame, os, sys
from batman import Batman
from coringa import Coringa
from gerenciador import GerenciadorItens

pygame.init()
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))

atual_dir = os.path.dirname(__file__)
caminho = os.path.join(atual_dir, 'assets', 'gotham.webp')

imagem_fundo = pygame.image.load(caminho).convert_alpha()
img_fundo = pygame.transform.scale(imagem_fundo, (800, 600))
img_fundo.set_alpha(90)

pygame.display.set_caption("Batman 2D - O Resgate de Gotham")

relogio = pygame.time.Clock()
FPS = 60

AZUL_ESCURO = (20, 20, 40)
VERMELHO = (220, 20, 60)
AMARELO = (255, 215, 0)
PRETO = (0, 0, 0)

batman = Batman(100, 400, LARGURA)
coringa = Coringa(600, 440)
gerenciador_itens = GerenciadorItens(LARGURA)

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
    projeteis_batman.update()
    
    gerenciador_itens.atualizar(batman)

    if gerenciador_itens.todos_coletados:
        grupo_coringa.update(projeteis_coringa)
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
    pygame.draw.rect(TELA, PRETO, (0, 500, LARGURA, 100)) 

    grupo_batman.draw(TELA)
    projeteis_batman.draw(TELA)
    gerenciador_itens.desenhar(TELA)

    if gerenciador_itens.todos_coletados:
        grupo_coringa.draw(TELA)
        projeteis_coringa.draw(TELA)

    texto_vida = fonte.render(f"Vida: {batman.vida}", True, VERMELHO)
    TELA.blit(texto_vida, (20, 20))
    
    texto_itens = fonte.render(f"Evidências Restantes: {gerenciador_itens.itens_restantes()}", True, AMARELO)
    TELA.blit(texto_itens, (20, 50))

    pygame.display.flip()

pygame.quit()