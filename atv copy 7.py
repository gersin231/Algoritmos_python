import os
valor = input("Digite um valor em decimal para converter em binário:")
valor_binario=[]
x=len(valor)

for i in valor:
    x= x - 1
    if i =="1":
        z=2**x
        valor_binario.append(z)

