#Programa que peça o raio de um círculo, calcule e mostre sua área

from cmath import pi
from socket import SOMAXCONN



raio = int(input("Digite Raio do Circulo em m²: "))

pi = 3.14

area = pi * (raio ** 2)


print ("A área do circulo é de: ", area)


