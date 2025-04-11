nome=input("nome: ")
salario= float(input("Salario : "))
b=100
if (salario<280.55):
    porcent =22.51 
    a=(salario*(22.51/100))
    p_aumento=a-b

elif(salario>=280.56 and salario<=709.72):
    porcent =15.39 
    a=(salario*(15.39/100))
    p_aumento=a-b
    
elif(salario>709.72 and salario<=1501.33):
    porcent =10.97 
    a=(salario*(10.97/100))
    p_aumento=a-b
    p_aumento=a-b

else:
     porcent =5.19 
     a=(salario*(5.19/100))
     p_aumento=a-b
    
print(nome)
print(f"antes do reajuste:{salario:.2f}")
print(f"porcentagem do Aumento: {p_aumento:.2f} R$")
print(f"valor do aumento: {porcent:.2f}%")
print(f"novo salario: {salario+a:2f} R$4")






