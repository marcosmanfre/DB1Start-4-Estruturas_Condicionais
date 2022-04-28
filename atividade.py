#Faça um Programa que peça dois números e imprima o maior deles. 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
maior = n1
if n2 > n1:
    maior = n2
print("O maior número digitado foi {}".format(maior))

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
numero = int(input("Digite um número: "))
if numero >= 0:
    print("O número digitado é positivo")
else:
    print("O número digitado é negativo")

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
letra = str(input("Digite uma letra: ")).upper()
if letra == "M":
    print("M - Masculino")
elif letra == "F":
    print("F - Feminino")
else:
    print("Sexo Inválido")

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
letra = input("Digite uma letra: ")
vogal = 'aeiou'
numeros = '0123456789'
if letra in vogal or letra in vogal.upper():
    print("A letra digitada é uma Vogal!!!")
elif letra in numeros or letra in numeros.upper():
    print("Erro! digite uma letra")        
else:
    print("A letra digitada é uma Consoate")

#Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada pelo aluno e apresentar:"
#A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
#A mensagem “Reprovado”, se a média for menor do que sete;
#A mensagem “Aprovado com Distinção”, se a média for igual a dez.”
notaParcial1 = float(input("Digite a nota: "))
notaParcial2 = float(input("Digite a nota: "))
media = (notaParcial1 + notaParcial2) / 2
if media >= 7 and media < 10:
    print("Aprovado! a sua média foi {} ".format(media))
elif media < 7:
    print("Reprovado! a sua média foi {} ".format(media))
elif media == 10:
    print("Aprovado com Distinção! a sua média foi {} Parabéns! ".format(media))

#Faça um Programa que leia três números e mostre o maior e o menor deles. 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print("O menor número digitado foi {}.".format(menor))
print("O maior número digitado foi {}.".format(maior))

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 
produto1 = int(input("Digite o valor primeiro produto: "))
produto2 = int(input("Digite o valor segundo produto: "))
produto3 = int(input("Digite o valor terceiro produto: "))

if produto1 < produto2:
    if produto1 < produto3:
        print("Você deve comprar o Primeiro Produto!")
    else:
        print("Você deve comprar o Terceiro Produto")

else:
    if produto2 < produto3:
        print("Você deve comprar o Segundo Produto!")
    else:
        print("Você deve comprar o Terceiro Produto!")

#Faça um Programa que leia três números e mostre-os em ordem decrescente. 
primeiroNumero = int(input("Primeiro número: "))
segundoNumero = int(input("Segundo número: "))
terceiroNumero = int(input("Terceiro número: "))

if primeiroNumero < terceiroNumero:
    primeiroNumero, terceiroNumero = terceiroNumero, primeiroNumero

if primeiroNumero < segundoNumero:
    primeiroNumero, segundoNumero = segundoNumero, primeiroNumero

if segundoNumero < terceiroNumero:
    segundoNumero, terceiroNumero = terceiroNumero, segundoNumero

print("A ordem decrescente é {}, {}, {}".format(primeiroNumero)(segundoNumero)(terceiroNumero))    

#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-Matutino ou V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa #Noite!" ou "Valor Inválido!", conforme o caso
print('''Turnos cadastrados:
M - Matutino.
V - Vespertino.
N - Noturno.            ''')

turno = input("Informe o turno que você estuda: ").upper()
if turno == 'M':
    print("Bom dia! ")
elif turno == 'V':
    print("Boa tarde! ")
elif turno == 'N':
    print("Boa noite! ")
else:
    print("Valor Inválido! ")

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R280,00eR 700,00 : aumento de 15%
# salários entre R700,00eR 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    percentual = 20 / 100
elif salario > 280 and salario <= 700:
    percentual = 15 / 100
elif salario > 700 and salario <= 1500:
    percentual = 10 / 100
else:
    percentual = 5 / 100

novoSalario = salario + (salario * percentual)
valorAumento = novoSalario - salario

print('''
Salário antes do reajuste: {:.2f}
Percentual de aumento aplicado: {:.2%} 
Valor do aumento: {:.2f}
Novo salário: {:.2f}
'''.format(salario, percentual, valorAumento, novoSalario))

