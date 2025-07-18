from .items import possible_items, item_descriptions 
from .stories import possible_scenarios, scenario_descriptions
from .maps import maps
import random

class Adventure:
    def __init__(self):
        self.state = "start"
        self.inventory = []
        self.current_scenario = "dungeon"
        self.current_location = None
        self.map_data = None
        self.stats = {}

    def start_game(self):
        print("Welcome to the Adventure Game!")
        self.state = "playing"
        print("Story:", scenario_descriptions.get(self.current_scenario, "No description available."))
        self.map_data = maps[self.current_scenario]  # Load the map for the scenario
        self.current_location = self.map_data["start"]
        self.stats["health"] = random.randint(50, 100)  # Random health between 50 and 100
        self.stats["strength"] = random.randint(5, 20)
        self.stats["intelligence"] = random.randint(5, 20)
        self.stats["agility"] = random.randint(5, 20)
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
            print(locs[current]["desc"])
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
                print(locs[self.current_location]["desc"])
            else:
                print("You can't go that way.")
        elif action.lower() == "stats":
            print("Your stats:", self.stats)
        else:
            print("I don't understand that action.")