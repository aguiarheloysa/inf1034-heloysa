import turtle
import math
import random

# Inicialização da tela
screen = turtle.Screen()
largura_tela = random.randint(800, 1000)
altura_tela = random.randint(600, 800)
screen.setup(width=largura_tela, height=altura_tela)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def reset_canvas():

    t.pu()
    t.goto(0, 0)
    t.setheading(0)
    t.clear()
    screen.bgcolor("white")

def desenhar_plano_cartesiano(passo=50, cor_grade="#D3D3D3"):
    
    t.pu()
    t.color(cor_grade)
    t.pensize(1)
    
    half_w = largura_tela // 2
    half_h = altura_tela // 2

    for x in range(-half_w, half_w, passo):
        t.goto(x, -half_h)
        t.pd()
        t.goto(x, half_h)
        t.pu()

    for y in range(-half_h, half_h, passo):
        t.goto(-half_w, y)
        t.pd()
        t.goto(half_w, y)
        t.pu()

    t.pensize(2)
    t.color("black")
    
    t.goto(-half_w, 0)
    t.pd()
    t.goto(half_w, 0)
    t.pu()

    t.goto(0, -half_h)
    t.pd()
    t.goto(0, half_h)
    t.pu()

def circulo(cx, cy, raio, cor):
    
    t.pu()
    t.goto(cx, cy - raio)
    t.setheading(0)
    t.color(cor)
    t.fillcolor(cor)
    t.begin_fill()
    t.pd()
    t.circle(raio)
    t.end_fill()
    t.pu()

def retangulo(x, y, w, h, cor):
    
    t.pu()
    t.goto(x, y)
    t.setheading(0)
    t.color(cor)
    t.fillcolor(cor)
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y - h)
    t.goto(x, y - h)
    t.goto(x, y)
    t.end_fill()

def triangulo(x1, y1, x2, y2, x3, y3, cor):
    
    t.pu()
    t.goto(x1, y1)
    t.color(cor)
    t.fillcolor(cor)
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()

def estrela(cx, cy, raio_ext, cor, angulo_rotacao=90):
    
    raio_int = raio_ext * 0.381966
    
    t.pu()
    t.color(cor)
    t.fillcolor(cor)
    
    angle_0 = math.radians(angulo_rotacao)
    x0 = cx + raio_ext * math.cos(angle_0)
    y0 = cy + raio_ext * math.sin(angle_0)
    t.goto(x0, y0)
    
    t.begin_fill()
    t.pd()
    
    for i in range(1, 11):
        r = raio_ext if i % 2 == 0 else raio_int
        angle = math.radians(angulo_rotacao + i * 36)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        t.goto(x, y)
            
    t.end_fill()
    t.pu()
    t.setheading(0)

reset_canvas()
# desenhar_plano_cartesiano()

# retangulo(-200, 150, 100, 100, "blue")
# circulo(0, 0, 50, "red")               
# triangulo(100, 50, 150, 150, 200, 50, "green")
# estrela(-100, -100, 40, "lilac")

screen.update()
turtle.done()