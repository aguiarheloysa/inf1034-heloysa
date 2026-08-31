import turtle
import time
import math

screen = turtle.Screen()
screen.title("Bandeiras do Mundo")
screen.setup(width=1000, height=700)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

WIDTH = 600
HEIGHT = 400

def reset_canvas():
    t.pu() 
    t.goto(0, 0)
    t.setheading(0)
    t.clear()
    screen.bgcolor("white")

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


def bandeira_turquia():
    reset_canvas()
    x, y = -300, 200
    retangulo(x, y, WIDTH, HEIGHT, "#E30A17")
    
    # Lua crescente
    t.pu()
    t.goto(-70, -100)
    t.setheading(0)
    t.color("#FFFFFF")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    
    t.goto(-45, -80)
    t.color("#E30A17")
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    
    estrela(70, 0, 35, "#FFFFFF", 0)

def bandeira_gana():
    reset_canvas()
    x, y = -300, 200
    h_faixa = HEIGHT / 3
    
    retangulo(x, y, WIDTH, h_faixa, "#CE1126")
    retangulo(x, y - h_faixa, WIDTH, h_faixa, "#FCD116")
    retangulo(x, y - 2 * h_faixa, WIDTH, h_faixa, "#006B3F")
    
    estrela(0, 0, 45, "#000000", 90)

def bandeira_palestina():
    reset_canvas()
    x, y = -300, 200
    h_faixa = HEIGHT / 3
    
    retangulo(x, y, WIDTH, h_faixa, "#000000")
    retangulo(x, y - h_faixa, WIDTH, h_faixa, "#FFFFFF")
    retangulo(x, y - 2 * h_faixa, WIDTH, h_faixa, "#007A3D")
    
    triangulo(x, y, x, y - HEIGHT, x + 200, y - (HEIGHT / 2), "#CE1126")

def bandeira_chile():
    reset_canvas()
    x, y = -300, 200
    
    retangulo(x, y - 200, WIDTH, 200, "#D52B1E")
    retangulo(x, y, 200, 200, "#0039A6")
    retangulo(x + 200, y, 400, 200, "#FFFFFF")
    
    estrela(-200, 100, 40, "#FFFFFF", 90)

def bandeira_bahamas():
    reset_canvas()
    x, y = -300, 200
    h_faixa = HEIGHT / 3
    
    retangulo(x, y, WIDTH, h_faixa, "#00778B")
    retangulo(x, y - h_faixa, WIDTH, h_faixa, "#FFC72C")
    retangulo(x, y - 2 * h_faixa, WIDTH, h_faixa, "#00778B")
    
    triangulo(x, y, x, y - HEIGHT, x + 230, y - (HEIGHT / 2), "#000000")

def bandeira_costa_rica():
    reset_canvas()
    x, y = -300, 200
    h_faixa = HEIGHT / 6
    
    retangulo(x, y, WIDTH, h_faixa, "#001489")
    retangulo(x, y - h_faixa, WIDTH, h_faixa, "#FFFFFF")
    retangulo(x, y - 2 * h_faixa, WIDTH, 2 * h_faixa, "#DA291C")
    retangulo(x, y - 4 * h_faixa, WIDTH, h_faixa, "#FFFFFF")
    retangulo(x, y - 5 * h_faixa, WIDTH, h_faixa, "#001489")

def bandeira_noruega():
    reset_canvas()
    x, y = -300, 200
    
    retangulo(x, y, WIDTH, HEIGHT, "#BA0C2F")
    
    retangulo(x + 150, y, 100, HEIGHT, "#FFFFFF")
    retangulo(x, y - 150, WIDTH, 100, "#FFFFFF")
 
    retangulo(x + 175, y, 50, HEIGHT, "#00205B")
    retangulo(x, y - 175, WIDTH, 50, "#00205B")

def bandeira_china():
    reset_canvas()
    x, y = -300, 200
    retangulo(x, y, WIDTH, HEIGHT, "#EE1C25")
    
    estrela(-200, 100, 45, "#FFDE00", 90)
    
    estrelas_menores = [
        (-110, 150, 15, 120),
        (-80, 120, 15, 100),
        (-80, 70, 15, 90),
        (-110, 40, 15, 75)
    ]
    
    for ex, ey, r, rot in estrelas_menores:
        estrela(ex, ey, r, "#FFDE00", rot)

bandeiras = [
    bandeira_turquia,
    bandeira_gana,
    bandeira_palestina,
    bandeira_chile,
    bandeira_bahamas,
    bandeira_costa_rica,
    bandeira_noruega,
    bandeira_china
]

for i, desenhar in enumerate(bandeiras):
    desenhar()
    screen.update()
    
    if i < len(bandeiras) - 1:
        time.sleep(15)

screen.mainloop()