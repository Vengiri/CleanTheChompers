##
# clean_the_chompers.py
# Game that is themed around dental hygene
# Author: Jacob Lum
# Date Created: 17/08/2021
# Date Updated: 17/08/2021
# v0.1


class Character:
    """
    This class stores information about characters in the game
    """
    def __init__(self, max_hp):
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
        damage is an int which is howmuch damage is incoming
        before the characters effects are taken into account
        """
        # In later versions damage will be calculated based on effects
        self.max_hp -= damage