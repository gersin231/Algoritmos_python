# while True:
#     valor=int(input("Digite 1 ou 0 para fim: "))
    
#     if valor==1:
#         print("Valor correto")
#     else:
#         print("valor para sair")
#         break
valor=float(input("Digite o numero a ser multiplicado: "))
valo=float(input("Digite a quantdade de vezes a ser multiplicade de 0 a 50: "))

while valor <50:
    valor= valor+1
    mult= valo * valor
    print(f"{valo} x {valor:.0f} = {mult}")