from turtle import *
from math import *
import time
import random

screen = Screen()
screen.setup(width=700, height=700)
t = Turtle()
t.speed(0)

def planoCartesiano():
    t.clear()
    t.penup()
    t.color("black")
    
    t.goto(-300, 0)
    t.pendown()
    t.goto(300, 0)
    t.stamp()

    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()
    t.goto(0, 300)
    t.stamp()
    t.setheading(0)


def raizQuadrada(x):
    if x < 0:
        return None
    return sqrt(x)

def inversaMult(x):
    if x == 0:
        return None
    return 1 / x

def exponencial(x):
    return 2 ** x

def elevaAoQuadrado(x):
    return 5 - x**2

def funcaoPolinomial(x):
    return x**2 - 5*x + 6

def funcaoCubica(x):
    return x**3 - x**2 - x + 1

def desenhar_funcao(funcao, cor, escala_x=30, x_inicio=-300, x_fim=300):
    planoCartesiano()
    t.color(cor)
    t.penup()
    
    desenhando = False
    
    for x_pixel in range(x_inicio, x_fim + 1):
        x = x_pixel / escala_x
        y_val = funcao(x)
        
        if y_val is None:
            desenhando = False
            continue
            
        y_pixel = y_val * escala_x
        
        if -300 <= y_pixel <= 300:
            t.goto(x_pixel, y_pixel)
            if not desenhando:
                t.pendown()
                desenhando = True
        else:
            desenhando = False
            t.penup()

    time.sleep(3)

# 1. y = √x
desenhar_funcao(raizQuadrada, "blue", escala_x=30, x_inicio=0, x_fim=300)

# 2. y = 1/x
desenhar_funcao(inversaMult, "purple", escala_x=30, x_inicio=-300, x_fim=300)

# 3. y = 2^x
desenhar_funcao(exponencial, "green", escala_x=30, x_inicio=-300, x_fim=300)

# 4. y = 5 - x^2
desenhar_funcao(elevaAoQuadrado, "red", escala_x=30, x_inicio=-300, x_fim=300)

# 5. y = x^2 - 5x + 6
desenhar_funcao(funcaoPolinomial, "orange", escala_x=30, x_inicio=-300, x_fim=300)

# 6. y = x^3 - x^2 - x + 1
desenhar_funcao(funcaoCubica, "magenta", escala_x=30, x_inicio=-300, x_fim=300)


# --- EXTRA: CORRIDA DE TARTARUGAS ---

def corrida_tartarugas(n):
    t.clear()
    t.penup()
    t.goto(0, 260)
    t.color("black")
    t.write("CORRIDA DE TARTARUGAS", align="center", font=("Arial", 16, "bold"))
    
    # Desenhar linha de chegada
    t.goto(250, 220)
    # t.stamp()
    t.setheading(270)
    t.pendown()
    t.goto(250, -220)
    
    tartarugas = []
    cores = ["red", "blue", "green", "orange", "purple", "cyan", "magenta", "brown"]
    
    # Espaçamento vertical entre as N tartarugas dentro da área do plano
    altura_util = 300
    passo_y = altura_util / max(1, n - 1) if n > 1 else 0
    
    for i in range(n):
        racer = Turtle(shape="turtle")
        racer.color(cores[i % len(cores)])
        racer.penup()
        y_pos = 200 - (i * passo_y)
        racer.goto(-250, y_pos)
        tartarugas.append(racer)
        
    time.sleep(1)
    
    chegada = False
    vencedor = None
    
    while not chegada:
        for i, racer in enumerate(tartarugas):
            passo = random.randint(3, 10)
            racer.forward(passo)
            if racer.xcor() >= 250:
                chegada = True
                vencedor = i + 1
                break
                
    # Anunciar vencedor
    t.penup()
    t.goto(0, -270)
    t.write(f"A Tartaruga {vencedor} venceu a corrida!", align="center", font=("Arial", 14, "bold"))
    t.pu()

corrida_tartarugas(8)
done()