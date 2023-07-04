"""""
Faça uma função que retorne as raizes de uma equação do segundo grau
"""
import math

def raiz (a,b, c):
  delta = (b**2) - 4*a*c
  aux = math.sqrt(delta)
  x1 = (-b + aux)/ (2*a)
  x2 = (-b - aux)/ (2*a)
  return x1, x2

k = raiz(2,3,1)
print (k)