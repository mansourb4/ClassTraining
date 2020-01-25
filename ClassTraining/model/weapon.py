class Weapon :

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.damage

    def set_weapon():
        my_weapon = input("Quelle arme voulez-vous : Arc ou Couteau ?\n-> ")
        while my_weapon != "Arc" or my_weapon != "Couteau":
            if my_weapon == "Arc":
                print("Vous avez obtenu l'Arc, vos dégats seront augmentés de 8 points ! ")
                break
            elif my_weapon == "Couteau":
                print("Vous avez obtenu le Couteau, vos dégats seront augmentés de 3 points ! ")
                break
            else:
                my_weapon = input("VOUS DEVEZ CHOISIR ENTRE L'ARC OU LE COUTEAU !\n-> ")


