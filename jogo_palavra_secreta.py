"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra = 'perfume'
letra_acertada = ''
tentativas = 0

while True: 
    letra_digitada = input('digite uma letra: ')
    
    tentativas += 1
    
    
    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue

    if letra_digitada in palavra:
        letra_acertada += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print(f'Palavra formada: {palavra_formada}')
    
    if palavra_formada == palavra:
        print('VOCÊ GANHOU!')
        print(f'A palavra era: {palavra_formada}')
        print(f'tentativas: {tentativas}')
        letra_acertada = ''
        tentativas = 0