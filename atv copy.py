# lista=[1,2,1,5,6,4,3,1]
# print(lista.count(1))

# fruta=["maça","banana","pera","kiwi","uva"]
# fruta[2:2]=["laranja"]

# t=[[1,2],[3],[4,5,6]]

# print (sum(t[0])+sum(t[1])+ sum(t[2]))

t=[1,2,3]

print ([sum(t[0:1]),sum(t[0:2]),sum(t[0:3])])


# a= t[0]
# b=t[0]+t[1]
# c=b+t[2]

# soma=[a,b,c]
# print (soma)
t=[1,2,3,4]

print(t[1:3])

country=["Alemanha","Itália","japão"]
country.extend([
    "Algéria", "Argel",
    "Andorra", "Andorra-a-Velha",
    "Angola", "Luanda",
    "Antígua e Barbuda", "São João",
    "Arábia Saudita", "Riad",
    "Argentina", "Buenos Aires",
    "Armênia", "Erevã",
    "Austrália", "Camberra",
    "Áustria", "Viena",
    "Azerbaijão", "Baku",
    "Bahamas", "Nasáu",
    "Bangladesh", "Daca",
    "Barbados", "Bridgetown",
    "Barein", "Manama",
    "Bélgica", "Bruxelas",
    "Belize", "Belmopan",
    "Benin", "Porto-Novo (formal), Cotonou (sede do governo)",
    "Birmânia", "Naypyidaw",
    "Bielorrússia", "Minsk",
    "Bolívia", "Sucre (constitucional), La Paz (administrativa)",
    "Bosnía e Herzegovina", "Sarajevo",
    "Botsuana", "Gaborone",
    "Brasil", "Brasília",
    "Brunei", "Bandar Seri Begawan",
    "Bulgária", "Sofia",
    "Burkina Faso", "Ouagadougou",
    "Burundi", "Bujumbura (anterior), Gitega (atualmente)",
    "Butão", "Thimphu",
    "Cabo Verde", "Praia",
    "Camarões", "Yaoundé",
    "Camboja", "Phnom Penh",
    "Canadá", "Ottawa",
    "Catar", "Doha",
    "Chade", "N'Djamena",
    "Chile", "Santiago",
    "China", "Pequim",
    "Chipre", "Nicósia",
    "Colômbia", "Bogotá",
    "Comores", "Moroni",
    "Congo (República do Congo)", "Brazzaville",
    "Congo (República Democrática do Congo)", "Kinshasa",
    "Coreia do Norte", "Pyongyang",
    "Coreia do Sul", "Seul",
    "Costa Rica", "São José",
    "Croácia", "Zagreb",
    "Cuba", "Havana",
    "Curaçau", "Willemstad",
    "Dinamarca", "Copenhague",
    "Djibuti", "Djibuti",
    "Dominica", "Roseau",
    "Egito", "Cairo",
    "El Salvador", "San Salvador",
    "Emirados Árabes Unidos", "Abu Dhabi",
    "Equador", "Quito",
    "Eritreia", "Asmara",
    "Eswatini", "Mbabane (administrativa), Lobamba (legislativa)",
    "Eslováquia", "Bratislava",
    "Eslovênia", "Liubliana",
    "Espanha", "Madri",
    "Estados Unidos", "Washington, D.C.",
    "Estônia", "Tallinn",
    "Etiópia", "Adis Abeba",
    "Fiji", "Suva",
    "Filipinas", "Manila",
    "Finlândia", "Helsinque",
    "França", "Paris",
    "Gabão", "Libreville",
    "Gâmbia", "Banjul",
    "Gana", "Acra",
    "Grécia", "Atenas",
    "Grenada", "Saint George's",
    "Guatemala", "Cidade da Guatemala",
    "Guiana", "Georgetown",
    "Guiné", "Conacri",
    "Guiné-Bissau", "Bissau",
    "Gâmbia", "Banjul",
    "Gibraltar", "Gibraltar",
    "Granada", "Saint George's",
    "Guiana", "Georgetown",
    "Guiné", "Conacri",
    "Guiné-Bissau", "Bissau",
    "Haiti", "Porto Príncipe",
    "Honduras", "Tegucigalpa",
    "Hong Kong", "Cidade de Hong Kong",
    "Hungria", "Budapeste",
    "Iémen", "Sana",
    "Ilhas Marshall", "Majuro",
    "Ilhas Maurício", "Port Louis",
    "Ilhas Salomão", "Honiara",
    "Índia", "Nova Délhi",
    "Indonésia", "Jacarta",
    "Irã", "Teerã",
    "Iraque", "Bagdá",
    "Irlanda", "Dublin",
    "Islândia", "Reiquiavique",
    "Israel", "Jerusalém",
    "Itália", "Roma",  # Excluído conforme solicitado
    "Jamaica", "Kingston",
    "Jordânia", "Amã",
    "Kênia", "Nairóbi",
    "Kiribati", "Tarawa",
    "Kuwait", "Catar",
    "Laos", "Vientiane",
    "Lesoto", "Maseru",
    "Letônia", "Riga",
    "Libéria", "Monróvia",
    "Líbano","Beirute",
    "Lituânia", "Vílnius",
    "Luxemburgo", "Cidade de Luxemburgo",
    "Macedônia", "Skopje",
    "Madagascar", "Antananarivo",
    "Malásia", "Putrajaya (administrativa), Kuala Lumpur (legislativa)",
    "Maláui", "Lilongwe",
    "Maldivas", "Malé",
    "Mali", "Bamaco",
    "Malta", "Valeta",
    "Marrocos", "Rabat",
    "Maurício", "Port Louis",
    "Mauritânia", "Nuakchot",
    "México", "Cidade do México",
    "Mianmar", "Naypyidaw",
    "Micronésia", "Palikir",
    "Moçambique", "Maputo",
    "Namíbia", "Windhoek",
    "Nauru", "Yaren",
    "Nepal", "Catmandu",
    "Nicarágua", "Manágua",
    "Níger", "Niamey",
    "Nigéria", "Abuja",
    "Niue", "Alofi",
    "Noruega", "Oslo",
    "Nova Zelândia", "Wellington",
    "Omã", "Muscat",
    "Panamá", "Cidade do Panamá",
    "Papua Nova Guiné", "Port Moresby",
    "Paquistão", "Islamabad",
    "Paraguai", "Assunção",
    "Peru", "Lima",
    "Polônia", "Varsóvia",
    "Portugal", "Lisboa",
    "Quênia", "Nairóbi",
    "Quiribati", "Tarawa",
    "República Centro-Africana", "Bangui",
    "República Dominicana", "Santo Domingo",
    "República Tcheca", "Praga",
    "Romênia", "Bucareste",
    "Ruanda", "Kigali",
    "Rússia", "Moscou",
    "Saara Ocidental", "El Aiune",
    "Samoa", "Apia",
    "San Marino", "Cidade de San Marino",
    "Santa Lúcia", "Castries",
    "Senegal", "Dacar",
    "Serra Leoa", "Freetown",
    "Seychelles", "Vitória",
    "Singapura", "Singapura",
    "Somália", "Mogadíscio",
    "Sri Lanka", "Colombo (comercial), Sri Jayawardenepura Kotte (legislativa)",
    "Sudão"])   
print(country)