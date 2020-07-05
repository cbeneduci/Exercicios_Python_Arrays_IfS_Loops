# Faça um programa de bomba de posto de combustível, o valor da Gasolina é de R$ 4,58 e do Álcool R$ 3,50:
# O Operador da bomba deve escolher o tipo do Combustível G (gasolina) ou A (alcool) 
# e colocar a quantidade de litros, o nosso programa deve retornar qual o valor total 
# considerando os descontos abaixo:

# Álcool:
#   * Até 20 litros, desconto de 3% por litro.
#   * Acima de 20 litros, desconto de 5% por litro.
    
# Gasolina:
#   * Até 20 litros, desconto de 4% por litro.
#   * Acima de 20 litros, desconto de 6% por litro.


# pede para o usuário digitar o tipo do combustivel
tipo_combustivel = input('Por favor digite o tipo do combustivel G (Gasolina) ou A (Alcool): ')

# pede para o usuário digitar a quantidade de litros
litros = float(input('Por favor digite a quantidade de Litros: '))

# mapeia os valores de preço
precos = {'alcool' : 3.50, 'gasolina' : 4.58}

# valida se o combustivel digitado foi gasolina ou alcool
if tipo_combustivel.lower() == 'g':

    # valida a quantidade de litros digitada
    if litros <= 20:
        # cria a variável valor_total, multiplicando o valor de litros pelo preço e depois multiplicando por 0.97
        valor_total = (litros * precos['gasolina']) * 0.97

    else:
        valor_total = (litros * precos['gasolina']) * 0.95

elif tipo_combustivel.lower() == 'a':
    if litros <= 20:
        valor_total = (litros * precos['alcool']) * 0.97
    else:
        valor_total = (litros * precos['alcool']) * 0.95

# imprime o valor total na tela
print(f'Valor total a pagar {round(valor_total,2)}')