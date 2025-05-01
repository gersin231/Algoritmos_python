votos=[]
voto1 = voto2 = voto3 = voto4 = voto5 = voto6 = 0
nomes_candidatos = {
    1: "Candidato 1",
    2: "Candidato 2",
    3: "Candidato 3",
    4: "Candidato 4",
    5: "Candidato 5",
    6: "Candidato 6"
}
while True:
    codigo=int(input("Digite a votos do candidato:"))
       
    if candidatos == 1:
        votos.append(candidatos)
        voto1=votos.count(1)
    elif candidatos ==2:
        votos.append(candidatos)
        voto2=votos.count(2)
    elif candidatos ==3:
        votos.append(candidatos)
        voto3=votos.count(3)
    elif candidatos ==4:
        votos.append(candidatos)
        voto4=votos.count(4)
    elif candidatos ==5:
        votos.append(candidatos)
        voto5=votos.count(5)
    elif candidatos ==6:
        votos.append(candidatos)
        voto6=votos.count(6)
    elif candidatos ==0:
        print("sair")
        break

    print(f"o candidato 1 teva:{voto1} votos")
    print(f"o candidato 2 teva:{voto2} votos")
    print(f"o candidato 3 teva:{voto3} votos")
    print(f"o candidato 4 teva:{voto4} votos")
    print(f"votos nulos:{voto5} votos")
    print(f"votos em branco:{voto6} votos")
    
    maior_voto = max(voto1, voto2, voto3, voto4, voto5, voto6)
    menor_voto = min(voto1, voto2, voto3, voto4, voto5, voto6)
    

    print(f"O maior número de votos é: {maior_voto}")
    print(f"O menor número de votos é: {menor_voto}")