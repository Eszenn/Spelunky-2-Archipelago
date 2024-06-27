from typing import Dict, Optional, NamedTuple

from BaseClasses import Item, ItemClassification


class DredgeItem(Item):
    game = "DREDGE"


class DredgeItemData(NamedTuple):
    classification: ItemClassification = ItemClassification.filler
    code: int = None
    amount: Optional[int] = 1


base_id = 379366373343000

equipment_items = {
    "Basic Fishing Pole": DredgeItemData(ItemClassification.progression, 1),
    "Simple Skimmer": DredgeItemData(ItemClassification.progression, 2, 2),
    "Weighted Line": DredgeItemData(ItemClassification.progression, 3),
    "Sinew Spindle": DredgeItemData(ItemClassification.progression, 4),
    "Hydraulic Rod": DredgeItemData(ItemClassification.progression, 5),
    "Flexible Fish Pole": DredgeItemData(ItemClassification.progression, 6),
    "Heat-Resistant Line": DredgeItemData(ItemClassification.progression, 7),
    "Anti-Tangle Line": DredgeItemData(ItemClassification.progression, 8),
    "Versatile Rod": DredgeItemData(ItemClassification.progression, 9),
    "Harvesting Platform": DredgeItemData(ItemClassification.progression, 10),
    "Bottomless Lines": DredgeItemData(ItemClassification.progression, 11),
    "Fathomless Winch": DredgeItemData(ItemClassification.progression, 12),
    "Sampling Device": DredgeItemData(ItemClassification.progression, 13),
    "Tendon Rod": DredgeItemData(ItemClassification.progression, 14),
    "Viscera Crane": DredgeItemData(ItemClassification.progression, 15),
    "Dredging Equipment": DredgeItemData(ItemClassification.progression, 16),
    "Encrusted Talisman": DredgeItemData(ItemClassification.useful, 17),
    "Basic Trawl Net": DredgeItemData(ItemClassification.progression, 18),
    "Improved Trawl Net": DredgeItemData(ItemClassification.progression, 19),
    "Silt Filtering Trawl Net": DredgeItemData(ItemClassification.progression, 20),
    "Tempered Mesh Net": DredgeItemData(ItemClassification.progression, 21),
    "Large Trawl Net": DredgeItemData(ItemClassification.progression, 22),
    "Heavy-Duty Trawl Net": DredgeItemData(ItemClassification.progression, 23),
    "Basic Crab Pot": DredgeItemData(ItemClassification.progression, 24),
    "Efficient Crab Pot": DredgeItemData(ItemClassification.progression, 25),
    "Hardy Crab Pot": DredgeItemData(ItemClassification.progression, 26),
    "Large Crab Pot": DredgeItemData(ItemClassification.progression, 27),
    "Complex Crab Pot": DredgeItemData(ItemClassification.progression, 28),
    "Massive Crab Pot": DredgeItemData(ItemClassification.progression, 29),
    "Reinforce Crab Pot": DredgeItemData(ItemClassification.progression, 30),
    "Mouth of the Deep": DredgeItemData(ItemClassification.progression, 31),
    "Sustainable Fishing": DredgeItemData(ItemClassification.progression_skip_balancing, 32),
    "Rods, Reels, and Rigs": DredgeItemData(ItemClassification.progression_skip_balancing, 33),
    "Correct Engine Operation": DredgeItemData(ItemClassification.progression_skip_balancing, 34),
    "The Relaxed Mind": DredgeItemData(ItemClassification.progression_skip_balancing, 35),
    "Engineer's Companion": DredgeItemData(ItemClassification.progression_skip_balancing, 36),
    "Art of the Silver Tongue": DredgeItemData(ItemClassification.progression_skip_balancing, 37),
    "Getting Over it with Mind and Body": DredgeItemData(ItemClassification.progression_skip_balancing, 38),
    "A Plan for the Future": DredgeItemData(ItemClassification.progression_skip_balancing, 39),
    "Haggling and Bartering - A Guide": DredgeItemData(ItemClassification.progression_skip_balancing, 40),
    "Advanced Fishing": DredgeItemData(ItemClassification.progression_skip_balancing, 41),
    "Pushing the Limit - Engines": DredgeItemData(ItemClassification.progression_skip_balancing, 42),
    "Nautical Engineering": DredgeItemData(ItemClassification.progression_skip_balancing, 43),
    "Peculiar Engine": DredgeItemData(ItemClassification.useful, 44, 2),
    "Weak Valve Engine": DredgeItemData(ItemClassification.useful, 45),
    "Rusty Outboard Engine": DredgeItemData(ItemClassification.useful, 46),
    "Improved Outboard Engine": DredgeItemData(ItemClassification.useful, 47),
    "Refined Outboard Engine": DredgeItemData(ItemClassification.useful, 48),
    "Jet Drive Engine": DredgeItemData(ItemClassification.useful, 49),
    "Twin Prop Engine": DredgeItemData(ItemClassification.useful, 50),
    "Twin Jet Drive Engine": DredgeItemData(ItemClassification.useful, 51),
    "Engine Stack": DredgeItemData(ItemClassification.useful, 52)
}

