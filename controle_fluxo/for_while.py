"""
# Inicializa a variavel contador
contador = 1

# Lista de cores
cores =["vermelho","azul","roxo"]

# Loop while que continua enquanto a condição for verdadeira
while contador <= 3:
    print("Contador é: ", contador) # Imprime o valor do contador atualmente

    # Loop for que itera sobre a lista de cores
    for cor in cores:
        print("Cor:", cor)

    contador += 1 #Incrementa o contador

#Mensagem apos o loop acabar
print("Loop terminado")

"""

"""
                    esse vai mostrar apenas uma cor por vez de acordo con o contador tambem
# Inicializa a variável contador
contador = 0

# Lista de cores
cores = ["vermelho", "azul", "roxo"]

# Loop while que continua enquanto o contador for menor que o número de cores
while contador < len(cores):
    print("Contador é:", contador + 1)
    print("Cor:", cores[contador])  # Mostra apenas uma cor por vez
    contador += 1  # Incrementa o contador

# Mensagem após o loop acabar
print("Loop terminado")
"""
