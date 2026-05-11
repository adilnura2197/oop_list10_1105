class Hayvon:
    def __init__(self, nom):
        self.nom = nom


class Ferma:
    def __init__(self):
        self.hayvonlar = []

    def add_animal(self, animal):
        self.hayvonlar.append(animal.nom)

    def info(self):
        print(self.hayvonlar)


h1 = Hayvon("Sigir")
h2 = Hayvon("Ot")

f1 = Ferma()
f1.add_animal(h1)
f1.add_animal(h2)
f1.info()
