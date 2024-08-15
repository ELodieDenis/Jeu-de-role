import random


pv_joueur = 50
pv_adversaire = 50
degats_adversaire = random.randint(5,10)
degats_joueur = random.randint(5, 15)
pv_potion = random.randint(15,50)
potions = 3


while pv_joueur > 0 and pv_adversaire > 0 :
    try :
        instruction = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) "))

        if instruction == 1 :
            if pv_adversaire > 0 and pv_joueur > 0 :
                pv_adversaire -= degats_adversaire
                pv_adversaire = max(pv_adversaire,0)
                pv_joueur -= degats_joueur
                pv_joueur = max(pv_joueur,0)
                pv_joueur = min(pv_joueur,50)

                print(f"🩸Vous avez infligé {degats_adversaire} point de dégats.\nIl reste {pv_adversaire} points de vie à l'adversaire.\n")
                print(f"🩸L'ennemi vous a infligé {degats_joueur} points de dégats.")
                print(f"Il vous reste {pv_joueur} points de vie" if pv_joueur > 0 else "Vous avez perdu")

            elif pv_adversaire == 0 :
                print("Vous avez gagné.\nVotre adversaire à été vaincu")
                break

            elif pv_joueur == 0 :
                print("Vous avez perdu")
                break

        if instruction == 2 :
            if potions > 0 :
                pv_joueur -= degats_joueur
                pv_joueur += pv_potion
                pv_joueur = min(pv_joueur,50)
                pv_joueur = max(pv_joueur,0)
                print(f"🩹La potion vous a rétablit {pv_potion} points de vie.")
                print(f"🩸L'ennemi vous a infligé {degats_joueur} point de dégats. Il vous reste {pv_joueur} points de vie")               
                potions -= 1
                print(f"🧪Il vous reste {potions} potions" if potions > 0 else "❌Vous n'avez plus de potions")

            else :
                print("❌Vous n'avez plus de potions")

        print("-" * 50)

        if instruction != 1 and instruction != 2 :
            raise ValueError("Veuillez entrer un chiffre valide (1 ou 2).")
    except ValueError :
        print("Veuillez entrer un chiffre valide(1 ou 2).")
        continue
