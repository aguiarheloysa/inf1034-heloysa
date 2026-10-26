import pygame, sys
from pygame.locals import QUIT, KEYDOWN
import random

def contabiliza_totais(min, max, nums, amplitude, tam_cat, l_cont):
    # Para cada número na minha lista
    for i in range(len(nums)):
        if nums[i] == max:
            l_cont[-1] += 1
            continue

        # Para cada faixa/categoria
        for i_cat in range(amplitude):
            # Obtém os limites inferior e superior
            lim_inf = min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            # Checa em qual faixa/categoria o número está com base nesses limites
            if lim_inf <= nums[i] < lim_sup:
                l_cont[i_cat] += 1
                break
    return l_cont

faixa : int = 4
tam :int = 60
l1 = []
i:int = 0
while i<tam:
    l1.append(random.randint(100, 300))
    i+=1
l1.sort()
print("len(l1)",len(l1))
l1_menor :int = l1[0]
l1_maior :int = l1[-1] #pega sempre o último elemento
amplitude :int = (l1_maior - l1_menor) // tam
l1_cont = [0]* faixa
print("amplitude \nl1_cont", amplitude, l1_cont)
# l1
print(contabiliza_totais(l1_menor, l1_maior, l1, amplitude, faixa, l1_cont))

l2 = [2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 21000, 
        12150, 1250, 3150, 4150, 5150, 6520, 7250, 8350, 3950, 10350,
        42175, 9275, 9375, 9475, 8575, 9675, 9775, 39875, 9975, 71075,
        1250, 8125, 8225, 8325, 8425, 9525, 9625, 9725, 9825, 9925, 10115,
        11218, 11880, 8000, 1500, 3000, 2000, 18000, 20000, 6780, 1500, 1600,
        1800, 62738, 82920, 7352, 82902, 62353, 11900, 23500]
tot_el = len(l2)
# print("Total de elementos na lista estática:", tot_el)

l2.sort()
l2_menor: int = l2[0]
l2_maior: int = l2[-1]  #pega sempre o último elemento
tam_l2 :int = 6
l2_cont = []
soma_acumulada = 0
# print("len(l2)",len(l2))
l2.sort()
l2_menor: int = l2[0]
amplitude_l2: int = (l2_maior - l2_menor) // tam_l2 #as listas possuem a mesma quantidade de elementos, reaproveitei o tamnaho

for i in range(tam_l2):
  if i == tam_l2 - 1:
    max_possivel = tot_el - soma_acumulada
  else:
    max_possivel = tot_el - soma_acumulada - (tam_l2 - 1 - i)
    if max_possivel < 0:
      max_possivel = 0

  qtd_faixa = random.randint(0, max_possivel)
  l2_cont.append(qtd_faixa)
  soma_acumulada += qtd_faixa
print(f"amplitude l2: {amplitude_l2}")
print(f"frequencia l2: {l2_cont}")
print(f"tamanho l2: {tam_l2}")
print(f"l2: {l2}")
# l2
print(contabiliza_totais(l2_menor, l2_maior, l2, tam_l2, amplitude_l2, l2_cont))
def exibe(screen, color, title):
    pygame.display.set_caption(title)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        draw(screen, color)
        pygame.display.update()
        clock.tick(60)

l3 = []
while True:
    num  = input("digite um númeor: \npara interromper o programa digite espaço e dê enter ")
    
    if num == " ":
        break
    num = int(num.strip())
    # print(f"tipo - {type(num)} ---- numero: {num}")
    l3.append(num)

l3.sort()
l3_menor :int = l3[0]
l3_maior :int = l3[-1] #pega sempre o último elemento
faixa_l3: int = int(input("Digite um número para a faixa/cateoria: "))
amplitude_l3 :int = (l3_maior - l3_menor) // faixa_l3 +1
l3_cont = [0]* amplitude_l3
print("amplitude \nl3_cont", amplitude, l3_cont)
# l3
print(contabiliza_totais(l3_menor, l3_maior, l3, amplitude_l3, faixa_l3, l3_cont))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((550, 650))

histos = [ 
    {"dados":l1_cont, "cor": "red", "titulo": "Histograma-1"},
    {"dados":l2_cont, "cor": "green", "titulo": "Histograma-2"},
    {"dados":l3_cont, "cor": "pink", "titulo": "Hitograma-3"}
]

def draw(screen, color, dados):
    screen.fill((0, 0, 0)) 
    screen_h = screen.get_height()
    for i in range(len(dados)):
        x = 60 + i * 70
        h = 15 * dados[i]
        pygame.draw.rect(screen, color, (x, screen_h - h - 60, 45, h))
i: int = 0
while True:
    histo_atual = histos[i]
    pygame.display.set_caption(f"{histo_atual['titulo']} (Pressione ESPAÇO para mudar)")
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                i = (i + 1) % len(histos) # Vai para o próximo e volta para o 0 ao chegar no fim

    draw(screen, histo_atual["cor"], histo_atual["dados"])
    
    pygame.display.update()
    clock.tick(60)
