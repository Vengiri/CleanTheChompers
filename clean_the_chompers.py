##
# clean_the_chompers.py
# Game that is themed around dental hygene
# Author: Jacob Lum
# Date Created: 17/08/2021
# Date Updated: 10/09/2021
# v0.10

import random
import math

class Character:
    """
    This class stores information about characters in the game
    """
    def __init__(self, max_hp, name):
        """
        max_hp is an int that defines the maximum hp
        current_hp is an int that starts at max_hp 
        name is the name of the character
        effects is a blank list
        """
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.name = name
        self.effects = []

    def damage_incoming(self, damage_calculated):
        """
        damage is an int which is how much damage is incoming
        """
        # In later versions damage will be calculated based on effects
        self.current_hp -= damage_calculated
        print(f"{self.name} took {damage_calculated} damage!")

    def damage_outcoming(self, damage):
        """
        damage is an int from the attack which does not include
        effects
        """
        # Print the first part of the damage 
        print(f"Base dmg of {damage} + ", end = "")

        # Calculate the damage with accordance to modifiers
        total_modifier = 0
        for effect in self.effects:
            total_modifier += effect.outcoming_modifier
        modified_damage = damage * (total_modifier/100 + 1)
        # Print the damage change from the modifier
        print(f"{modified_damage-damage} from modifiers + ", end = "")
        # This is the maximum % change in damage
        DAMAGE_VARIANCE = 15
        # Calculate how damage changes
        damage_change = random.randint(0, DAMAGE_VARIANCE*2)
        # Determine if increase or decrease
        if damage_change < DAMAGE_VARIANCE:
            # Calculate damage decrease
            total_damage = math.floor(modified_damage*((100-damage_change)/100))
        else:
            # Calculate new damage rounded down
            total_damage = math.floor(modified_damage + (modified_damage*((damage_change-DAMAGE_VARIANCE)/100)))
        # In later versions damage will be calculated with effects
        print(f"{total_damage-modified_damage} from damage variance",
              f"for a total of {total_damage}!")
        return total_damage

    def display_stats(self):
        """
        Displays the current stats of the character
        """
        print(f"{self.name} has {self.current_hp}hp")


class Player(Character):
    """
    This class stores information about the player
    """
    def __init__(self, max_hp):
        """
        draw is the draw pile
        discard is the discard pile
        """
        super().__init__(max_hp, "Player")
        self.draw = []

    def attack(self, damage):
        """
        Does an attack
        """
        print(self.damage_outcoming(damage))


class Effect:
    """
    This class is the status effects which effect enimies and players
    """
    def __init__(self, duration, outcoming_modifier,
                 incoming_modifier, name):
        """
        duration is how many turns an effect lasts for
        outcoming_modifier is the amount it changes outcoming damage by
        incoming_modifier is the amount it changes incoming damage by
        """
        self.duration = duration
        self.outcoming_modifier = outcoming_modifier
        self.incoming_modifier = incoming_modifier
        self.name = name


class Enemy(Character):
    """
    This class is for enimies in the game
    """
    def __init__(self, max_hp, name, damage):
        """
        Damage is how much raw damage it deals per turn
        """
        super().__init__(max_hp, name)
        self.base_damage = damage

    def damage_deal(self):
        """
        This returns the ammount of damage the enemy deals on this turn
        """
        return self.damage_outcoming(self.base_damage)


def menu():
    """
    This is tha mian menu for the game
    """
    choice = ""
    # Run unti lthe player wants to exit
    while choice != "Q":
        print("""
Welcome to clean the chompers!
What would you like to do?
(P)lay
(S)ettings
(Q)uit""")
        choice = input("Enter choice: ").upper()
        # Do the coressponding thing to thier choice
        if choice == "P":
            battle_menu()
        elif choice == "S":
            pass
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("That wasn't a valid option")


def battle_menu():
    """
    Menu for the options a player can take in battle
    """
    battle = True
    while battle:
        # Display the players stats
        you.display_stats()
        
        # Create space
        print()
        print("Actions you can take: ")
        
        # Print all the actions the player has
        for i in range(0,len(you.draw)):
            print(f"""
    action {i} {you.draw[i].name}""")
        choice = int(input("Enter choice: "))
        
        # Check if there is an effect
        if you.draw[choice].effect != None:
            you.effects.append(you.draw[choice].effect)
            print(you.effects[0].name)

        # Apply the damage to the enemy
        cavity.damage_incoming(you.damage_outcoming(you.draw[choice].damage))

        # Check if it dies
        if cavity.current_hp <= 0:
            print("It dies")
            battle = False
        else:
            # Calculate how much damage the player takes
            you.damage_incoming(cavity.damage_deal())

            # Check if player dies
            if you.current_hp <= 0:
                print("Your teeth rot away into the meaningless sands of time")
                battle = False
                
        
        

  
class Action:
    """
    This class stores information about an action the player could make
    """
    
    def __init__(self, damage, name, effect = None):
        """Damage is how much damage it does"""
        self.damage = damage
        self.name = name
        self.effect = effect


if __name__ == "__main__":
    you = Player(100)
    toothbrush = Action(100, "Toothbrush")
    toothpaste = Effect(0, 20, 0, "Toothpaste")
    tube = Action(0, "Tube", toothpaste)
    cavity = Enemy(300, "Cavity", 20)
    you.draw.append(toothbrush)
    you.draw.append(tube)
    menu()


        
        
