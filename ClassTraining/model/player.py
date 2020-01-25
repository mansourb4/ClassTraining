from model.weapon import Weapon

knife = Weapon("Couteau", 3)
bow = Weapon("Arc", 8)

class Player :
    # Premiere fonction qui va s'initialiser lorsque l'on va creer une nouvelle instance de l'objet Player
    # self est une sorte de base de données dans laquelle on va pouvoir injecter les elements qui vont etre contenu dans cet objet Player
    def __init__(self, pseudo, health, attack, weapon):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", pseudo, "\nVie : ", health, "PV", "\nAttaque : ", attack, "\nArme : ", weapon, "\n#################################")

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage



    def attack_player(self, target_player):
        target_player.damage(self.attack)
