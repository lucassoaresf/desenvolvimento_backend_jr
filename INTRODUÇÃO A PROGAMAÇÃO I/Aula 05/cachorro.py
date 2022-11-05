class Cachorro():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print(self.nome.title() + " está sentado.")

cachorro1 = Cachorro('vasco', 2)
cachorro1.sentar()

cachorro2 = Cachorro('doug', 5)
cachorro2.sentar()