#Universidade Mogi das Cruzes
#Thais Pereira de Oliveira
#Estrutura Sequencial - Exercicios

#1
# print("oola mundo")

#2
# numero= int(input("digite um numero"))
# print("o numero digitado foi:", numero)

#3
# n1=int(input("digite o primeiro numero"))
# n2=int(input("digite o segundo numero"))
# soma=n1+n2
# print("a soma dos dois numero é igual a:", soma) 

#4
# print("calculo de nota bimestral")
# n1=int(input("digite a primeira nota"))
# n2=int(input("digite a segunda nota")) 
# n3=int(input("digite a terceira nota"))
# n4=int(input("digite a quarta nota"))
# soma=n1+n2+n3+n4
# media=soma/4
# print("a media é igual a", media)

#5
# print("conversão de metros para centimetros")
# metro=int(input("digite o valor em metros"))
# centimetro=metro*100
# print("o valor em centimetro é igual a:", centimetro)

#6
# print("CALCULANDO O RAIO E ÁREA DE UM CÍRCULO.")
# r = int(input("Digite o diâmetro do círculo: "))
# raio = r / 2
# print("O raio do círculo é igual a:", raio)
# area = raio ** 2 * 3.14
# print("A área do círculo é igual a:", area)

#7
# print("Cálculo da área de um quadrado, em seguida mostre o dobro desta área para o usuário")
# lado=int(input("digite o  valor do lado do quadrado"))
# area=lado**2
# dobro=area*2
# print("a area do quadrado é:", area )
# print(" o dobro da area é igual a:", dobro)

#8
# print("CALCULO SALARIAL")
# hora=float(input("digite quanto voce ganha por hora: "))
# numero=int(input("digite o numero de horas trabalhadas no mes:"))
# salario=hora*numero
# print("total do salario no mes:",salario)

#9
# print("Transforme tempertura em graus Fahrenheit para celsius")
# tem=int(input("digite a temperatura em graus fahrenheit: "))
# conversao=((tem-32) * (5/ 9))
# print("a temperatura fahrenheit em celsius é: ", conversao)

#10
# print("Transforme temperatura em Celsius para Fahrenheit")
# temp=int(input("digite a temperatura em graus Celsius:"))
# conversao=(temp*(9/5) + 32)
# print("a temperatura celsius em fahrenheit é: ", conversao)

#11
# print("calculo")
# n1=int(input("digite o primeiro numero:"))
# n2=int(input("digite o segundo numero:"))
# n3=float(input("digite um numeor real: "))
# produto=(n1*2) * (n2/2)
# soma=(n1*3)+n3
# cubo=n3*3
# print("O produto do dobro do primeiro com metade do segundo é:", produto)
# print("A soma do triplo do primeiro com o terceiro é:", soma)
# print("O terceiro número elevado ao cubo é:", cubo)

#12
# print("Peso Ideal")
# altura=float(input("digite sua altura:"))
# ideal=(72.7*altura) - 58
# print("seu peso ideal é", ideal)

#13
# print("Peso Ideal")
# mf=input("digite F para Feminino ou M para masculino:")
# altura= float(input("digite sua altura:"))
# ideal=(72.7*altura) - 58
# if mf == "F":
#    ideal=(72.7*altura) - 58 
#    print("o peso ideal é", ideal)
# elif mf=="M":
#    ideal=(62.1*altura) - 44.7
#    print("o peso ideal é", ideal)

#14
#print("Peso")
# ps=float(input("digite o peso dos peixes:"))
# if ps >+40:
#    excesso=ps-50
#    multa=excesso * 4.0
#    print(f" o peso está acima do regurlamento, voce deve pagar {multa}")

#15
print("Calculo Salarial")
salario=float(input("Digite o valor que voce ganha por hora:"))
horas=float(input("Digite as horas trabalhadas"))
salariobruto=salario*horas
ir=salariobruto*0.11
inss=salariobruto*0.08
sindicato=salariobruto*0.05
totaldesconto= inss+sindicato+ir
salarioliquido= totaldesconto-salariobruto
print(f"+ Salário Bruto : R$ {salariobruto:.2f}")
print(f"- IR (11%) : R$ {ir:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
print(f"= Salário Líquido : R$ {salarioliquido:.2f}")

