# Faça um Programa que leia um número inteiro menor que 1000 e 
# imprima a quantidade de centenas, dezenas e unidades do mesmo.

# Observando os termos no plural a colocação do "e", da vírgula entre outros. 

# Exemplos:
#   326 = 3 centenas, 2 dezenas e 6 unidades
#   12 = 1 dezena e 2 unidades 

# Testar com: 326, 300, 100, 320, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

# Pede para o usuário digitar um número
numero = int(input('Por favor digite um número inteiro menor que 1000: '))

# inicia um loop infinito
while True:

    # valida se o número digitado é menor que 1000
    if numero < 1000:

        # quebra o loop
        break
    
    # se o número não for menor que 1000, o loop não será quebrado e então 
    # é solicitado novamente para o usuário digitar um número menor que 1000
    numero = int(input('Desculpe, o número digitado não é válido, por favor digite um número inteiro menor que 1000: '))

# converte o número para String (texto)
numero = str(numero)

# valida o tamanho do número em quantidade de digitos (ex. 100 = 3, 28 = 2)
tamanho_numero = len(numero)

# inicia a várial com o valor final que será exibido em tela
texto_final = numero + ' = '

# navega nas posicoes (digitos) do numero digitado
for posicao in numero:
        
    # valida pelo tamanho do número em qual casa estamos (Centena, Dezena ou Unidade)    
    if tamanho_numero == 3:
        # se o número da posição for 1 devemos utilizar a palavra no singular
        if posicao == 1:
        
            # concatenamos na variável texto final, as informações dessa posição
            texto_final = texto_final + '1 Centena , '
        
        #se não, utilizamos a palavra no plural
        else:
            # concatenamos na variável texto final, as informações dessa posição
            texto_final = texto_final + posicao + ' Centenas , '
    
    elif tamanho_numero == 2:
        if posicao == 1:
            texto_final = texto_final + '1 Dezena e '
        else:
            texto_final = texto_final + posicao + ' Dezenas e '
    
    elif tamanho_numero == 1:
        if posicao == 1:
            texto_final = texto_final + '1 Unidade'
        else:
            texto_final = texto_final + posicao + ' Unidades'

    # subtraimos 1 da variável de tamanho, pois estamos utilizando ela 
    # como referencia para saber em qual casa estamos navegando
    tamanho_numero -=1

# mostra o texto final
print(texto_final)