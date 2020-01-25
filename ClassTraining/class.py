from model.player import Player
from model.weapon import Weapon

knife = Weapon("Couteau", 3)
bow = Weapon("Arc", 8)



player1 = Player("Mansour", 20, 3, Weapon.set_weapon())
player2 = Player("Bob", 100, 15, Weapon.set_weapon())

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())
print(player2.get_pseudo(), "vient de subir", player1.get_attack_value(), "dégats !", "\n#################################")

player2.attack_player(player1)
print(player2.get_pseudo(), "attaque", player1.get_pseudo())
print(player1.get_pseudo(), "vient de subir", player2.get_attack_value(), "dégats !", "\n#################################")

if player1.get_health() <= 0 :
    print("Vous êtes mort !", "\n#################################")
else :
    print("Il reste à", player1.get_pseudo(), player1.get_health(), "PV", "\n#################################")


if player2.get_health() <= 0 :
    print("Vous êtes mort !", "\n#################################")
else :
    print("Il reste à", player2.get_pseudo(), player2.get_health(), "PV", "\n#################################")