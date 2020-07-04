# Nosso time foi contratado por uma empresa para fazer um sistema de pagamento de salários, 
# esse sistema deve receber o salario atual de um colaborador 
# e calcular o reajuste dele para o próximo salário:

# Seguem os criterios para o reajuste:
# * Salários até R$ 280,00 (incluindo) : aumento de 20%
# * Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# * Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# * Salários de R$ 1500,00 em diante : aumento de 5% 

# Assim que calcularmos o aumento, devemos informar na tela os dados abaixo:

# * salário antes do reajuste
# * percentual de aumento aplicado
# * valor do aumento
# * novo salário, após o aumento

# Armazena o nome do funcionário na variável nome
nome = input('Por favor digite o nome do funcionário: ')

# Armazena o valor do salário do funcionário já como float
salario = float(input('Por favor digite o salario atual do {nome}: '))

# valida o valor do salário do usuário

#se o salario for até 280
if salario <= 280:

    # coloca na variável salario_novo o valor do salário X 1.2 assim temos o salario 20% maior
    salario_novo = salario * 1.2
    # adiciona na variavel percentual, qual percentual utilizamos
    percentual = 20

# se o salário for até 700, como temos um IF antes validando se o salário vai até 280,
# não precisamos fazer um salario >280 and salario <= 700, por que para chegar nesse elif 
# o salário precisa ser maior já que o 280

elif salario <= 700:
    salario_novo = salario * 1.15
    percentual = 15

# se o salario for até 1500
elif salario <= 1500:
    salario_novo = salario * 1.1
    percentual = 10

# se o salário não for nenhuma das outras opções, ou seja maior que 1500
else:
    salario_novo = salario * 1.05
    percentual = 5


# Print das informações de salário para o usuário

print('=' * 60)

print(f'Informações de salário de {nome}')
print(f'Salario antes do reajuste: {salario}')
print(f'Percentual de aumento aplicado: {percentual}%')
print(f'Valor do aumento: {salario_novo - salario}')
print(f'Salário após o aumento: {salario_novo}')

print('=' * 60)