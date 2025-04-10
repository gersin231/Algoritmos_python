salario= float(input("Salario : "))

if (salario<500):
    print((salario*(15/100)))

elif(salario>=500 and salario<=1000):
    print((salario*(10/100)))
    
else:
    print((salario*(5/100)))

