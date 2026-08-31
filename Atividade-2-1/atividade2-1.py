from turtle import *

t = Turtle()

t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()
t.rt(90)

t.pu()
t.goto(0, 0)
t.pd()

t.pu()
t.goto(100, 90)
t.pd()

t.color("yellow")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica:")
t.fillcolor(var_color)
t.begin_fill()

#pentágono
t.fd(172)
t.lt(90)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(90)
t.end_fill()

t.pu()
t.goto(0, 0)
t.pd()
t.pu()
t.goto(-250, 100)
t.color("green")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica:")
t.fillcolor(var_color)
t.begin_fill()
t.pd()
#hexagono
for cont in range(8):
    t.fd(80)
    t.lt(45)
t.end_fill()

t.pu()
t.goto(-300, 200)
t.pd()
t.color("blue")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica:")
t.fillcolor(var_color)
t.begin_fill()
#espiral
for i in range(25):
    t.fd(i)  
    t.lt(60)        
t.end_fill()

t.pu()
t.goto(-250, -200)
t.pd()
t.color("#C8A2C8")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica:")
t.fillcolor(var_color)
t.begin_fill()
#trapezio
t.fd(200)
t.lt(120)
t.fd(100)
t.lt(60)  
t.fd(100)
t.lt(60)  
t.fd(100)
t.end_fill()

t.pu()
t.goto(250, -200)
t.pd()
t.rt(60)
t.color("orange")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica:")
t.fillcolor(var_color)
t.begin_fill()
#triangulo
t.fd(150)
t.rt(60)
t.fd(100)
t.lt(90)

t.end_fill()

mainloop()