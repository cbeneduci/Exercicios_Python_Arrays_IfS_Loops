# Faça um programa para a leitura de três notas parciais de um aluno para cinco matérias. 
# O programa deve calcular a média alcançada por aluno e apresentar para cada matéria:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# Cria um array do tipo dict vazio
aluno = {}
# Cria uma key nome vazia
aluno['nome'] = ''
# Cria uma key notas com um array tipo dict vazio
aluno['notas'] = {}

# Cria um array de referencia para as matérias
materias = ['Português', 'Matematica', 'Biologia', 'Quimica', 'Inglês']

# Coloca o nome digitado pelo usuário na Key aluno do array dict
aluno['nome'] = input('Por favor digite o nome do Aluno: \n')

# Navega no array tipo list de matérias
for materia in materias:

    # Inicia a nota final do aluno com 0
    notafinal = 0
    
    # Inicia a variável de controle com 1
    quantidade_notas = 1

    # Executa o loop 3X (enquanto a quantidade de notas for menor que 4)
    while quantidade_notas < 4:

        # Armazena a nota digitada na variável nota
        nota = input(f'Por favor digite a {quantidade_notas} º nota de {materia} do aluno: ')

        # Soma a nota final com o valor coletado do usuário
        notafinal += float(nota)

        # Soma 1 a variável de controle quantidade_notas
        quantidade_notas +=1

    # divite o valor da notafinal por 3 para pegar a média do aluno
    notafinal = notafinal/3

    # adiciona no array dict de notas, uma nova key com o nome da materia e com o valor da nota final do aluno
    aluno['notas'][materia] = notafinal

print('='*60)

# mostra o nome do aluno
print(f'Notas de {aluno["nome"]} /n')

# navega no array de materias
for materia in materias:

    # valida a nota do aluno na materia que estamos navegando

    # se a nota for 10 mostra a mensagem de aprovado com distinção
    if aluno['notas'][materia] == 10:

        print(f'{materia}: {aluno["notas"][materia]} - Aprovado com Distinção')

    # se a nota for maior que 7 mostra a mensagem de aprovado
    elif aluno['notas'][materia] >= 7:
        
        print(f'{materia}: {aluno["notas"][materia]} - Aprovado')

    # se a nota qualquer outra coisa, mostra a mensagem de reprovado
    else:
        
        print(f'{materia}: {aluno["notas"][materia]} - Reprovado')

print('='*60)
