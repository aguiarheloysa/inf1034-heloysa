import sys
import pygame
import random

faixa : int = 20
tam :int = 50
l1 = []
i:int = 0
while i<tam:
    l1.append(random.randint(100, 300))
    i+=1
l1.sort()
print(l1)
amplitude :int = (l1[0] + l1[59]) // tam
l1_cont = [0* amplitude]
print("amplitude", amplitude)


l2 = []
while i<60:
    l2.append(random.randint(300, 500))
    i+=1
l2.sort()
print(l2)
