import pygame
import sys
import forcapygame, adivinhacaopygame

def valida_email(email: str) -> bool:
    valid: str = "@puc.com"
    for i, c in enumerate(email):
        if c == '@':
            inicio = email[:i]
            if inicio != "":
                if len(email[i:]) == len(valid):
                    if email[i:] == valid:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    return False


def valida_senha(senha: str) -> bool:
    if len(senha) < 8:
        return False
    
    tem_maiuscula: bool = False
    tem_minuscula: bool = False
    tem_numero: bool = False
    
    for c in senha:
        if c.isupper():
            tem_maiuscula = True
        elif c.islower():
            tem_minuscula = True
        elif c.isdigit():
            tem_numero = True
            
    if tem_maiuscula and tem_minuscula and tem_numero:
        return True
    
    return False

def cifra_cesar(texto: str) -> str:
    texto_cifrado: str = ""
    inicio_faixa = ord('0') 
    fim_faixa = ord('z')     
    tamanho_faixa = (fim_faixa - inicio_faixa) + 1
    
    for c in texto:
        codigo = ord(c)
        if inicio_faixa <= codigo <= fim_faixa:
            novo_codigo = inicio_faixa + (codigo - inicio_faixa + 3) % tamanho_faixa
            texto_cifrado += chr(novo_codigo)
        else:
            texto_cifrado += c
            
    return texto_cifrado

def decifra_cesar(texto_cifrado: str) -> str:
    texto_original: str = ""
    inicio_faixa = ord('0') 
    fim_faixa = ord('z')     
    tamanho_faixa = (fim_faixa - inicio_faixa) + 1
    
    for c in texto_cifrado:
        codigo = ord(c)
        if inicio_faixa <= codigo <= fim_faixa:
            
            novo_codigo = inicio_faixa + (codigo - inicio_faixa - 3) % tamanho_faixa
            texto_original += chr(novo_codigo)
        else:
            texto_original += c
            
    return texto_original


print("=== TESTES DE E-MAIL ===")
print("teste_1 (válido):", valida_email("heloysaaguiar@puc.com"))
print("teste_2 (inválido - domínio):", valida_email("heloysaaguiar@puc.com.br"))
print("teste_3 (inválido - sem usuário):", valida_email("@puc.com"))

print("\n=== TESTES DE SENHA ===")
print("senha_1 ('Puc2026!'):", valida_senha("Puc2026!"))
print("senha_2 ('curta1A'):", valida_senha("curta1A"))
print("senha_3 ('apenasletras'):", valida_senha("apenasletras"))

print("\n=== TESTE DA CIFRA DE CÉSAR E DECRIPTOGRAFIA ===")
senha_teste = "Puc1rio3"
cifrada = cifra_cesar(senha_teste)
decriptada = decifra_cesar(cifrada)
print(f"Original: {senha_teste}")
print(f"Cifrada (+3): {cifrada}")
print(f"Decriptada: {decriptada}")

pygame.init()

LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Sistema PUC")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (30, 144, 255)
VERMELHO = (220, 20, 60)
VERDE = (34, 139, 34)
CINZA = (200, 200, 200)
CINZA_ESCURO = (50, 50, 50)

FONTE = pygame.font.SysFont("arial", 24)
FONTE_MENOR = pygame.font.SysFont("arial", 18)

