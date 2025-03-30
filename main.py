"""'''PRIMEIRA'''
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")

'''SEGUNDA'''
numero = float(input("Digite um número: "))

if numero > 10:
    print(f"O número {numero} é maior que 10")
else:
    print(f"O número {numero} é menor que 10")


'''TERCEIRA'''
idade = int(input("Digite sua idade"))

if idade >= 18:
    print("Você é de maior")
else:
    print("Você é de menor")

'''QUARTA'''
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Voto é obrigatório.")
elif idade == 16 or idade >= 70:
    print("Voto opcional.")
else:
    print("Não tem voto.")

'''QUINTA'''
numero = float(input("Digite um número"))

if numero == 0:
    print("O número é zero")
elif numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"o número {numero} é negativo")


'''SEXTA'''
nota = float(input("Digite o valor da nota: "))

if nota >= 9:
    print('Nota A')
elif nota == 7 or nota == 8:
    print('Nota B')
elif nota == 5 or nota == 6:
    print('Nota C')
elif nota == 3 or nota == 4:
    print('Nota D')
elif nota < 2:
    print('Nota E')


'''SÉTIMA'''

idade = int(input("Digite sua idade: "))

if idade <= 12 or idade >= 60:
    print("Tem direito a desconto.")
else:
    print("Não tem direito de desconto.")


'''OITAVA'''

l1 = int(input("Digite o primeiro lado: "))
l2 = int(input("Digite o segundo lado: "))
l3 = int(input("Digite o terceiro lado: "))

if l1 + l2 > l3 or l1 + l3 > l2 or l2 + l3 > l1:
    if l1 == l2 == l3:
        print("O trinâgulo é equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O trinâgulo é isóceles.")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("O triângulo é escaleno")
else:
    print("Não é um triângulo")


'''NONA'''
valorT = float(input("Digite o valor total da compra: "))

if valorT < 100:
    desconto = (valorT * 5) / 100
    valorT = valorT - desconto
    print(f"O valor a se pagar é R$: {valorT}")
elif valorT >= 100 or valorT <= 500:
    desconto = (valorT * 10) / 100
    valorT = valorT - desconto
    print(f"O valor a se pagar é R$: {valorT}")
elif valorT > 500:
    desconto = (valorT * 15) / 100
    valorT = valorT - desconto
    print(f"O valor a se pagar é R$: {valorT}")


'''DÉCIMA'''

ano = int(input("Digite o ano: "))

if ano % 4 == 0 and ano % 100 != 0:
    print("Ano é bissexto")
elif ano % 100 == 0 and ano % 400 == 0:
    print("Ano é bissexto")
else:
    print("Ano não é bissexto")

'''DÉCIMA PRIMEIRA'''

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)

if imc >= 30:
    print("Obesidade")
elif imc >= 25 and imc <= 24.9:
    print("Sobrepeso")
elif imc > 18.5 and imc < 24.9:
    print("Peso normal")
elif imc <= 18.5:
    print("Abaixo do peso")

'''DÉCIMA SEGUNDA'''

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if n1 < n2 < n3:
    print("Estão em ordem crescente")
elif n1 > n2 > n3:
    print("Estão em ordem decrescente")
elif n1 == n2 == n3:
    print("Os números são iguais")

'''DÉCIMA TERCEIRA'''
temp = float(input("Digite a temperatura: "))

if temp > 40:
    print("Muito Quente")
elif temp > 25 and temp <= 40:
    print("Quente")
elif temp > 10 and temp <= 25:
    print("Aconchegante")
elif temp <= 10:
    print("Frio")"""

'''DÉCIMA QUARTA'''

from datetime import datetime

data_hoje = hoje.strftime('%d/%m/%y')  # Descobrindo a data atual para

input_data_limite = input('DATA LIMITE: ') # Entrando com a data limite

data_limite = datetime.strftime(input_data_limite, '%d/%m/%y') # deveria


print(data_limite) 