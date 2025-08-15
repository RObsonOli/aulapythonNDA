lista_de_frutas = ['banana', 'laranja', 'uva', 'morango']

fruta = lista_de_frutas[1] # ao atribuir a uma funçaõ o lista[0], você podera pegar o valor que esta na posição 0 da lista

banana, *others = lista_de_frutas # serve para separa a mostragem de dados, fazendo com que seja atribuida o valor banana da lista na variavel banana e usando o *others ele fica como uma variavel para ser atribuida os outros valores da lista

print(others)
print(banana)
