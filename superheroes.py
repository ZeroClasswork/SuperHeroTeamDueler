import random

class Ability:
    def __init__(self, name, max_damage):
        '''Create Instance Variables:
            name:String
            attack_strength:Integer
        '''
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block
    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = []
        self.armors = []
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.starting_health = starting_health
        self.current_health = self.starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list 
            ability: Ability Object
        '''
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors
            armor: Armor Object
        '''
        self.armors.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, damage_amt):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health = self.current_health - damage + self.defend(damage)
        
    def is_alive(self): 
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health > 0:
            return True
        return False

    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        my_turn = True
        while self.is_alive() and opponent.is_alive():
            if my_turn:
                opponent.take_damage(self.attack())
                my_turn = False
            else:
                self.take_damage(opponent.attack())
                my_turn = True

        if my_turn: 
            opponent.add_kill(1)
            self.add_death(1)
            print(opponent.name + " won!")
        else:
            self.add_kill(1)
            opponent.add_death(1)
            print(self.name + " won!")

    def add_kill(self, num_kills):
        ''' Update kills with num_kills '''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths


class Weapon(Ability):
    def attack(self):
        """ This method returns a random value
            between one half to the full attack power of the weapon.
        """
        return random.randint(self.max_damage // 2, self.max_damage)

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name '''
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        ''' Remove hero from heroes list.
            If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
                return
        return 0

    def view_all_heroes(self):
        ''' Prints out all heroes to the console. '''
        print("Introducing " + self.name + ": ")
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        random.shuffle(self.heroes)
        random.shuffle(other_team.heroes)
        for own_hero in self.heroes:
            while own_hero.is_alive():
                for other_hero in other_team.heroes:
                    if other_hero.is_alive():
                        own_hero.fight(other_hero)
        if self.heroes[len(self.heroes)].is_alive():
            return self.name + " won."
        else:
            return other_team.name + " won."        

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print(hero.name + ": " + hero.kills + " kills to " + hero.deaths + " deaths.")
            
if __name__ == "__main__":
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.attack())
    # print(hero.current_health)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)



    pass