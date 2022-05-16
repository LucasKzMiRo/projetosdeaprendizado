jogo = 'JOGO DA FORCA'
print (f'{jogo:*^30}')
palavra = input('JOGADOR 1: Digite uma palavra de até 12 dígitos: ')
let_dig = []
let_arm = []
chances = 5

while (int(len(palavra) > 12)):
    print ('Insira uma palavra menor...')
print ('Ok, agora vamos passar o comando ao jogador 2...')

while True:
    if chances == 0:
        print ('Que pena, você perdeu!')
        break
    letra = input ('Jogador 2, insira uma letra: ')

    if len(letra) > 1:
        print ('Por favor, digite apenas 1 letra.')
    else:
        if letra in palavra and letra not in let_dig:
            let_dig.append(letra)
            print ('Parabéns, a letra está na palavra!')
        elif letra in palavra and letra in let_dig:
            print ('Letra repetida, tente novamente.')
        else:
            print ('Que pena, a letra não está na palavra.')

        status_palavra = ''
        for letra_dig in palavra:
            if letra_dig in let_dig:
                status_palavra += letra_dig
            else:
                status_palavra += '*'

        if status_palavra == palavra:
            print (f'Parabéns!!! Você acertou. A palavra era {palavra}')
            break
        else:
            print (f'A palavra está assim: {status_palavra}')

        if letra not in palavra:
            chances -= 1

        print (f'Você ainda tem {chances} chances')
print ()