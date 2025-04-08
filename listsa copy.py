print("******************************** \n"
"calculadora\n"

"1 adição\n"
"2 subtração\n"
"3 multiplicação\n"
"4 divisão\n"
"********************************")

esc=input("escolha: ")

if esc =="1":
    n=int(input("digite um numero: "))
    n2=int(input("digite um numero: "))
    res= n+n2
    print(res)
elif esc =="2":
    n=int(input("digite um numero: "))
    n2=int(input("digite um numero: "))
    res= n-n2
    print(res)
elif esc =="3":
    n=int(input("digite um numero: "))
    n2=int(input("digite um numero: "))
    res= n*n2
    print(res)
elif esc =="4":
    n=int(input("digite um numero: "))
    n2=int(input("digite um numero: "))
    res= n/n2
    print(res)

else:
    print("ERRRO")