def desenhar_casinha(senha_cifrada: str, senha_decriptada: str):
    TELA.fill((135, 206, 235))
    pygame.draw.rect(TELA, (34, 139, 34), (0, 450, LARGURA, 150))
    pygame.draw.rect(TELA, (245, 222, 179), (300, 250, 200, 200))
    pygame.draw.polygon(TELA, (178, 34, 34), [(400, 150), (250, 250), (550, 250)])
    pygame.draw.rect(TELA, (139, 69, 19), (375, 350, 50, 100))
    pygame.draw.rect(TELA, (173, 216, 230), (320, 280, 50, 50))
    pygame.draw.rect(TELA, PRETO, (320, 280, 50, 50), 2)
    
    titulo = FONTE.render("Projeto 1: Casinha PUC", True, PRETO)
    TELA.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 30))
    
    txt_cifrada = FONTE_MENOR.render(f"Senha Cifrada: {senha_cifrada}", True, PRETO)
    TELA.blit(txt_cifrada, (LARGURA // 2 - txt_cifrada.get_width() // 2, 70))

    txt_decriptada = FONTE_MENOR.render(f"Senha Decriptada: {senha_decriptada}", True, PRETO)
    TELA.blit(txt_decriptada, (LARGURA // 2 - txt_decriptada.get_width() // 2, 95))
    
    instrucao = FONTE_MENOR.render("Pressione ESC para voltar ao menu.", True, CINZA_ESCURO)
    TELA.blit(instrucao, (LARGURA // 2 - instrucao.get_width() // 2, 550))

def rodar_menu(senha_cifrada: str, senha_decriptada: str):
    relogio = pygame.time.Clock()
    projeto_ativo = None
    
    while True:
        TELA.fill(BRANCO)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif evento.type == pygame.KEYDOWN:
                if projeto_ativo is not None:
                    if evento.key == pygame.K_ESCAPE:
                        projeto_ativo = None
                else:
                    if evento.key == pygame.K_1:
                        projeto_ativo = 1
                    elif evento.key == pygame.K_2:
                        projeto_ativo = 2
                    elif evento.key == pygame.K_3:
                        projeto_ativo = 3
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
        if projeto_ativo == 1:
            desenhar_casinha(senha_cifrada, senha_decriptada)
        elif projeto_ativo == 2:
            TELA.fill((240, 240, 240))
            t = FONTE.render("Projeto 1: Jogo da forca", True, AZUL)
            TELA.blit(t, (LARGURA // 2 - t.get_width() // 2, 250))
            voltar = FONTE_MENOR.render("Pressione ESC para voltar ao menu", True, PRETO)
            TELA.blit(voltar, (LARGURA // 2 - voltar.get_width() // 2, 320))
        elif projeto_ativo == 3:
            TELA.fill((240, 240, 240))
            t = FONTE.render("Projeto 2: Jogo adivinhacao", True, VERDE)
            TELA.blit(t, (LARGURA // 2 - t.get_width() // 2, 250))
            voltar = FONTE_MENOR.render("Pressione ESC para voltar ao menu", True, PRETO)
            TELA.blit(voltar, (LARGURA // 2 - voltar.get_width() // 2, 320))
        else:
            titulo = FONTE.render("Menu de Projetos - Selecione uma opção:", True, AZUL)
            TELA.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 150))
            
            p1 = FONTE_MENOR.render("[ 1 ] Casinha (com Cifra de César e Decriptografia)", True, PRETO)
            p2 = FONTE_MENOR.render("[ 2 ] Segundo Projeto / Jogo", True, PRETO)
            p3 = FONTE_MENOR.render("[ 3 ] Terceiro Projeto / Jogo", True, PRETO)
            sair = FONTE_MENOR.render("[ ESC ] Sair do Sistema", True, VERMELHO)
            
            TELA.blit(p1, (200, 250))
            TELA.blit(p2, (200, 300))
            TELA.blit(p3, (200, 350))
            TELA.blit(sair, (200, 420))
            
        pygame.display.flip()
        relogio.tick(30)

def rodar_login():
    email = ""
    senha = ""
    ativo_campo = 1
    mensagem_erro = ""
    relogio = pygame.time.Clock()
    
    while True:
        TELA.fill(BRANCO)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    ativo_campo = 2 if ativo_campo == 1 else 1
                elif evento.key == pygame.K_BACKSPACE:
                    if ativo_campo == 1:
                        email = email[:-1]
                    else:
                        senha = senha[:-1]
                elif evento.key == pygame.K_RETURN:
                    if valida_email(email) and valida_senha(senha):
                        senha_cifrada = cifra_cesar(senha)
                        senha_decriptada = decifra_cesar(senha_cifrada)
                        rodar_menu(senha_cifrada, senha_decriptada)
                    else:
                        mensagem_erro = "E-mail inválido (@puc.com) ou senha fraca (mín. 8 chars, 1 maiúsc, 1 minúsc, 1 núm)."
                else:
                    if evento.key <= 127:
                        if ativo_campo == 1:
                            email += evento.unicode
                        else:
                            senha += evento.unicode
                            
        titulo = FONTE.render("Sistema de Login - PUC", True, AZUL)
        TELA.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 80))
        
        txt_email_label = FONTE_MENOR.render("E-mail (@puc.com):", True, PRETO)
        TELA.blit(txt_email_label, (200, 180))
        
        cor_caixa_1 = AZUL if ativo_campo == 1 else CINZA
        pygame.draw.rect(TELA, cor_caixa_1, (200, 205, 400, 40), 2)
        txt_email_val = FONTE.render(email, True, PRETO)
        TELA.blit(txt_email_val, (210, 212))
        
        txt_senha_label = FONTE_MENOR.render("Senha:", True, PRETO)
        TELA.blit(txt_senha_label, (200, 280))
        
        cor_caixa_2 = AZUL if ativo_campo == 2 else CINZA
        pygame.draw.rect(TELA, cor_caixa_2, (200, 305, 400, 40), 2)
        senha_mascarada = "*" * len(senha)
        txt_senha_val = FONTE.render(senha_mascarada, True, PRETO)
        TELA.blit(txt_senha_val, (210, 312))
        
        instrucao = FONTE_MENOR.render("Pressione ENTER para entrar (TAB alterna os campos)", True, CINZA_ESCURO)
        TELA.blit(instrucao, (LARGURA // 2 - instrucao.get_width() // 2, 400))
        
        if mensagem_erro:
            txt_erro = FONTE_MENOR.render(mensagem_erro, True, VERMELHO)
            TELA.blit(txt_erro, (400 - txt_erro.get_width() // 2, 460))
                
        pygame.display.flip()
        relogio.tick(30)

rodar_login()