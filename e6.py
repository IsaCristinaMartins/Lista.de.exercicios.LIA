"""""
Um número a é uma potência de b se for divisível por b e a/b for uma
potência de b. Escreva uma função chamada is_power que receba os
parâmetros a e b e retorne True se a for uma potência de b
"""

def is_power (a, b):
  if (b/b) ==0:
    return b**a
  elif b**a:
    return True

k = is_power()