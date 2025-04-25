print("******************************** \n"
"calculadora\n"

"1 adição\n"
"2 subtração\n"
"3 multiplicação\n"
"4 divisão\n"
"S ou s para sair\n"
"********************************")
while True:
    esc=input("escolha: ")

    if esc =="1":
        print("adição")
        n=float(input("digite um numero: "))
        n2=float(input("digite um numero: "))
        res= n+n2
        print(res)
    elif esc =="2":
        print("subtração")
        n=float(input("digite um numero: "))
        n2=float(input("digite um numero: "))
        res= n-n2
        print(res)
    elif esc =="3":
        print("multiplicação")
        n=float(input("digite um numero: "))
        n2=float(input("digite um numero: "))
        res= n*n2
        print(res)
    elif esc =="4":
        print("divisa")
        n=float(input("digite um numero: "))
        n2=float(input("digite um numero: "))
        res= n/n2
        print(res)

    elif esc == "S" or esc=="s":
        break

