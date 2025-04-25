while True:
    nome=input("Digite o nome:")
    idade=int(input("Digite a idade:"))
    salario=float(input("Digite o salario:"))
    sexo=input("Digite o sexo:")
    Estado_Civil=input("Digite o Estado Civil:")
    quantidade = len(nome)
    
    if (quantidade>=3 and 
    idade>=0 and idade<=150 and 
    sexo in["m","f","o"] and 
    Estado_Civil in ["s","c","v","d"]):

        
        print(f" nome: {nome}\n idade: {idade}\n salario: {salario}\n sexo: {sexo}\n Estado Civil: {Estado_Civil}")
        break
    else:
        print("Tente novamente")
        