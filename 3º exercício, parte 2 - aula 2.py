print("3º exercício, parte 2 - aula 2\n")

def ordenar_tres_numeros(a, b, c):
    return sorted([a, b, c])

a = int(input("digite o primeiro número: "))
b = int(input("digite o segundo número: "))
c = int(input("digite o terceiro número: "))

ordenados = ordenar_tres_numeros(a, b, c)
print("números em ordem crescente:", ordenados)
