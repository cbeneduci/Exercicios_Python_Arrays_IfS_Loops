# Faça um programa para receber as informações de atletas em uma competição de salto em distância e 
# informar quais são os 3 primeiros lugares respeitando as condições abaixo:

#   * Cada atleta deve fazer 5 saltos
#   * O Resultado do atleta será calculado pela média dos seus saltos.
  
# Depois de cadastrar o nome de todos os atletas e contabilizar os saltos de cada um deles, 
# imprima na tela o nome do atleta, o valor de cada um dos cinco saltos, a média dele e a posição dele.
# 
#  **Importante**, essa impressão deve ser em ordem crescente como um ranking de posições.

# importa o modulo operator que vamos utilizar para ordenar o array
from operator import itemgetter

# define um array de atletas do tipo list vazio
atletas = []

# cria um loop infinito
while True:

    # Pede para o usuário digitar o nome do atleta e salva como nome do atleta
    nome_atleta = input('Por favor digite o nome do Atleta: ')

    # caso o nome do atleta venha em branco quebra o loop entendendo que acabaram os cadastros
    if nome_atleta == '':
        break

    # Cria um array de saltos do tipo list vazio
    saltos = []

    # Cria uma variável de controle de qual salto está sendo executado
    salto = 1

    # Roda o código 5 vezes, uma para cada salto
    while salto <= 5:

        # adiciona no array de saltos o valor do salto digitado pelo usuário
        saltos.append(float(input(f'Por favor digite a distancia do {salto}º salto em metros: ')))
        
        # soma 1 ao valor da variavel de controle salto
        salto +=1

    # adiciona o array de atletas um novo array tipo dict com o nome do atleta e os saltos dele.    
    atletas.append({'nome' : nome_atleta,
                    'saltos' : saltos})


# navega no array de atletas
for atleta in atletas:

    # cria uma nova key no array de atletas chamada media
    # adiciona nessa key a soma dos valores do salto do atleta dividido por 5
    atleta['media'] = sum(atleta['saltos'])/5

# cria um array do ranking fazendo um sort(ordenando) o array de atletas
# o primeiro parametro da funcao sorted é o nome do array que queremos ordenar
# o segundo parametro é a chave do array que queremos usar para ordena-lo
# o terceiro parametro fala que devemos ordena-lo em forma decrescente
ranking = sorted(atletas, key=itemgetter('media'), reverse=True) 

# cria uma variável de controle para a posição do ranking
posicao = 1

print('\n\n')

print('='*80)

# navega no ranking de atletas
for atleta in ranking:

    # faz um print na tela com o nome do atleta, os saltos dele e a posição no ranking usando a variável de controle
    print(f'Nome: {atleta["nome"]}, saltos: {atleta["saltos"]}, Posição no ranking: {posicao}')

    # soma 1 a variável de controle
    posicao +=1

print('='*80)


