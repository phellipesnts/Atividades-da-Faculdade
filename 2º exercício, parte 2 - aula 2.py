print("2º exercício, parte 2 - aula 2\n")

def dias_no_mes(mes):
    if mes == 2:
        return 28
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return "oxe esse mês não existe não, vai ver o calendário >:("

mes = int(input("digite o número do mês: "))
print("dias no mês:", dias_no_mes(mes))
