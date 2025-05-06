print("******************************** \n"
"calculadora\n"

"a ou A = adição\n"
"s ou Ssubtração\n"
"m ou M multiplicação\n"
"d ou D divisão\n"
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

