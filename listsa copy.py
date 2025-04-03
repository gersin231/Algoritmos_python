"********************************"
"calculadora"

"1 adição"
"2 subtração"
"3 multiplicação"
"4 divisão"
"********************************"
n=int(input("digite um numero: "))
n2=int(input("digite um numero: "))
esc=input("escolha: ")

if esc =="1":
    res= n+n2
    print(res)
elif esc =="2":
    res= n-n2
    print(res)
elif esc =="3":
    res= n*n2
    print(res)
elif esc =="4":
    res= n/n2
    print(res)

else:
    print("ERRRO")

