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

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
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
        self.current_health = int(self.current_health) - int(damage) + int(self.defend())
        
    def is_alive(self): 
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if int(self.current_health) > 0:
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
        if len(self.heroes) < 1 or len(other_team.heroes) < 1:
            return
        random.shuffle(self.heroes)
        random.shuffle(other_team.heroes)
        for own_hero in self.heroes:
            for other_hero in other_team.heroes:
                if other_hero.is_alive() and own_hero.is_alive():
                    own_hero.fight(other_hero)
        if self.heroes[len(self.heroes)-1].is_alive():
            print(self.name + " won.")
        else:
            print(other_team.name + " won.")      

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print(hero.name + ": " + hero.kills + " kills to " + hero.deaths + " deaths.")

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = Team("One")
        self.team_two = Team("Two")

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("Name your ability: ")
        max_damage = input("What is the max damage of this ability?: ")
        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("Name your weapon: ")
        max_damage = input("What is the max damage of this weapon?: ")
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        name = input("Name your armor: ")
        max_block = input("What is the max block of this armor?: ")
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        name = input("Name your hero: ")
        starting_health = int(input("What is the starting health of this hero?: "))
        hero = Hero(name, starting_health)
        inputter = -1
        while inputter < 0:
            inputter = int(input("How many pieces of armor does this hero wear?: "))
            for armor in range(inputter):
                hero.add_armor(self.create_armor())
        inputter = -1
        while inputter < 0:
            inputter = int(input("How many abilities does this hero possess?: "))
            for ability in range(inputter):
                hero.add_ability(self.create_ability())
        inputter = -1
        while inputter < 0:
            inputter = int(input("How many weapons does this hero wield?: "))
            for weapon in range(inputter):
                hero.add_weapon(self.create_weapon())
        if len(hero.abilities) == 0:
            existance = Ability("Existance is Pain", random.randint(13, 37))
            hero.add_ability(existance)
            print(hero.name + " unlocked a new ability! EXISTANCE IS PAIN doing up to " + str(existance.max_damage) + " damage.")
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        number_of_heroes = 0
        while number_of_heroes < 1:
            number_of_heroes = int(input("How many heroes should be on team one?: "))
        for hero in range(number_of_heroes):
            print("Hero " + str(hero) + ": ")
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        number_of_heroes = 0
        while number_of_heroes < 1:
            number_of_heroes = int(input("How many heroes should be on team two?: "))
        for hero in range(number_of_heroes):
            print("Hero " + str(hero) + ": ")
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        team_one_average_kills = 0
        team_one_average_deaths = 0
        team_two_average_kills = 0
        team_two_average_deaths = 0
        for hero in self.team_one.heroes:
            team_one_average_kills += hero.kills
            team_one_average_deaths += hero.deaths
        team_one_average_kills /= len(self.team_one.heroes)
        team_one_average_deaths /= len(self.team_one.heroes)
        for hero in self.team_two.heroes:
            team_two_average_kills += hero.kills
            team_two_average_deaths += hero.deaths
        team_two_average_kills /= len(self.team_two.heroes)
        team_two_average_deaths /= len(self.team_two.heroes)
        print("Team one average kills: " + str(team_one_average_kills))
        print("Team one average deaths: " + str(team_one_average_deaths))
        print("Team two average kills: " + str(team_two_average_kills))
        print("Team two average deaths: " + str(team_two_average_deaths))
        print("Remaining heroes: ")
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(" - " + hero.name)
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(" - " + hero.name)

class Weapon(Ability):
    def attack(self):
        """ This method returns a random value
            between one half to the full attack power of the weapon.
        """
        return random.randint(int(self.max_damage) // 2, self.max_damage)

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

    # arena = Arena()
    # arena.build_team_one()
    # arena.build_team_two()
    # arena.team_battle()
    # arena.show_stats()

    if __name__ == "__main__":
        game_is_running = True

        # Instantiate Game Arena
        arena = Arena()

        #Build Teams
        arena.build_team_one()
        arena.build_team_two()

        while game_is_running:

            arena.team_battle()
            arena.show_stats()
            play_again = input("Play Again? Y or N: ")

            #Check for Player Input
            if play_again.lower() == "n":
                game_is_running = False

            else:
                #Revive heroes to play again
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()