abilities = {
    "Haste": DredgeItemData(ItemClassification.useful, 53),
    "Manifest": DredgeItemData(ItemClassification.useful, 54),
    "Banish": DredgeItemData(ItemClassification.useful, 55),
    "Atrophy": DredgeItemData(ItemClassification.useful, 56),
    "Camera": DredgeItemData(ItemClassification.filler, 57)
}

ship_upgrades = {
    "Progressive Hull Upgrade": DredgeItemData(ItemClassification.useful, 58, 3),
    "Progressive Rod Space Upgrade": DredgeItemData(ItemClassification.useful, 59, 4),
    "Progressive Net Space Upgrade": DredgeItemData(ItemClassification.useful, 60, 2),
    "Progressive Cargo Space Upgrade": DredgeItemData(ItemClassification.useful, 61, 3),
    "Progressive Engine Space Upgrade": DredgeItemData(ItemClassification.useful, 62, 3),
    "Progressive Light Space Upgrade": DredgeItemData(ItemClassification.useful, 63, 3),
}

relics = {
    "Ornate Key": DredgeItemData(ItemClassification.progression_skip_balancing, 64),
    "Rusted Music Box": DredgeItemData(ItemClassification.progression_skip_balancing, 65),
    "Jewel Encrusted Band": DredgeItemData(ItemClassification.progression_skip_balancing, 66),
    "Shimmering Necklace": DredgeItemData(ItemClassification.progression_skip_balancing, 67),
    "Antique Pocket Watch": DredgeItemData(ItemClassification.progression_skip_balancing, 68)
}

upgrade_materials = {
    "Research Part": DredgeItemData(ItemClassification.progression_skip_balancing, 69, 78),
    "Lumber": DredgeItemData(ItemClassification.progression_skip_balancing, 70, 64),
    "Metal Scraps": DredgeItemData(ItemClassification.progression_skip_balancing, 71, 49),
    "Cloth": DredgeItemData(ItemClassification.progression_skip_balancing, 72, 33),
    "Refined Metal": DredgeItemData(ItemClassification.progression_skip_balancing, 73, 8),
}

quest_items = {
    "Handkerchief": DredgeItemData(ItemClassification.progression, 74),
    "Bronze Belt Buckle": DredgeItemData(ItemClassification.progression, 75),
    "Family Crest": DredgeItemData(ItemClassification.progression, 76),
    "Mortar Frame": DredgeItemData(ItemClassification.progression, 77),
    "Mortar Barrel": DredgeItemData(ItemClassification.progression, 78),
    "Dog Tags": DredgeItemData(ItemClassification.progression, 79, 4),
    "Fathomless Flame": DredgeItemData(ItemClassification.progression, 80, 3),
    "Packed Explosive": DredgeItemData(ItemClassification.progression, 81),
    "Small Package": DredgeItemData(ItemClassification.progression, 82),
    "Large Package": DredgeItemData(ItemClassification.progression, 83),
    "Repulsion Machine": DredgeItemData(ItemClassification.progression, 84),
    "Stone Tablet": DredgeItemData(ItemClassification.progression, 85, 3),
    "Fused Tablet": DredgeItemData(ItemClassification.progression, 86, 1),
    "Pungent Bait": DredgeItemData(ItemClassification.progression, 87, 1),
    "Fetid Bait": DredgeItemData(ItemClassification.progression, 88, 1),
    "Reeking Bait": DredgeItemData(ItemClassification.progression, 89, 1),
    "Chunk of Flesh": DredgeItemData(ItemClassification.progression, 90, 3)
}

