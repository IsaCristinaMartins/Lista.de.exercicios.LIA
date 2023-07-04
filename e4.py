#Escreva uma função de forma recursiva que retorne o fatorial de um número
#fatorial: vc multiplica o número inicial pelo número logo abaixo até chagar no 1: 5! = 5*4*3*2*1 -> 120

def fatorial(n):
  if n==0:
    return 1
  return (n-1) * n

j = fatorial ()