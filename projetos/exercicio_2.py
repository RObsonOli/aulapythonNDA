"""
Escreva um programa que peça ao usuario para digitar um numero
e então imprima a tabuada desse numero até o 10


numero = int(input("Digite um número: "))

print(f'A tabuada do número {numero} é')

for i in range(1, 21):
    resultado = numero * i
    print(f'{numero} X {i} = {resultado}')

print('-'* 25)

for i in range(1, 11):
    resultado = numero / i
    print(f'{numero} / {i} = {resultado}')

"""


def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')


numero_usuario = int(input("Digite um numero para ver a tabuada: "))
tabuada(numero_usuario)
