from .items import possible_items, item_descriptions 
from .stories import possible_scenarios, scenario_descriptions
from .maps import maps
import random

class Adventure:
    def __init__(self):
        self.state = "start"
        self.inventory = []
        self.current_scenario = None
        self.current_location = None
        self.map_data = None

    def start_game(self):
        print("Welcome to the Adventure Game!")
        self.state = "playing"
        story = random.choice(possible_scenarios)
        print("Story:", scenario_descriptions.get(story, "No description available."))
        self.main_loop()

    def main_loop(self):
        while self.state == "playing":
            action = input("What do you want to do? ")
            self.handle_action(action)

    def handle_action(self, action):
        if action.lower() == "look":
            print("You look around and see a beautiful landscape.")
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
            print("Available actions: look, take, inventory, quit, help")
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

        else:
            print("I don't understand that action.")