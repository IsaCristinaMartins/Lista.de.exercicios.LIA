#Escreva uma função que retorne o valor absoluto de cada elemento de uma lista

o = [1,2,3,4,5,6]

def valor(n):
    c = o[n]
    return c

n = int(input("Defina qual elemento da lista vc quer" ))

j = valor(n)

print (j)