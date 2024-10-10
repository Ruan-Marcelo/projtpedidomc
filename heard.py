import math
from turtle import *

def hearta(R):
    return 12 * math.sin(R)**3

def heartb(R):
    return 12 * math.cos(R) - 5 * \
           math.cos(2*R) - 2 * \
           math.cos(3*R) - \
           math.cos(4*R)

speed(0)  # Define a velocidade máxima do desenho
bgcolor("black")  # Define a cor de fundo como preto
penup()  # Levanta a caneta para não desenhar enquanto se move para o ponto inicial
goto(0, 0)  # Move para o ponto inicial (opcional)
pendown()  # Abaixa a caneta para começar a desenhar

for i in range(1000):  # Um número menor de iterações para suavizar o desenho
    x = hearta(i/100) * 20  # Ajusta o fator de escala
    y = heartb(i/100) * 20  # Ajusta o fator de escala
    goto(x, y)
    color("#f73487")  # Define a cor da linha
    goto(0, 0)  # Retorna ao centro

done()