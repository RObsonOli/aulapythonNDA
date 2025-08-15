carro = {
    'nome': 'Lancer Evolution',
    'modelo': 'X',
    'cor': 'preto'
}
a, b, c = carro.values() # usando as variaveis a, b, c estaram sendo atribuidas na ordem o nome, modelo e cor do carro, ao usar o .values vai ser mostrado diretamente o valor de cada item do dicionario
a, b, c = carro.items() # ao usar o .items será atribuido o primeiro valor completo, com ('nome', 'Lancer Evolution')

print(a)