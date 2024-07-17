#Universidade Mogi das Cruzes
#Thais Pereira de Oliveira
#Estrutura de Decisão - Exercicios

#1 Faça um Programa que peça dois números e imprima o maior dele
# n1=float(input("digite um numero"))
# n2=float(input("digite outro numero"))
# if n1>n2:
#   print(n1)
# else:
#   print(n2)
   
#2Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# numero=float(input("digite um numero"))
# if numero<0:
#     print("esse numero é negativo")
# elif numero>0:
#   print("esse numero é positivo")

#3Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# letra = input("Digite uma letra: ")
# if letra == "F": 
#     print("Sexo feminino")
# elif letra == "M":
#     print("Sexo masculino")
# else:
#     print("Sexo Inválido")

#4Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# letra = input("Digite uma letra: ")
# if letra in ['a','e','i','o','u']: 
#     print("Essa letra é vogal")
# else:
#     print("Essa letra é consoante")

#5Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# m1=int(input("digite a primeira nota"))
# m2=int(input("digite a segunda nota"))
# soma = m1+m2
# media = soma/2
# if media >= 7 and media > 10:
#     print("aprovado")
# elif media < 7:
#     print("reprovado")
# elif media == 10:
#     print("aprovado com distinção")

#6 Faça um Programa que leia três números e mostre o maior deles.
# n1=int(input("digite o primeiro numero"))
# n2=int(input("digite o segundo numero"))
# n3=int(input("digite o terceiro numero"))
# if n1>=n2 and n1>=n3:
#     maior=n1
# if n2>=n1 and n2>=n3:
#     maior=n2
# else:
#     maior=n3
# print("o maior numero é:", maior)
    
#7Faça um Programa que leia três números e mostre o maior e o menor deles.
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))

# if n1 <= n2 and n1 <= n3:
#     menor = n1
# elif n2 <= n1 and n2 <= n3:
#     menor = n2
# else:
#     menor = n3

# if n1>=n2 and n1>=n3:
#     maior=n1
# if n2>=n1 and n2>=n3:
#     maior=n2
# else:
#     maior=n3

# print("o maior numero é:", maior)
# print("O menor número é:", menor)

# 8Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# prod1 = int(input("Digite o valor do primeiro produto: "))
# prod2 = int(input("Digite o valor do segundo produto: "))
# prod3 = int(input("Digite o valor do terceiro produto: "))

# if prod1 < prod2 and prod1 < prod3:
#     produto_mais_barato = prod1
#     menor_preco = prod1
# elif prod2 < prod1 and prod2 < prod3:
#     produto_mais_barato = prod2
#     menor_preco = prod2
# else:
#     produto_mais_barato = prod3
#     menor_preco = prod3

# print(f"Você deve comprar o produto {produto_mais_barato}, que custa R${menor_preco}")

#9
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))
# if num1 >= num2 >= num3:
#     ordem = (num1, num2, num3)
# elif num1 >= num3 >= num2:
#     ordem = (num1, num3, num2)
# elif num2 >= num1 >= num3:
#     ordem = (num2, num1, num3)
# elif num2 >= num3 >= num1:
#     ordem = (num2, num3, num1)
# elif num3 >= num1 >= num2:
#     ordem = (num3, num1, num2)
# else:
#     ordem = (num3, num2, num1)

# print("Os números em ordem decrescente são:", ordem)

#10
# print("Qual turno você estuda?")
# opção=input("""digite o periodo que você estuda:
#           M- Matutino
#           V- Vespertino
#           N- Noturno
#           :""")
# if opção=='M':
#     print("bom dia!")
# elif opção=='V':
#     print("boa tarde!")
# elif opção=='N':
#     print("boa noite!")

#11
# print("Organização Tabajara - AUMENTO SALARIAL")
# salario = float(input("Digite seu salário: "))
# if salario == 280.00:
#     aumento_percentual = 20
#     aumento = salario * 0.20
#     novosalario = salario + aumento
# elif 280.00 <= salario <= 700.00:
#     aumento_percentual = 15
#     aumento = salario * 0.15
#     novosalario = salario + aumento
# elif 700.00 <= salario <= 1500.00:
#     aumento_percentual = 10
#     aumento = salario * 0.10
#     novosalario = salario + aumento
# elif salario >= 1500.00:
#     aumento_percentual = 5
#     aumento = salario * 0.05
#     novosalario = salario + aumento

# print("Salário antes do reajuste:", salario)
# print("Percentual do aumento aplicado:", aumento_percentual, "%")
# print("Aumento:", aumento)
# print("Novo salário:", novosalario)

