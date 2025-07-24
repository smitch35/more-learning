possible_enemies = [ "skeleton", "rat", "spider", "goblin", "orc" ]

enemy_stats = {
    "skeleton": {"health": 30, "attack": 5, "xp": 10},
    "rat": {"health": 10, "attack": 2, "xp": 10},
    "spider": {"health": 15, "attack": 3, "xp": 10},
    "goblin": {"health": 25, "attack": 4, "xp": 10, "items": ["potion"], "gold": 2},
    "orc": {"health": 40, "attack": 6, "xp": 10},
}


LEVEL_BOOSTS = {
    1: {},
    2: {"health": 10, "strength": 2, "agility": 1},
    3: {"health": 15, "strength": 3, "agility": 2},
    4:{"health": 20, "strength": 4, "agility": 3},
    5: {"health": 25, "strength": 6, "agility": 4},
    # Add more levels as needed
}