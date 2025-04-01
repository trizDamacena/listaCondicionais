'''PRIMEIRA'''
print("PRIMEIRA")
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")


'''SEGUNDA'''
print("\nSEGUNDA")
numero = float(input("Digite um número: "))

if numero > 10:
    print(f"O número {numero} é maior que 10")
elif numero < 10:
    print(f"O número {numero} é menor que 10")
else:
    print(f"O número {numero} é igual a 10")


'''TERCEIRA'''
print("\nTERCEIRA")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é de maior")
else:
    print("Você é de menor")

'''QUARTA'''
print("\nQUARTA")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Voto é obrigatório.")
elif idade >=16 and idade < 18 or idade >= 70:
    print("Voto opcional.")
else:
    print("Não tem voto.")

'''QUINTA'''
print("\nQUINTA")
numero = float(input("Digite um número: "))

if numero == 0:
    print("O número é zero")
elif numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"o número {numero} é negativo")


'''SEXTA'''
print("\nSEXTA")
nota = int(input("Digite o valor da nota: "))

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
print("\nSÉTIMA")
idade = int(input("Digite sua idade: "))

if idade <= 12 or idade >= 60:
    print("Tem direito a desconto.")
else:
    print("Não tem direito de desconto.")


'''OITAVA'''
print("\nOITAVA")
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
print("\nNONA")
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
print("\nDÉCIMA")
ano = int(input("Digite o ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print("Ano é bissexto")

else:
    print("Ano não é bissexto")


'''DÉCIMA PRIMEIRA'''
print("\nDÉCIMA PRIMEIRA")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)

if imc >= 30:
    print("Obesidade")
elif imc >= 25 and imc <= 24.9:
    print("Sobrepeso")
elif imc >= 18.5 and imc < 24.9:
    print("Peso normal")
elif imc < 18.5:
    print("Abaixo do peso")


'''DÉCIMA SEGUNDA'''
print("\nDÉCIMA SEGUNDA")
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
print("\nDÉCIMA TERCEIRA")
temp = float(input("Digite a temperatura: "))

if temp >= 40:
    print("Muito Quente")
elif temp >= 25 and temp < 40:
    print("Quente")
elif temp >= 10 and temp < 25:
    print("Aconchegante")
elif temp < 10:
    print("Frio")

'''DÉCIMA QUARTA'''
print("\nDÉCIMA QUARTA")
from datetime import datetime

data = input("Digite a data: ")

data = datetime.strptime(data, '%d/%m/%Y').date()
print(data)


'''DÉCIMA QUINTA'''
print("\nDÉCIMA QUINTA")
import re
senha = input("Digite a senha: ")
tamanho = len(senha)

'''print (re.findall('[A-Z]', senha))
print( re.findall('[a-z]', senha))
print( re.findall('\W', senha))
'''
if tamanho >= 8:
    if re.findall('[A-Z]', senha):
        if re.findall('[a-z]', senha):
            if re.findall('\W', senha):
                if re.findall('\d', senha):
                    print("A senha atende todos os critérios")
                else:
                    print("A senha não contém um número")
            else:
                print("A senha não contém caracter especial")
        else:
            print("A senha não contém letra minuscula")
    else:
        print("A senha não contém letra maiuscula")
else:
    print("Senha do tamanho errado")


'''DÉCIMA SEXTA'''
print("\nDÉCIMA SEXTA")
import math
num_raiz = int(input("Digite o número: "))

if num_raiz < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo")
elif num_raiz > 100:
    print("Nùmero muito grande, reduza para um valor abaixo de 100")
else:
    raiz = math.sqrt(num_raiz)
    print(f"A raíz quadrada é {raiz:.2f}")


'''DÉCIMA SÉTIMA'''
print("\nDÉCIMA SÉTIMA")

data = input("Digite a data: ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])


if ano % 4 == 0 and ano % 100 != 0:

    if mes <= 12  and mes >= 1:
        if mes == 2 and dia <= 29:
            print("Válida")
            print(ano, mes, dia, sep='-')
        elif mes == 1 or 3 or 5 or 7 or 8 or 10 or 12 and dia <=31:
            print("Válida")
            print(ano, mes, dia, sep='-')
        elif mes == 4 or 6 or 8 or 9 or 11 and dia <= 30:
            print("Válida")
            print(ano, mes, dia, sep='-')
        else:
            print("Inválida por total de dias")
    else:
        print("Mês incorreto")
elif ano % 400 == 0:
    if mes <= 12 and mes >= 1:
        if mes == 2 and dia <= 29:
            print("Válida")
            print(ano, mes, dia, sep='-')
        elif mes == 1 or mes== 3 or mes== 5 or mes== 7 or mes== 8 or mes== 10 or mes== 12 and dia <=31:
            print("Válida")
            print(ano, mes, dia, sep='-')
        elif mes == 4 or mes== 6 or mes== 8 or mes== 9 or mes== 11 and dia <= 30:
            print("Válida")
            print(ano, mes, dia, sep='-')
        else:
            print("Inválida por total de dias")
    else:
        print("Mês incorreto")
else:
    if mes <= 12 and mes >= 1 :
        if mes == 2 and dia <= 28:
            print("Válida")
            print(ano, mes, dia, sep='-')
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia <= 31:
             print("Válida")
             print(ano, mes, dia, sep='-')
        elif mes == 4 or mes == 6 or mes == 8 or mes == 9 or mes == 11 and dia <= 30:
            print("Válida")
            print(ano, mes, dia, sep='-')
        else:
            print("Inválida por total de dias")
    else:
        print("Mês incorreto")


"""DÉCIMA OITAVA"""
print("\nDÉCIMA OITAVA")
expressao = input("Digite a expressão")
expressao = eval(expressao)
print(expressao)


"""DESAFIO"""
print("\nDESAFIO")
import re

cpf = input("Digite o CPF: ")
padrao = r"\d{3}.\d{3}.\d{3}-\d{2}"
resultado = re.search(padrao, cpf)

if resultado or len(cpf) == 11:

    if len(cpf) == 11:
        cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])


    v0 = int(cpf[0])
    v1 = int(cpf[1])
    v2 = int(cpf[2])
    v3 = int(cpf[4])
    v4 = int(cpf[5])
    v5 = int(cpf[6])
    v6 = int(cpf[8])
    v7 = int(cpf[9])
    v8 = int(cpf[10])
    v10 = int(cpf[12])
    v11 = int(cpf[13])

    primeiro  = (v0 * 10) + (v1* 9) + (v2*8) + (v3*7)+ (v4*6)+(v5*5)+(v6*4)+(v7*3)+(v8*2) #soma dos numero
    segundo = (v0*11)+(v1*10)+(v2*9) + (v3*8)+ (v4*7)+(v5*6)+(v6*5)+(v7*4)+(v8*3)+(v10*2)

    div1 = primeiro % 11
    div2 = segundo % 11

    verificador1 = 11 - div1
    verificador2 = 11 - div2

    if div1 > 2 and verificador1 == v10:
        if div2 > 2 and verificador2 == v11:
            print("CPF VÁLIDO")
        elif div2 < 2 and verificador2 == 11:
            print("CPF VÁLIDO")
        else:
            print("CPF NÃO É VÁLIDO")

    elif div1 < 2 and verificador1 == 11:
        if div2 > 2 and verificador2 == v11:
            print("CPF VÁLIDO")
        elif div2 < 2 and verificador2 == 11:
            print("CPF VÁLIDO")
        else:
            print("CPF NÃO É VÁLIDO")
    else:
        print("CPF NÃO É VÁLIDO")

else:
    print("O CPF NÃO ESTÁ CORRETO")
