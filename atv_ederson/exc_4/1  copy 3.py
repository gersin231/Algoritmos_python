nome=input("nome: ")
salario= float(input("Salario : "))

if (salario<280.55):
    porcent =22.51 
    a=(salario*(22.51/100))
    

elif(salario>=280.56 and salario<=709.72):
  porcent =15.39 
  a=(salario*(15.39/100))
   
    
elif(salario>709.72 and salario<=1501.33):
    porcent =10.97 
    a=(salario*(10.97/100))

else:
     porcent =5.19 
     a=(salario*(5.19/100))
    
print(nome)
print("antes do reajuste",salario)
print("porcentagem do Aumento",porcent)
print("valor do aumento",a,"%")
print("novo salario",salario+a)






