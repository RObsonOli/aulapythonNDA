carro = {
    'nome': 'bugatti',
    'modelo': 'bolide'
}
print(carro.get('nome')) # .get serve para pegar uma condição especifica do dicionario, nesse caso nome do carro
print(carro.get('modelo'))

carro['modelo'] = 'chiron' # serve para atribuir um novo modelo de carro ao dicionario

print(carro)
print(carro.get('modelo')) # consequentemente o modelo foi alterado para a versão mais nova
