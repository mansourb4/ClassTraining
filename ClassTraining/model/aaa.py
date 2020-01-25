def yes (my_weapon):
    my_weapon = input("Quelle arme voulez-vous : Arc ou Couteau ?\n-> " )
    while my_weapon != "Arc" or my_weapon != "Couteau":
        if my_weapon == "Arc":
            print("Vous avez obtenu l'Arc, vos dégats seront augmentés de 8 points ! ")
            break
        elif my_weapon == "Couteau":
            print("Vous avez obtenu le Couteau, vos dégats seront augmentés de 3 points ! ")
            break
        else:
            my_weapon = input("VOUS DEVEZ CHOISIR ENTRE L'ARC OU LE COUTEAU !\n-> ")


yes()

from model.player import Player
from model.weapon import Weapon

knife = Weapon("Couteau", 3)
bow = Weapon("Arc", 8)



player1 = Player("Mansour", 20, 3, Player.set_weapon(""))
player2 = Player("Bob", 100, 15, Player.set_weapon(""))

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