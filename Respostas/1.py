# Faça um Programa que leia três números armazene em um array, 
# em um print mostre mostre o maior deles e em outro todos os 
# valores ordenados de forma decrescente.

import os

# Limpa a tela (Para windows pode ser necessário alterar de clear para cls)
os.system('clear')

# Declarado array do tipo List para armazenar o valor dos números
numeros = []

# Variável de controle para 3 tentativas
controle = 3

# Enquanto a variável for maior que 0 roda o código dentro do while
while controle > 0:
    
    # Pede para o usuário digitar um número e adiciona ao array
    numeros.append(input('digite um número: '))
    
    # Subtrai 1 da variável de controle
    controle -=1

    # Limpa a tela (Para windows pode ser necessário alterar de clear para cls)
    os.system('clear')

# Ordena a lista de forma decrescente utilizando o parametro reverse=true
numeros.sort(reverse=True)

# Informa o maior número da lista, que está na posição 0 depois de ordenada
print(f'O Maior número é o {numeros[0]} \n')

print('Lista decrescente: ')

# Navega na lista fazendo um print de todos os números
for numero in numeros:
    print(numero)
