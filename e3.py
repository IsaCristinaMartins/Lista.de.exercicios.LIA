# Escreva uma função que retorne a distância Euclidiana entre dois pontos.

# formula euclidiana ->> d = √((xll - xl)^2 + (yll - yl)^2)
import math 

def euclidinho():
   xll = int(input("Coloque o valor de x2")) 
   xl = int(input("Coloque o valor de x1"))
   yl = int (input("Coloque o valor de y1"))
   yll = int (input("Coloque o valor de y2"))
   h = (xll - xl) * (xll - xl)
   k = (yll - yl) * (yll - yl)
   aux = float (h + k)
   resultado  = math.sqrt (aux)
   return xll, xl, yll, yl, h, k, aux, resultado 

foi = euclidinho()

print(foi[7])