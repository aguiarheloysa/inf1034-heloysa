from turtle import *
from math import *
import time
# Criar uma função para desenhar o plano cartesiano (25XP);
# Devem ser desenhadas as seguintes funções matemáticas:
#     - y = √x (50XP)
#     - y = 1/x (50XP)
#     - y = 2^x (50XP)
#     - y = 5 - x^2 (75XP)
#     - y = x^2 - 5x + 6 (75XP)
#     - y = x^3 - x^2 - x + 1 (75XP)
# OBS.: Dar o clear depois de desenhar cada função.


# EXTRA (100XP)
# Fazer uma função para rodar uma "corrida de tartarugas" para N tartarugas (a função só receberá o N como parâmetro).


t = Turtle()
def planoCartesiano():
    t.color("black")
    t.goto(-450,0)
    t.pu()
    t.pd()
    t.goto(450,0)
    t.pu()
    t.pd()
    t.goto(-450,0)
    t.pu()
    t.pd()
    t.goto(450,0)


def raizQuadrada(x):
    return sqrt(x)

def exponencial(x):
    return 2**x

def elevaAoQuadrado(x):
    return 5- x**2

def funcaoParabola(x1, x2):
    return (x1**2 - 5**x2 +6)

def funcaoCubica (x1, x2, x3):
    return (x1**3 - x2**2 - x3 + 1)

for x in range(401):
    t.color("blue")
    t.goto(x, raizQuadrada(10*x))

time.sleep(10)
t.clear()

for x in range(-8,8):
    t.color("green")
    t.goto(x, exponencial(x))
