
a=float(input("digite a nota 1: "))
b=float(input("digite a nota 2: "))

media= (a+b)/2

if(media>=7 and media<=9.99):
    print("Aprovado")
elif(media<6.99):
    print("Reprovado")
    
elif(media==10):
    print("Aprovado com distinção")