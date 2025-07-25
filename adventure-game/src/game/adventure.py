from .items import possible_items, item_descriptions 
from .stories import possible_scenarios, scenario_descriptions
from .maps import maps, map_dungeon 
from .enemies import possible_enemies, enemy_stats, LEVEL_BOOSTS
from colorama import init, Fore, Style
import random 
import pygame
import os
import sys


class Adventure:    
    def __init__(self):
        pygame.mixer.init()
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(os.path.dirname(__file__))
        self.state = "start"
        self.inventory = ["map"]
        self.current_scenario = "dungeon"
        self.current_location = None
        self.map_data = None
        self.stats = {}
        self.stats["xp"] = 0
        self.LEVEL_THRESHOLDS = [0, 20, 50, 100, 200]  # XP needed for each level
        self.player_x = 2
        self.player_y = 3
        
        pygame.mixer.music.load(os.path.join("game", "music", "overworld.mp3"))
        pygame.mixer.music.play(-1)

        
    def combat(self,enemy):
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(os.path.dirname(__file__))
        pygame.mixer.music.load(os.path.join("game", "music", "battle_music.mp3"))
        pygame.mixer.music.play(-1)
        
        while self.stats["health"] > 0 and enemy.health > 0:
            print("\nChoose your action:")
            print("1. Attack")
            print("2. Use Item")
            print("3. Run")
            choice = input("Enter the number of your action: ").strip()

            if choice == "1":
                damage = random.randint(1, self.stats["strength"])
                enemy.health -= damage
                print(f"You hit {enemy.name} for {damage} damage.  Enemy health: {enemy.health}")
                damage = random.randint(1, enemy.attack)
                self.stats["health"] -= damage
                print(f"The {enemy.name} hits you for {damage} damage.  Your health: {self.stats['health']}")
            elif choice == "2":
                pass # TODO: Implement use item
            elif choice == "3":
                if random.random() < 0.7:
                    print("You run from combat")
                    pygame.mixer.music.load(os.path.join("game", "music", "overworld.mp3"))
                    pygame.mixer.music.play(-1)
                    return
                else:
                    damage = random.randint(1, enemy.attack)
                    self.stats["health"] -= damage
                    print(f"The {enemy.name} hits you for {damage} damage.  Your health: {self.stats['health']}")
            else:
                print("Invalid choice. Try again.")
                continue  # Repeats the turn
            
            
            if enemy.health <= 0:
                pygame.mixer.music.load(os.path.join("game", "music", "overworld.mp3"))
                pygame.mixer.music.play(-1)
                print(f"You defeated the {enemy.name} and gained {enemy.xp}xp!")
                self.stats["xp"] += enemy.xp
                self.stats["gold"] += enemy_stats[enemy.name]["gold"]
                self.check_level_up()
                for item in enemy_stats[enemy.name].get("items", []):
                    if random.random() < 0.5:  # 50% chance to drop each item
                        pygame.mixer.music.load(os.path.join("game", "music", "overworld.mp3"))
                        pygame.mixer.music.play(0)
                        self.inventory.append(item)       
                        print(f"You found a {item} on the {enemy.name}!")
                return
            

            if self.stats["health"] <= 0:
                print("You died.")
                self.state = "quit"

    def start_game(self):
        self.state = "playing"
        print(Fore.CYAN + "Story:" + Style.RESET_ALL + " " + Fore.GREEN + scenario_descriptions.get(self.current_scenario, "No description available.") + Style.RESET_ALL)
        self.map_data = maps[self.current_scenario]  # Load the map for the scenario
        self.current_location = self.map_data["start"]
        self.stats["health"] = random.randint(50, 100)  # Random health between 50 and 100
        self.stats["strength"] = random.randint(5, 20)
        self.stats["intelligence"] = random.randint(5, 20)
        self.stats["agility"] = random.randint(5, 20)
        self.stats["level"] = 1
        self.stats["gold"] = 0
        print(f"Your stats: {self.stats}")
        self.main_loop()
        

    def main_loop(self):
        while self.state == "playing":
            action = input("What do you want to do? ")
            self.handle_action(action)

    def handle_action(self, action):
        if action.lower() == "look":
            locs = self.map_data["locations"]
            current = self.current_location
            print(Fore.GREEN + locs[current]["desc"] + Style.RESET_ALL)
            if "north" in locs[current]:
                print("You can go north to:", locs[current]["north"])
                
            if "south" in locs[current]:
                print("You can go south to:", locs[current]["south"])
                
            if "east" in locs[current]:
                print("You can go east to:", locs[current]["east"])
            if "west" in locs[current]:
                print("You can go west to:", locs[current]["west"])
        elif action.lower() == "take":
            item = input("What do you want to take? ")
            self.inventory.append(item)
            print(f"You have taken {item}.")
        elif action.lower() == "inventory":
            print("Your inventory:", self.inventory)
        elif action.lower() == "quit":
            print("Thanks for playing!")
            self.state = "quit"
        elif action.lower() == "help":
            print("Available actions: look (move with cardinal directions), take, inventory, quit, help")
        elif action.lower() == "find":
            item = random.choice(possible_items)
            self.inventory.append(item)
            print(f"You found a {item} and added it to your inventory!")
        elif action.lower() == "inspect":
            item = input("Which item do you want to inspect? ")
            if item in self.inventory:
                print(f"Inspecting {item}: {item_descriptions.get(item, 'No description available.')}")
            else:
                print("You don't have that item.")
        elif action.lower() in ["north", "south", "east", "west"]:
            locs = self.map_data["locations"]
            current = self.current_location
            if action.lower() in locs[current]:
                self.current_location = locs[current][action.lower()]
                print(Fore.GREEN + locs[self.current_location]["desc"] + Style.RESET_ALL)
                if action.lower() == "north":
                    self.player_y -= 1
                elif action.lower() == "south":
                    self.player_y += 1
                elif action.lower() == "east":
                    self.player_x += 1
                elif action.lower() == "west":
                    self.player_x -= 1
                if random.random() < 0.5:
                    enemy_name = random.choice(possible_enemies)
                    enemy = Enemy(enemy_name, enemy_stats[enemy_name]["health"], enemy_stats[enemy_name]["attack"], enemy_stats[enemy_name]["xp"])
                    print(f"A wild {enemy.name} appears! Health: {enemy.health}, Attack: {enemy.attack}")
                    self.combat(enemy)
            else:
                print("You can't go that way.")
        elif action.lower() == "stats":
            print("Your stats:", self.stats)
        
        elif action.lower() == "map":
            # Make sure you have player_x and player_y defined and updated as the player moves
            self.display_map(map_dungeon, self.player_x, self.player_y)

        else:
            print("I don't understand that action.")

    def check_level_up(self):
        current_level = self.stats["level"]
        for i, threshold in enumerate(self.LEVEL_THRESHOLDS):
            if self.stats["xp"] >= threshold and i + 1 > current_level:
                self.stats["level"] = i + 1
                boosts = LEVEL_BOOSTS[i +1] if i + 1 < len(LEVEL_BOOSTS) else {}
                for stat, amount in boosts.items():
                    self.stats[stat] += amount
                print(f"You leveled up! Now level {self.stats['level']}. Stats increated: {boosts}")
    
    def display_map(self, map_grid, player_x, player_y):
        for y, row in enumerate(map_grid):
            line = ""
            for x, cell in enumerate(row):
                if x == player_x and y == player_y:
                    line += "@ "
                elif cell == "# ":
                    line += Fore.RED + "# " + Style.RESET_ALL 
                else:
                    line += cell
            print(line)

class Enemy:
    def __init__(self, name, health, attack, xp):
        self.name = name
        self.health = health
        self.attack = attack
        self.xp = xp