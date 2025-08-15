def saudacao(nome): # def seria o modelo padrao para uma função, a função se chama saudação, e tem um parametro chamado nome
    print(f'Meu nome é {nome}!') # Exibe uma mensagem com o nome passado na função acima


saudacao('Robson') # serve para atribuir um valor para a função saudação consequentemente atribuindo um valor ao print
saudacao('Carlos')


def dobro(numero):
    return numero * 2


resultado = dobro(5)

print(f'O dobro de 5 é {resultado}')