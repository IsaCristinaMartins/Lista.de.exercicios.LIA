#Faça a função de fibonacci(n) que recebe uma entrada n e retorna o n-ésimo número na sequência de Fibonacci.

def fibbo(n):
  if n==1:
    return 1
  elif n== 0:
    return 0
  return (n -1) + (n-2)

h = fibbo()