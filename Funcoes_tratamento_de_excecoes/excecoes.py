try: # try é usado quando achamos que um bloco de codigo pode estar sucetivel a falhar, impedindo de quebrar bruscamente o projeto inteiro

    def div(a, b):

        return a/b

    x = float(input("Digite o número 1: "))
    y = float(input("Digite o número 2: "))

    print(div(x, y))

except ValueError: # ja o except serve para tratar o possivel erro que possa a acontecer, esse se trata de um ValueError, que pega um erro de escrita, por tentar colocar um valor que não é possivel ser usado durante a função
    print("Entrada inválida.")
except ZeroDivisionError: # já esse ZeroDivisionError, como o proprio nome já diz ele vai tratar uma conta com erro de divisão por zero.
    print("Não é possivel dividir por 0.")
