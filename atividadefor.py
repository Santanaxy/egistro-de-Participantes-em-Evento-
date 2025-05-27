total_participantes = 0 
maior_participantes = 0 

for dia in range(1, 6):
    participantes_dia = int(input(f"Digite numero de participante do dia {dia} :"))
    print(f"Dia {dia} total de participantes {participantes_dia}: ")
    total_participantes += participantes_dia
    print(total_participantes)

    if participantes_dia > maior_participantes:
        maior_participantes = participantes_dia
        print(f"o maior numero de participantes em um único dia é: {maior_participantes}")
        print(f"a maior parte media do dia é: {total_participantes / 5 }")