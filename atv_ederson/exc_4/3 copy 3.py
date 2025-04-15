
horas_trab=float(input("digite o valor de horas trabalhadas: "))



if(horas_trab<=900):
    print("Aprovado")
elif(horas_trab>900 and horas_trab<=1500):
    porcentagem=5
    IR=5
    INSS=10
    
    total_des=horas_trab*(IR/100) +horas_trab*(INSS/100)
    print(total_des)
    
