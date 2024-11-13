"""Exercício 08.

Soma e Média de Números
Crie um programa que leia cinco números e apresente a soma e a média desses números.
"""

numeros = []
i = 1
while i < 6:
    num = int(input(f"Digite um numero {i}: "))
    numeros.append(num)
    i += 1
print(f"Numeros: {numeros}")

soma = sum(numeros)
print(f"A some deles é: {soma}")

med = sum(numeros) / len(numeros)
print(f"A media deles é: {med}")