#12
# print("FOLHA DE PAGAMENTO")
# valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
# horas_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# salario_bruto = valor_hora * horas_mes
# fgts = salario_bruto * 0.11  

# if salario_bruto <= 900.00:
#     ir = 0 
#     inss = salario_bruto * 0.03  
# elif salario_bruto <= 1500.00:
#     ir = salario_bruto * 0.05  
#     inss = salario_bruto * 0.10  
# elif salario_bruto <= 2500.00:
#     ir = salario_bruto * 0.10  
#     inss = salario_bruto * 0.10  
#     ir = salario_bruto * 0.20  
#     inss = salario_bruto * 0.10  

# total_descontos = ir + inss
# salario_liquido = salario_bruto - total_descontos
# print(f"Salário Bruto: ({valor_hora} * {horas_mes}): R$ {salario_bruto:.2f}")
# print(f"(-) IR ({ir * 100 / salario_bruto:.0f}%): R$ {ir:.2f}")
# print(f"(-) INSS (10%): R$ {inss:.2f}")
# print(f"FGTS (11%): R$ {fgts:.2f}")
# print(f"Total de descontos: R$ {total_descontos:.2f}")
# print(f"Salário Líquido: R$ {salario_liquido:.2f}")

#13
# print("dias da semana")
# dia = int(input("Digite um número: "))

# if dia not in [1, 2, 3, 4, 5, 6, 7]:
#     print("Opção inválida")
# elif dia == 1:
#     print("Segunda-Feira")
# elif dia == 2:
#     print("Terça-Feira")
# elif dia == 3:
#     print("Quarta-Feira")
# elif dia == 4:
#     print("Quinta-Feira")
# elif dia == 5:
#     print("Sexta-Feira")
# elif dia == 6:
#     print("Sábado")
# elif dia == 7:
#     print("Domingo")

#14
# print("Media")
# n1=int(input("Digite a primeira nota:"))
# n2=int(input("Digite a segunda nota:"))
# media=(n1+n2)/2
# if 9 <= media <=10:
#     conceito="A"
#     status="Aprovado"
# elif 7.5 <= media <=9:
#      conceito="B"
#      status="Aprovado"
# elif 6 <= media <= 7.5:
#     conceito="C"
#     status="Aprovado"
# elif 4 <= media <= 6:
#     conceito="D"
#     status="Reprovado"
# elif 4 <= 0:
#     conceito="E"
#     status="Reprovado"

# print(f"Notas:{n1},{n2}")
# print(f"Media semestral:{media:.2f}")
# print("Conceito", conceito)
# print("Status:", status)

#15
# ("Trinagulo")
# lado1=int(input("digite o valor do primeiro lado:"))
# lado2=int(input("digite o valor do segundo lado:"))
# lado3=int(input("digite o valor do terceiro lado:"))
# if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
#   if lado1==lado2==lado3:
#     print("Triângulo Equilátero: três lados iguais.")
#   elif lado1==lado2 or lado1==lado3 or lado2==lado3:
#     print("Triângulo Isósceles: quaisquer dois lados iguais.")
#   else:
#     print("Triângulo Escaleno: três lados diferentes.")
# else:
#     print("Os valores fornecidos não formam um triângulo.")

#16
# print("Equação Segundo Grau")
# valorA = int(input("Digite o primeiro valor: "))
# valorB = int(input("Digite o segundo valor: "))
# valorC = int(input("Digite o terceiro valor: "))

# if valorA + valorB > valorC and valorA + valorC > valorB and valorB + valorC > valorA:
#     if valorA == valorB == valorC:
#         print("Equilátero")
#     elif valorA == valorB or valorB == valorC or valorA == valorC:
#         print("Isósceles")
#     else:
#         print("Escaleno")
# else:
#     print("Não é um triângulo")

#17
# print("Ano Bissexto")
# ano=int(input("Digite um ano"))
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print(f"O ano {ano} é bissexto.")
# else:
#     print(f"O ano {ano} não é bissexto.")
    
#18 
# data = input("Digite uma data no formato dd/mm/aaaa: ")

# if len(data) == 10 and data[2] == '/' and data[5] == '/':
#     dia, mes, ano = data.split('/')
    
    
#     if dia.isdigit() and mes.isdigit() and ano.isdigit():
#         dia = int(dia)
#         mes = int(mes)
#         ano = int(ano)
        
    
#         if 1 <= mes <= 12:

#             if dia > 0:
     
#                 dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                
#                 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#                     dias_no_mes[1] = 29

#                 if dia <= dias_no_mes[mes - 1]:
#                     print("A data é válida.")
#                 else:
#                     print("A data não é válida.")
