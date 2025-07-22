print("3º exercício, parte 1 - aula 2\n")

HA = float(input("digite o valor recebido por hora/aula (HA): R$ "))
HT = float(input("digite o total de horas trabalhadas no mês (HT): "))
d = float(input("digite a % de desconto do INSS: "))


salario_bruto = HA * HT
inss = salario_bruto * (d / 100)
salario_liquido = salario_bruto - inss

print("\nresumão do salário:")
print(f"salário bruto: R$ {salario_bruto:.2f}")
print(f"desconto do INSS ({d}%): R$ {inss:.2f}")
print(f"salário líquido: R$ {salario_liquido:.2f}")
