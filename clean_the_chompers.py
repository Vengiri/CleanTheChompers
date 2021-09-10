##
# clean_the_chompers.py
# Game that is themed around dental hygene
# Author: Jacob Lum
# Date Created: 17/08/2021
# Date Updated: 10/09/2021
# v0.9

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

    def damage_incoming(self, damage):
        """
        damage is an int which is how much damage is incoming
        before the characters effects are taken into account
        """
        # In later versions damage will be calculated based on effects
        self.max_hp -= damage

    def damage_outcoming(self, damage):
        """
        damage is an int from the attack which does not include
        effects
        """
        # This is the maximum % change in damage
        DAMAGE_VARIANCE = 15
        # Calculate how damage changes
        damage_change = random.randint(0, DAMAGE_VARIANCE*2)
        # Determine if increase or decrease
        if damage_change < DAMAGE_VARIANCE:
            # Calculate damage decrease
            damage = math.floor(damage*((100-damage_change)/100))
        else:
            # Calculate new damage rounded down
            damage = math.floor(damage + (damage*((damage_change-DAMAGE_VARIANCE)/100)))
        # In later versions damage will be calculated with effects
        return damage

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
        self.discard = []

    def attack(self, damage):
        """
        Does an attack
        """
        print(self.damage_outcoming(damage))


class Effect():
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
    you.attack(you.draw[choice].damage)
    # Check if there is an effect
    if you.draw[choice].effect != None:
        you.effects.append(you.draw[choice].effect)
        print(you.effects[0].name)
        

  
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
    you.draw.append(toothbrush)
    you.draw.append(tube)
    menu()


        
        
