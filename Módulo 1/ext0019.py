"""Faça um programa que leia um comprimento de cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa."""


import math

ca = float(input('Cateto Opostosto: '))
co = float(input('Cateto Adjacente: '))
hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

print(f'O resultado é: {hipotenusa:.2f}')