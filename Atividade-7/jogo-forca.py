# JOGO DA FORCA

# PRINCIPAL 700XP
# - Condição de vitória: Acertar a palavra toda 100XP;
# - Condição de derrota: Perder todos os membros/vidas (6 no total) 100XP;
# - Ao começar o jogo uma palavra aleatória deve ser gerada com base em uma LISTA DE PALAVRAS (todas dentro de um mesmo tema) 100XP;
# - A entrada do usuário deve ser validada, permitindo que ele digite SOMENTE LETRAS 200XP;
# - A única exceção é para o caso do jogador chutar uma palavra inteira 100XP;
# - O jogo deve poder ser reiniciado 100XP;

# EXTRA 300XP
# - Tudo da forca, porém feito no PyGame, devendo ter interação com o teclado para entrada de dados.

from random import choices

lista_palavaras = ["vermelho", "carro", "piscina", "notebook", "tempo", 
    "cor", "musica", "viajar", "futebol", "basquete", "praia", "roxo", "azul", "verde"]

palavra_aleatoria = choices(lista_palavaras)
palavra_oculta =  len(palavra_aleatoria) * "_ "
print(len(palavra_aleatoria))
print(palavra_aleatoria)
print(palavra_oculta)
