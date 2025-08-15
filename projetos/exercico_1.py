# Escreva um programa que receba uma frase do usuario
# e conte quantas letras "a" aparece durante essa frase

"""
forma simples e rapida de ser feita

frase = input("Qual seu nome completo: ")
print(frase.count('a'))

"""

# Forma mais estruturada
def contar_letras_a(frase): # função para contar as letras 'a' de uma frase
    count = 0 # contador começa pelo 0
    for letra in frase: # para cada letra na frase
        if letra == 'a' or letra == 'A': # quando a letra for igual a 'a' ou igual a 'A'
            count += 1 # adicione 1 ao contador
    return count

frase_usuario = input("Digite uma frase: ")
quantidade_a = contar_letras_a(frase_usuario)
print(f"A letra 'a' aparece {quantidade_a} vezes na frase '{frase_usuario}'.")