filler_items = {
    "Small Scrap of Paper": DredgeItemData(ItemClassification.filler, 91),
    "Scrap of Paper": DredgeItemData(ItemClassification.filler, 92),
    "Large Scrap of Paper": DredgeItemData(ItemClassification.filler, 93),
    "Fish Flag": DredgeItemData(ItemClassification.filler, 94),
    "Anchor Flag": DredgeItemData(ItemClassification.filler, 95),
    "Hook Flag": DredgeItemData(ItemClassification.filler, 96),
    "Pirate Flag": DredgeItemData(ItemClassification.filler, 97),
    "Eye Flag": DredgeItemData(ItemClassification.filler, 98),
    "Serpent Flag": DredgeItemData(ItemClassification.filler, 99),
    "Ouroboros Flag": DredgeItemData(ItemClassification.filler, 100),

    "6th, 7th March 1927 Message Bottle": DredgeItemData(ItemClassification.filler, 101),
    "1st June 1927 Message Bottle": DredgeItemData(ItemClassification.filler, 102),
    "20th August 1927 Message Bottle": DredgeItemData(ItemClassification.filler, 103),
    "21st August 1927 Message Bottle": DredgeItemData(ItemClassification.filler, 104),
    "9th September 1927 Message Bottle": DredgeItemData(ItemClassification.filler, 105),
    "14th September 1927 Message Bottle": DredgeItemData(ItemClassification.filler, 106),
    "??? (Twisted Strand) Message Bottle": DredgeItemData(ItemClassification.filler, 107),
    "??? (Devil's Spine) Message Bottle": DredgeItemData(ItemClassification.filler, 108),
    "Artifact Manifest Message Bottle": DredgeItemData(ItemClassification.filler, 109),
    "Tattered Receipt Message Bottle": DredgeItemData(ItemClassification.filler, 110),
    "Fisherman's Note": DredgeItemData(ItemClassification.filler, 111),
    "Ragged Note": DredgeItemData(ItemClassification.filler, 112)
}

createable_filler_items = {
    "Random Trinket": DredgeItemData(ItemClassification.filler, 113),
    "Random Fish": DredgeItemData(ItemClassification.filler, 114),
    "Small Ice Block": DredgeItemData(ItemClassification.filler, 115),
}

blackstone_key_items = {
    "Arterial Engine": DredgeItemData(ItemClassification.useful, 116),
    "Sign of Ruin": DredgeItemData(ItemClassification.useful, 117)
}

pale_reach_items = {
    "Barbed Ice Rod": DredgeItemData(ItemClassification.progression, 118),
    "Glacial Lance": DredgeItemData(ItemClassification.progression, 119),
    "Brittle Trawl Net": DredgeItemData(ItemClassification.progression, 120),
    "Radiant Trawl Net": DredgeItemData(ItemClassification.progression, 121),
    "Book of Astral Symbols": DredgeItemData(ItemClassification.progression_skip_balancing, 122),
    "Icebreaker": DredgeItemData(ItemClassification.progression, 123)
}

pale_reach_quest_items = {
    "Ice Axe": DredgeItemData(ItemClassification.progression, 124, 4),
    "Icebreaker Plow Half": DredgeItemData(ItemClassification.progression, 125, 2),
    "Icebreaker Bracing": DredgeItemData(ItemClassification.progression, 126),
    "Ice Shaper": DredgeItemData(ItemClassification.progression, 127),
    "Frozen Heart": DredgeItemData(ItemClassification.progression, 128, 4)
}

pale_reach_filler_items = {
    "Captain's Log - 30th May, 1847": DredgeItemData(ItemClassification.filler, 129),
    "Captain's Log - 1st June, 1847": DredgeItemData(ItemClassification.filler, 130),
    "Captain's Log - 5th June 1847": DredgeItemData(ItemClassification.filler, 131),
    "Leather Journal - 4th June, 1847": DredgeItemData(ItemClassification.filler, 132),
    "Leather Journal - 7th June, 1847": DredgeItemData(ItemClassification.filler, 133),
    "Leather Journal - 8th June, 1847": DredgeItemData(ItemClassification.filler, 134),
    "Tattered Diary - 2nd June, 1847": DredgeItemData(ItemClassification.filler, 135),
    "Tattered Diary - 4th June, 1847": DredgeItemData(ItemClassification.filler, 136),
    "Tattered Diary - 5th June, 1847": DredgeItemData(ItemClassification.filler, 137)
}

