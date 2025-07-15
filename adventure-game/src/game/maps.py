maps = {
    "dungeon": {
        "start": "cell",
        "locations": {
            "north": {"desc": "An empty Hallway.", "id": "hallway"},
            "south": {"desc": "A dark cell.", "id": "cell"},
            "east": {"desc": "A damp corridor.", "id": "corridor"},
            "west": {"desc": "A locked door.", "id": "door"}
        }
    },
    "forest": {
        "description": "A dense forest with towering trees.",
        "exits": {
            "south": "dungeon",
            "west": "castle"
        }
    },
    "castle": {
        "description": "A grand castle with high walls.",
        "exits": {
            "south": "forest",
            "west": "dungeon"
        }
    }
}