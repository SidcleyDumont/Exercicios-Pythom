#Programa que peça as 4 notas bimestrais e mostre a média.

from msilib.schema import Media
from statistics import median


valor1 = float(input("Digite valor 1: "))

valor2 = float(input("Digite valor 2: "))

valor3 = float(input("Digite valor 3: "))

valor4 = float(input("Digite valor 4: "))


Media1 = (valor1+valor2+valor3+valor4)/4


print("Sua Média Final é:  " , Media1)