"""
trap_items = {
    "Crow Swarm Trap": DredgeItemData(ItemClassification.trap) # Summon the crows to harass you
    "Infection Trap": DredgeItemData(ItemClassification.trap) # Infect a random fish on board
    # One where it spawns the angler fish guy behind you for a little while
    "Instant Damage Trap": DredgeItemData(ItemClassification.trap) # Instantly damage the ship once
    "Time Travel Trap": DredgeItemData(ItemClassification.trap) # Advances time 12 hours forward
}
"""

item_data_table = {
    **equipment_items,
    **abilities,
    **ship_upgrades,
    **relics,
    **upgrade_materials,
    **quest_items,
    **filler_items,
    **createable_filler_items,
    **blackstone_key_items,
    **pale_reach_items,
    **pale_reach_quest_items}

item_categories = {
    "Coastal Rods":  {"Basic Fishing Pole", "Sinew Spindle", "Flexible Fish Pole",
                      "Anti-Tangle Line", "Versatile Rod", "Harvesting Platform"},

    "Coastal Nets":  {"Basic Net", "Improved Trawl Net", "Tempered Mesh Net",
                      "Large Trawl Net", "Heavy-Duty Trawl Net", "Radiant Trawl Net"},

    "Shallow Rods":  {"Simple Skimmer", "Weighted Line", "Sinew Spindle", "Flexible Fish Pole",
                      "Heat Resistant Line", "Versatile Rod", "Harvesting Platform", "Tendon Rod"},

    "Shallow Nets":  {"Silt Filtering Trawl Net", "Large Trawl Net", "Radiant Trawl Net"},

    "Oceanic Rods":  {"Hydraulic Rod", "Harvesting Platform", "Fathomless Winch",
                      "Tendon Rod", "Glacial Lance"},

    "Oceanic Nets":  {"Heavy-Duty Trawl Net", "Radiant Trawl Net"},

    "Abyssal Rods":  {"Bottomless Lines", "Fathomless Winch", "Sampling Device",
                      "Viscera Crane"},

    "Hadal Rods":    {"Bottomless Lines", "Fathomless Winch", "Viscera Crane"},

    "Mangrove Rods": {"Anti-Tangle Line", "Versatile Rod", "Tendon Rod"},

    "Mangrove Nets": {"Silt Filtering Trawl Net"},

    "Volcanic Rods": {"Heat Resistant Line", "Versatile Rod"},

    "Volcanic Nets": {"Tempered Mesh Net"},

    "Ice Rods":      {"Barbed Ice Rod", "Glacial Lance"},

    "Ice Nets":      {"Brittle Trawl Net", "Radiant Trawl Net"},

    "Crab Pots":     {"Basic Crab Pot", "Efficient Crab Pot", "Hardy Crab Pot",
                      "Large Crab Pot", "Complex Crab Pot", "Massive Crab Pot",
                      "Reinforced Crab Pot", "Mouth of the Deep"},

    "Relics":        {"Ornate Key", "Rusted Music Box", "Jewel Encrusted Band",
                      "Shimmering Necklace", "Antique Pocket Watch"},

    "Books":         {"Sustainable Fishing", "Rods, Reels, and Rigs", "Correct Engine Operation",
                      "Engineer's Companion", "A Plan for the Future", "Art of the Silver Tongue", "Advanced Fishing",
                      "Getting over it with Mind and Body", "Haggling and Bartering: A Guide", "The Relaxed Mind",
                      "Pushing the Limit: Engines", "Nautical Engineering", "Book of Astral Symbols"},

    "Abilities":     {"Haste", "Manifest", "Atrophy", "Banishment"},

    "Engines":       {"Peculiar Engine", "Arterial Engine", "Weak Valve Engine",
                      "Rusty Outboard Engine", "Improved Outboard", "Refined Outboard Engine",
                      "Jet Drive Engine", "Twin Prop Engine", "Twin Jet Drive Engine", "Engine Stack"}
}

item_name_to_id = {name: data.code + base_id for name, data in item_data_table.items()}
