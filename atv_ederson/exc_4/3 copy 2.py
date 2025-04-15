
horas_trab=float(input("digite o valor de horas trabalhadas: "))
horas_por_mes=float(input("digite as horas trabalhadas por mes: "))
salario_bruto=horas_trab*horas_por_mes
FGTS=11

print("Salário Bruto:" "(",horas_trab,"*",horas_por_mes,")")

if(salario_bruto<=900):
    print("Aprovado")
elif(salario_bruto>900 and salario_bruto<=1500):
    IR=salario_bruto*(5/100)
    INSS=salario_bruto*(10/100)
    FGTS=salario_bruto*(10/100)
    
    total_des=IR +INSS
    salario_liquido=salario_bruto-total_des
    print("(-) IR (5%)                   :",IR)
    print("(-) INSS (10%)                   :",INSS)
    print("(-) FGTS (11%)                   :",FGTS)
    print("Total de descontos               :",total_des)
    print("Salario liquido                  :",salario_liquido)
elif(salario_bruto>1500 and salario_bruto<=2500):
    IR=salario_bruto*(10/100)
    INSS=salario_bruto*(10/100)
    total_des=IR +INSS
    salario_liquido=salario_bruto-total_des
    print("(-) IR (10%)                   :",IR)
    print("(-) FGTS (11%)                   :",FGTS)
    print("Total de descontos               :",total_des)
    print("Salario liquido                  :",salario_liquido)
elif(salario_bruto>2500):
    IR=salario_bruto*(20/100)
    INSS=salario_bruto*(10/100)
    total_des=IR +INSS
    salario_liquido=salario_bruto-total_des
    print("(-) IR (20%)                   :",IR)
    print("(-) FGTS (11%)                   :",FGTS)
    print("Total de descontos               :",total_des)
    print("Salario liquido                  :",salario_liquido)


