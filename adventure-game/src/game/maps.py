maps = {
    "dungeon": {
        "start": "cell",
        "locations": {
            "cell": {"desc": "A dark cell.", "north": "hallway"},
            "hallway": {"desc": "An empty hallway.", "south": "cell", "east": "corridor"},
            "corridor": {"desc": "A damp corridor.", "west": "hallway"},
            "door": {"desc": "A locked door.", "east": "hallway"}
        }
    },
    "forest": {
        "start": "clearing",
        "locations": {
            "clearing": {"desc": "A forest clearing.", "north": "deep_forest", "west": "castle"},
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