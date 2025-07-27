possible_items = {
    "equipment": ["sword", "shield"],
    "consumables": ["potion", "hi-potion"],
    "story_items": ["map", "key", "letter", "torch"]
}


item_descriptions = {
    "sword": {"desc": "A sharp blade, useful for fighting enemies."},
    "shield": {"desc": "A sturdy shield to protect you from attacks."},
    "potion": {"desc": "A mysterious liquid that restores health."},
    "map": {"desc": "A map showing the surrounding area."},
    "hi-potion": {"desc": "Larger than the initial potion"},
    "key": {"desc":"A small key that might open a locked door."},
    "letter": {"desc":"A letter written by a lost loved one."},
    "torch": {"desc": "Its a torch for seeing better in the dark."}
}

item_effects = {
    "potion": {"health": 10},
    "hi-potion": {"health": 20},
    "sword": {"strength": 2},
    "shield": {"health": 5}

}