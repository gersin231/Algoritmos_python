
a=float(input("digite a nota 1: "))
b=float(input("digite a nota 2: "))

media= (a+b)/2

if(media>=7 and media<=9.9):
    print("Aprovado")
elif(media<7):
    print("Reprovado")
    
elif(media==10):
    print("Aprovado com distinção")