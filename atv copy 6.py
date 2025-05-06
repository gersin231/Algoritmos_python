# lista=[10,20,12,33,24,15,18,99,56,478]
# x=0
# while x < len(lista):
#     print(x,lista[x])
#     x += 1

# import os
# valor = float(input("Digite um valor em decimal para converter em binário:"))
# valor_binario=[]

# while valor> 0:
#     novovalor= valor % 2
#     novovalor=int(novovalor)
#     print("Resto: ",valor)
#     valor= valor/2
#     print("Divisor: ",valor)
#     valor=int(valor)
#     valor_binario.insert(0,novovalor)

# output= " ".join(map(str,valor_binario))
# print(output)

import os
valor = input("Digite um valor em decimal para converter em binário:")
valor_binario=[]
x=len(valor)

for i in valor:
    x= x - 1
    if i =="1":
        z=2**x
        valor_binario.append(z)

