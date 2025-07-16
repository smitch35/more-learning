maps = {
    "dungeon": {
        "start": "cell",
        "locations": {
            "cell": {"desc": "A dark cell.  It reeks of excrement and death.  Your only sollace is that the door appears to be open and you can leave.", "north": "hallway"},
            "hallway": {"desc": "An empty hallway.  It's quiet and the only sound you hear is the scurry of an aniamal and the drip of moisture.", "south": "cell", "west": "corridor"},
            "corridor": {"desc": "A damp corridor.  You wonder how far this dungeon goes and why you are there in the first place.  If only you could find your way", "east": "hallway", "north": "door"},
            "door": {"desc": "A locked door.", "south": "corridor"},
            "hallway_2": {"desc": "Another empty hallway, you wonder how big this place is.", "east": "empty_cell"},
            "empty_cell": {"desc": "Another cell, its captor long dead.", "south": "hallway_3"},
            "hallway_3": {"desc": "You continue down another dark dank path.", "south": "store_room"},
            "store_room": {"desc": "It appears you've found a storeroom that seems to have some items that could help.", "east": "dead_end", "south": "exit"},
            "exit": {"desc": "You're free from the dungeon, but what lies ahead..."}

        }
    },
    "forest": {
        "start": "clearing",
        "locations": {
            "clearing": {"desc": "A forest clearing.", "north": "deep_forest", "west": {"map" :"castle", "location": "gate"},
            "deep_forest": {"desc": "Dense trees surround you.", "south": "clearing"}
        }
    },
    "castle": {
        "start": "gate",
        "locations": {
            "gate": {"desc": "A grand castle gate.", "east": "forest"}
        }
    },

    "maze": {
        "start": "entrance",
        "locations": {
            "entrance": {"desc": "You stand at the entrance of a twisting maze.", "north": "hallway"},
            "hallway": {"desc": "A long, narrow hallway.", "south": "entrance", "east": "dead_end1", "north": "crossroads"},
            "dead_end1": {"desc": "A dead end. Nothing here.", "west": "hallway"},
            "crossroads": {"desc": "A crossroads with paths in all directions.", "south": "hallway", "east": "dead_end2", "west": "gallery", "north": "treasure_room"},
            "dead_end2": {"desc": "A dead end with a pile of rocks.", "west": "crossroads"},
            "gallery": {"desc": "A gallery filled with old paintings.", "east": "crossroads", "north": "dead_end3"},
            "dead_end3": {"desc": "A dead end. The air is cold here.", "south": "gallery"},
            "treasure_room": {"desc": "A room glittering with treasure! You found the exit.", "south": "crossroads"}
        }
    }
}
}