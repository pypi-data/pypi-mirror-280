class Corso:
    def __init__(self, nome, durata, link):
        self.nome = nome
        self.durata = durata
        self.link = link

    def __repr__(self):
        return f"{self.nome} [{self.durata} ORE] ({self.link})"


corsi = [
    Corso("Corso Hacking Etico", 60, "link1"),
    Corso("Corso Linux", 15, "link2"),
    Corso("Corso Personalizzazione Linux", 3, "link3"),
    Corso("Corso Python Offensive", 50, "link4")
]

def lista_corsi():
    for corso in corsi:
        print(corso)

def cerca_corso_by_nome(nome):
    for corso in corsi:
        if corso.nome == nome:
            return corso
    
    return None