#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.#
# Desconto do IR:
# Salário Bruto até 900 (inclusive) – isento
# Salário Bruto até 1500 (inclusive) – desconto de 5%
# Salário Bruto até 2500 (inclusive) – desconto de 10%
# Salário Bruto acima de 2500 – desconto de 20% Imprima na tela as informações
valorHora = float(input("Digite o valor da sua hora trabalhada: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salarioBruto = valorHora * horasTrabalhadas
fgts = (salarioBruto * 11) / 100
sindicato = (salarioBruto * 3) / 100

if salarioBruto <= 900:
    salarioLiquido = salarioBruto - sindicato
    
elif salarioBruto > 900 and salarioBruto <= 1500:
    impostoRenda = (salarioBruto * 5) / 100
    salarioLiquido = salarioBruto - impostoRenda - sindicato

elif salarioBruto > 1500 and salarioBruto <= 2500:
    impostoRenda = (salarioBruto * 10) / 100
    salarioLiquido = salarioBruto - impostoRenda - sindicato

else:
    impostoRenda = (salarioBruto * 20) / 100
    salarioLiquido = salarioBruto - impostoRenda - sindicato

print('''
O seu salário bruto é: {:.2f}
O valor do FGTS é: {:.2f} 
O desconto do Sindicato é: {:.2f}
O desconto do Imposto de Renda é: {:.2f}
O seu salário liquido é: {:.2f}
'''.format(salarioBruto, fgts, sindicato, impostoRenda, salarioLiquido))

#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 
diaSemana = input("Digite um número para a semana: ")

if diaSemana == '1':
    print("1-Domingo")
elif diaSemana == '2':
    print("2-Segunda")
elif diaSemana == '3':
    print("3-Terça")
elif diaSemana == '4':
    print("4-Quarta")
elif diaSemana == '5':
    print("5-Quinta")
elif diaSemana == '6':
    print("6-Sexta")
elif diaSemana == '7':
    print("7-Sabado")
else:
    print("Valor inválido! Tente novamente")

#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: Média de Aproveitamento Conceito Entre 9.0 e 10.0 A Entre 7.5 e 9.0 B Entre 6.0 e 7.5 C Entre 4.0 e 6.0 D Entre 4.0 e zero
# E O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
notaParcial1 = float(input("Digite a primeira nota: "))
notaParcial2 = float(input("Digite a segunda nota: "))
media = (notaParcial1 + notaParcial2) / 2

if media >= 9 and media <= 10:
    conceito = "A"
    mensagem = "Aprovado"
elif media < 9 and media >= 7.5:
    conceito = "B"
    mensagem = "Aprovado"
elif media < 7.5 and media >= 6:
    conceito = "C"
    mensagem = "Aprovado"
elif media < 6 and media >= 4:
    conceito = "D"
    mensagem = "Reprovado"
else:
    conceito = "E"
    mensagem = "Reprovado"

print('''
Primeira nota: {:.1f}
Segunda nota: {:.1f}
Media: {:.1f}
Conceito: {}
Mensagem: {}
'''.format(notaParcial1, notaParcial2, media, conceito, mensagem))

#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os valores informados podem formar um Triângulo ", end="")
    if lado1 == lado2 == lado3:
        print("Equilátero!")
    elif lado1 != lado2 != lado3 != lado1:
        print("Escaleno!")
    else:
        print("Isósceles!")
else:
    print("Os valores informados NÃO podem formar um Triângulo! ")

#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
print("O valor de delta é: ", delta)
x1 = (-b - delta**0.5) / (2*a)
x2 = (-b + delta**0.5) / (2*a)
print("O valor de x1 é: ", x1)
print("O valor de x2 é: ", x2)

#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 
ano = int(input("Qual ano gostaria de consultar? "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é Bissexto! ".format(ano))
else:
    print("O ano {} não é Bissexto!". format(ano))

#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))

valida = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 9 or mes == 10 or mes == 11 or mes == 12:
    if dia <= 31:
        valida = True

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        valida = True

elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if dia <= 29:
            valida = True
    elif dia <= 28:
        valida = True

if valida:
    print("Data Válida!")
    print("Você digitou a data: {}/{}/{}".format(dia, mes, ano))
else:
    print("Data Inválida!")

#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

numero = int(input("Informe um número: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10

if numero >0 and numero < 1000:
    print("O número digitado foi {}.".format(numero))
    print("Unidade: {}".format(unidade))
    print("Dezena: {}".format(dezena))
    print("Centena: {}".format(centena))
else:
    print("Digite um número inteiro menor que 1000! ")