letra=[0,12,3,45,6,7,8,9,10]

print(letra[1:10])
print(letra[8:])
print(letra[::2])
print(letra[1::2])
letra.reverse()
print(letra)


par=[]
impar=[]

for num in letra:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print("par: ",par)
print("impar: ",impar)

