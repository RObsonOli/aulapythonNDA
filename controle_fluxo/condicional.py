idade = int(input("Digite sua idade: "))

if idade > 18: #if idade > 18 significa que, se sua idade for maior que 18 anos você pode votar.
    print("Você pode votar")
elif idade == 18: #elif idade == 18, significa que se a sua idade for exatamente igual a 18 você poderá tirar seu titulo de eleitor.
    print("Você ja pode tirar o seu titulo de eleitor!")
else: # se sua idade for menor que 18 anos você terá que estudar.
    print("Vai estudar!")
