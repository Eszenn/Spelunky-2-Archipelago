from typing import NamedTuple, Optional

from BaseClasses import Location


class DredgeLocation(Location):
    game = "DREDGE"


# Gotta add flag "quest" locations somewhere
class DredgeLocationData(NamedTuple):
    region: str
    address: Optional[int] = None


base_id: int = 379366373343000

fish_entries = {
    # The Marrows Encyclopedia Entries
    "Blue Mackerel Encyclopedia Entry": DredgeLocationData("The Marrows", 1),
    "Cod Encyclopedia Entry": DredgeLocationData("The Marrows", 2),
    "Arrow Squid Encyclopedia Entry": DredgeLocationData("The Marrows", 3),
    "Grey Eel Encyclopedia Entry": DredgeLocationData("The Marrows", 4),
    "Gulf Flounder Encyclopedia Entry": DredgeLocationData("The Marrows", 5),
    "Black Grouper Encyclopedia Entry": DredgeLocationData("The Marrows", 6),
    "Stingray Encyclopedia Entry": DredgeLocationData("The Marrows", 7),
    "Sailfish Encyclopedia Entry": DredgeLocationData("The Marrows", 8),
    "Bronze Whaler Encyclopedia Entry": DredgeLocationData("The Marrows", 9),
    "Blacktip Reef Shark Encyclopedia Entry": DredgeLocationData("The Marrows", 10),
    "Common Crab Encyclopedia Entry": DredgeLocationData("The Marrows", 11),
    "Fiddler Crab Encyclopedia Entry": DredgeLocationData("The Marrows", 12),

    # Gale Cliffs Fish
    "Oceanic Perch Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 13),
    "Tiger Mackerel Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 14),
    "Black Sea Bass Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 15),
    "Stonefish Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 16),
    "Blackmouth Salmon Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 17),
    "Conger Eel Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 18),
    "Devil Ray Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 19),
    "Sturgeon Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 20),
    "Wreckfish Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 21),
    "Rock Crab Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 22),
    "Decorator Crab Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 23),
    "Oarfish Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 24),

    # Stellar Basin Fish
    "Aurora Jellyfish Encyclopedia Entry": DredgeLocationData("Stellar Basin", 25),
    "Fangtooth Encyclopedia Entry": DredgeLocationData("Stellar Basin", 26),
    "Barreleye Encyclopedia Entry": DredgeLocationData("Stellar Basin", 27),
    "Firefly Squid Encyclopedia Entry": DredgeLocationData("Stellar Basin", 28),
    "Red Snapper Encyclopedia Entry": DredgeLocationData("Stellar Basin", 29),
    "Giant Amphipod Encyclopedia Entry": DredgeLocationData("Stellar Basin", 30),
    "Loosejaw Encyclopedia Entry": DredgeLocationData("Stellar Basin", 31),
    "Snailfish Encyclopedia Entry": DredgeLocationData("Stellar Basin", 32),
    "Coral Grouper Encyclopedia Entry": DredgeLocationData("Stellar Basin", 33),
    "Glowing Octopus Encyclopedia Entry": DredgeLocationData("Stellar Basin", 34),
    "Anglerfish Encyclopedia Entry": DredgeLocationData("Stellar Basin", 35),
    "Barracuda Encyclopedia Entry": DredgeLocationData("Stellar Basin", 36),
    "Hammerhead Shark Encyclopedia Entry": DredgeLocationData("Stellar Basin", 37),
    "Crown of Thorns Encyclopedia Entry": DredgeLocationData("Stellar Basin", 38),
    "Blue Crab Encyclopedia Entry": DredgeLocationData("Stellar Basin", 39),
    "Spiny Lobster Encyclopedia Entry": DredgeLocationData("Stellar Basin", 40),
    "Gulper Eel Encyclopedia Entry": DredgeLocationData("Stellar Basin", 41),

    # Twisted Strand Fish
    "Grey Mullet Encyclopedia Entry": DredgeLocationData("Twisted Strand", 42),
    "Tarpon Encyclopedia Entry": DredgeLocationData("Twisted Strand", 43),
    "Sergeant Fish Encyclopedia Entry": DredgeLocationData("Twisted Strand", 44),
    "Gar Encyclopedia Entry": DredgeLocationData("Twisted Strand", 45),
    "Longfin Eel Encyclopedia Entry": DredgeLocationData("Twisted Strand", 46),
    "Catfish Encyclopedia Entry": DredgeLocationData("Twisted Strand", 47),
    "Horseshoe Crab Encyclopedia Entry": DredgeLocationData("Twisted Strand", 48),
    "Giant Mud Crab Encyclopedia Entry": DredgeLocationData("Twisted Strand", 49),
    "Goliath Tigerfish Encyclopedia Entry": DredgeLocationData("Twisted Strand", 50),

    # Devil's Spine Fish
    "Armored Searobin Encyclopedia Entry": DredgeLocationData("Devil's Spine", 51),
    "Cusk Eel Encyclopedia Entry": DredgeLocationData("Devil's Spine", 52),
    "Snake Mackerel Encyclopedia Entry": DredgeLocationData("Devil's Spine", 53),
    "Pale Skate Encyclopedia Entry": DredgeLocationData("Devil's Spine", 54),
    "Ghost Shark Encyclopedia Entry": DredgeLocationData("Devil's Spine", 55),
    "Frilled Shark Encyclopedia Entry": DredgeLocationData("Devil's Spine", 56),
    "Volcano Snail Encyclopedia Entry": DredgeLocationData("Devil's Spine", 57),
    "Squat Lobster Encyclopedia Entry": DredgeLocationData("Devil's Spine", 58),
    "Spider Crab Encyclopedia Entry": DredgeLocationData("Devil's Spine", 59),
    "Coelacanth Encyclopedia Entry": DredgeLocationData("Devil's Spine", 60),

    # Open Ocean Fish
    "Anchovy Encyclopedia Entry": DredgeLocationData("Open Ocean", 61),
    "Scarlet Prawn Encyclopedia Entry": DredgeLocationData("Open Ocean", 62),
    "Blackfin Tuna Encyclopedia Entry": DredgeLocationData("Open Ocean", 63),
    "Viperfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 64),
    "Moonfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 65),
    "Rattail Encyclopedia Entry": DredgeLocationData("Open Ocean", 66),
    "Ocean Sunfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 67)
}

aberration_entries = {
    # The Marrows Aberrations
    "Grotesque Mackerel Encyclopedia Entry": DredgeLocationData("The Marrows", 68),
    "Lumpy Mackerel Encyclopedia Entry": DredgeLocationData("The Marrows", 69),
    "Many-Eyed Mackerel Encyclopedia Entry": DredgeLocationData("The Marrows", 70),
    "All-Seeing Cod Encyclopedia Entry": DredgeLocationData("The Marrows", 71),
    "Fanged Cod Encyclopedia Entry": DredgeLocationData("The Marrows", 72),
    "Three-Headed Cod Encyclopedia Entry": DredgeLocationData("The Marrows", 73),
    "Brood Squid Encyclopedia Entry": DredgeLocationData("The Marrows", 74),
    "Snag Squid Encyclopedia Entry": DredgeLocationData("The Marrows", 75),
    "Barbed Eel Encyclopedia Entry": DredgeLocationData("The Marrows", 76),
    "Host Eel Encyclopedia Entry": DredgeLocationData("The Marrows", 77),
    "Cyclopean Flounder Encyclopedia Entry": DredgeLocationData("The Marrows", 78),
    "Riddled Flounder Encyclopedia Entry": DredgeLocationData("The Marrows", 79),
    "Tusked Grouper Encyclopedia Entry": DredgeLocationData("The Marrows", 80),
    "Voltaic Grouper Encyclopedia Entry": DredgeLocationData("The Marrows", 81),
    "Shard Ray Encyclopedia Entry": DredgeLocationData("The Marrows", 82),
    "Sallow Sailfish Encyclopedia Entry": DredgeLocationData("The Marrows", 83),
    "Hooked Sailfish Encyclopedia Entry": DredgeLocationData("The Marrows", 84),
    "Bloodskin Shark Encyclopedia Entry": DredgeLocationData("The Marrows", 85),
    "Cleft-Mouth Shark Encyclopedia Entry": DredgeLocationData("The Marrows", 86),
    "Cerebral Crab Encyclopedia Entry": DredgeLocationData("The Marrows", 87),
    "Malignant Pincer Encyclopedia Entry": DredgeLocationData("The Marrows", 88),

    # Gale Cliffs Aberrations
    "Gnashing Perch Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 89),
    "Flayed Mackerel Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 90),
    "Bearded Mackerel Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 91),
    "Scouring Bass Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 92),
    "Gelatinous Stonefish Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 93),
    "Enthralled Stonefish Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 94),
    "Decaying Blackmouth Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 95),
    "Sprouting Eel Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 96),
    "Withered Ray Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 97),
    "Translucent Sturgeon Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 98),
    "Shattered Wreckfish Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 99),
    "Bony Wreckfish Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 100),
    "Splintered Crab Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 101),
    "Cortex Decorator Encyclopedia Entry": DredgeLocationData("Gale Cliffs", 102),

    # Stellar Basin Aberrations
    "Parhelion Jellyfish Encyclopedia Entry": DredgeLocationData("Stellar Basin", 103),
    "Cursed Fangtooth Encyclopedia Entry": DredgeLocationData("Stellar Basin", 104),
    "Voideye Encyclopedia Entry": DredgeLocationData("Stellar Basin", 105),
    "Radiant Squid Encyclopedia Entry": DredgeLocationData("Stellar Basin", 106),
    "Blood Snapper Encyclopedia Entry": DredgeLocationData("Stellar Basin", 107),
    "Latching Snapper Encyclopedia Entry": DredgeLocationData("Stellar Basin", 108),
    "Ruptured Vessel Encyclopedia Entry": DredgeLocationData("Stellar Basin", 109),
    "Perished Loosejaw Encyclopedia Entry": DredgeLocationData("Stellar Basin", 110),
    "Calcified Snailfish Encyclopedia Entry": DredgeLocationData("Stellar Basin", 111),
    "Seizing Snailfish Encyclopedia Entry": DredgeLocationData("Stellar Basin", 112),
    "Consumed Grouper Encyclopedia Entry": DredgeLocationData("Stellar Basin", 113),
    "Medusa Octopus Encyclopedia Entry": DredgeLocationData("Stellar Basin", 114),
    "Bursting Anglerfish Encyclopedia Entry": DredgeLocationData("Stellar Basin", 115),
    "Savage Barracuda Encyclopedia Entry": DredgeLocationData("Stellar Basin", 116),
    "Concertina Barracuda Encyclopedia Entry": DredgeLocationData("Stellar Basin", 117),
    "Gazing Shark Encyclopedia Entry": DredgeLocationData("Stellar Basin", 118),
    "Crown of Nadir Encyclopedia Entry": DredgeLocationData("Stellar Basin", 119),
    "Entangled Crab Encyclopedia Entry": DredgeLocationData("Stellar Basin", 120),
    "Imperious Lobster Encyclopedia Entry": DredgeLocationData("Stellar Basin", 121),

    # Twisted Strand Aberrations
    "Entwined Mullet Encyclopedia Entry": DredgeLocationData("Twisted Strand", 122),
    "Gleaming Mullet Encyclopedia Entry": DredgeLocationData("Twisted Strand", 123),
    "Blistered Tarpon Encyclopedia Entry": DredgeLocationData("Twisted Strand", 124),
    "Vortex Interloper Encyclopedia Entry": DredgeLocationData("Twisted Strand", 125),
    "Clawfin Gar Encyclopedia Entry": DredgeLocationData("Twisted Strand", 126),
    "Grinning Gar Encyclopedia Entry": DredgeLocationData("Twisted Strand", 127),
    "Twinned Eels Encyclopedia Entry": DredgeLocationData("Twisted Strand", 128),
    "Nightwing Catfish Encyclopedia Entry": DredgeLocationData("Twisted Strand", 129),
    "Effigy Crab Encyclopedia Entry": DredgeLocationData("Twisted Strand", 130),
    "Mire Screecher Encyclopedia Entry": DredgeLocationData("Twisted Strand", 131),

    # Devil's Spine Aberrations
    "Ossified Searobin Encyclopedia Entry": DredgeLocationData("Devil's Spine", 132),
    "Infernal Eel Encyclopedia Entry": DredgeLocationData("Devil's Spine", 133),
    "Serpentine Mackerel Encyclopedia Entry": DredgeLocationData("Devil's Spine", 134),
    "Tattered Mackerel Encyclopedia Entry": DredgeLocationData("Devil's Spine", 135),
    "Defaced Skate Encyclopedia Entry": DredgeLocationData("Devil's Spine", 136),
    "Rapt Shark Encyclopedia Entry": DredgeLocationData("Devil's Spine", 137),
    "Twisted Shark Encyclopedia Entry": DredgeLocationData("Devil's Spine", 138),
    "Grasping Snail Encyclopedia Entry": DredgeLocationData("Devil's Spine", 139),
    "Sable Reacher Encyclopedia Entry": DredgeLocationData("Devil's Spine", 140),
    "Umbral Puppet Encyclopedia Entry": DredgeLocationData("Devil's Spine", 141),

    # Open Ocean Aberrations
    "Anchovy King Encyclopedia Entry": DredgeLocationData("Open Ocean", 142),
    "Leeching Prawn Encyclopedia Entry": DredgeLocationData("Open Ocean", 143),
    "Razormouth Tuna Encyclopedia Entry": DredgeLocationData("Open Ocean", 144),
    "Decrepit Viperfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 145),
    "Collapsed Viperfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 146),
    "Skeletal Moonfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 147),
    "Beaked Moonfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 148),
    "Congealed Rattail Encyclopedia Entry": DredgeLocationData("Open Ocean", 149),
    "Charred Sunfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 150),
    "Glaring Sunfish Encyclopedia Entry": DredgeLocationData("Open Ocean", 151),
}

pursuit_rewards = {
    "A Place to Rest: Research Part 1": DredgeLocationData("The Marrows", 152),
    "A Place to Rest: Research Part 2": DredgeLocationData("The Marrows", 153),
    "A Place to Rest: The Engineer's Companion": DredgeLocationData("The Marrows", 154),

    "Best Before: $150": DredgeLocationData("Gale Cliffs", 155),

    "Castaway: Signet Ring": DredgeLocationData("The Marrows", 156),

    "Craven Courier: Getting Over it with Mind and Body": DredgeLocationData("The Marrows", 157),

    "Caught to Order: Basic Crab Pot": DredgeLocationData("The Marrows", 158),
    "Caught to Order: Research Part 1": DredgeLocationData("The Marrows", 159),
    "Caught to Order: Research Part 2": DredgeLocationData("The Marrows", 160),

    "Figure in Blue: Haggling and Bartering: A Guide": DredgeLocationData("Open Ocean", 161),
    "Figure in Gold: Advanced Fishing": DredgeLocationData("Open Ocean", 162),
    "Figure in Purple: Pushing the Limits: Engines": DredgeLocationData("Open Ocean", 163),
    "Figure in Red: Nautical Engineering": DredgeLocationData("Open Ocean", 164),

    "Flames of the Deep: Ghost Rock Slab Research Part": DredgeLocationData("Devil's Spine", 165),
    "Flames of the Deep: Ghost Rock Slab Refined Metal 1": DredgeLocationData("Devil's Spine", 166),
    "Flames of the Deep: Ghost Rock Slab Refined Metal 2": DredgeLocationData("Devil's Spine", 167),
    "Flames of the Deep: Crab Rock Slab Research Part": DredgeLocationData("Devil's Spine", 168),
    "Flames of the Deep: Crab Rock Slab Lumber": DredgeLocationData("Devil's Spine", 169),
    "Flames of the Deep: Crab Rock Slab TRINKET 1": DredgeLocationData("Devil's Spine", 170),  # Find out what trinkets actually go here
    "Flames of the Deep: Crab Rock Slab TRINKET 2": DredgeLocationData("Devil's Spine", 171),
    "Flames of the Deep: Aberration Rock Slab Encrusted Talisman": DredgeLocationData("Devil's Spine", 172),

    "Grotesque Fish: Dredging Equipment": DredgeLocationData("The Marrows", 173),

    "Hermitage: Packed Explosives": DredgeLocationData("Gale Cliffs", 174),

    "Lost at Sea: Research Part": DredgeLocationData("The Marrows", 175),

    "Lost Dog: TRINKET": DredgeLocationData("Stellar Basin", 176),  # Find out what trinket actually goes here

    "Package Delivery: Sustainable Fishing": DredgeLocationData("The Marrows", 177),

    "Recording Rarities: Oarfish Research Part 1": DredgeLocationData("Gale Cliffs", 178),
    "Recording Rarities: Oarfish Research Part 2": DredgeLocationData("Gale Cliffs", 179),
    "Recording Rarities: Gulper Eel Research Part 1": DredgeLocationData("Stellar Basin", 180),
    "Recording Rarities: Gulper Eel Research Part 2": DredgeLocationData("Stellar Basin", 181),
    "Recording Rarities: Goliath Tigerfish Research Part 1": DredgeLocationData("Twisted Strand", 182),
    "Recording Rarities: Goliath Tigerfish Research Part 2": DredgeLocationData("Twisted Strand", 183),
    "Recording Rarities: Coelacanth Research Part 1": DredgeLocationData("Devil's Spine", 184),
    "Recording Rarities: Coelacanth Research Part 2": DredgeLocationData("Devil's Spine", 185),

    "Research Assistant: Sampling Device": DredgeLocationData("Stellar Basin", 186),
    "Research Assistant: Research Part": DredgeLocationData("Stellar Basin", 187),
    "Research Assistant: A Plan for the Future": DredgeLocationData("Stellar Basin", 188),

    "Stone Tablets: Flame of the Sky": DredgeLocationData("Devil's Spine", 189),
    "Stone Tablets: Goblet 1": DredgeLocationData("Devil's Spine", 190),
    "Stone Tablets: Goblet 2": DredgeLocationData("Devil's Spine", 191),
    "Stone Tablets: Citrine Ring 1": DredgeLocationData("Devil's Spine", 192),
    "Stone Tablets: Citrine Ring 2": DredgeLocationData("Devil's Spine", 193),

    "The Collector: Haste": DredgeLocationData("The Marrows", 194),
    "The Collector: Manifest": DredgeLocationData("The Marrows", 195),
    "The Collector: Banish": DredgeLocationData("The Marrows", 196),
    "The Collector: Atrophy": DredgeLocationData("The Marrows", 197)
}

pursuit_quest_items = {
    "Craven Courier: Large Package": DredgeLocationData("The Marrows", 198),

    "Flames of the Deep: Ghost Rock Slab Fathomless Flame": DredgeLocationData("Devil's Spine", 199),
    "Flames of the Deep: Crab Rock Slab Fathomless Flame": DredgeLocationData("Devil's Spine", 200),
    "Flames of the Deep: Aberration Rock Slab Fathomless Flame": DredgeLocationData("Devil's Spine", 201),

    "Grotesque Fish: Handkerchief": DredgeLocationData("The Marrows", 202),

    "Hermitage: Family Crest": DredgeLocationData("Gale Cliffs", 203),

    "Lost at Sea: Bronze Belt Buckle": DredgeLocationData("The Marrows", 204),

    "Package Delivery: Small Package": DredgeLocationData("The Marrows", 205),

    "Research Assistant: Prototype Parts": DredgeLocationData("Stellar Basin", 206),
    "Research Assistant: Repulsion Machine": DredgeLocationData("Stellar Basin", 207),

    "Stone Tablets: Stone Tablet 1": DredgeLocationData("Devil's Spine", 208),
    "Stone Tablets: Stone Tablet 2": DredgeLocationData("Devil's Spine", 209),
    "Stone Tablets: Stone Tablet 3": DredgeLocationData("Devil's Spine", 210),
    "Stone Tablets: Fused Tablet": DredgeLocationData("Devil's Spine", 211),  # REDO ID'S FROM HERE

    "The Bitter End: Mortar Barrel": DredgeLocationData("Twisted Strand", 212),
    "The Bitter End: Mortar Frame": DredgeLocationData("Twisted Strand", 213),
    "The Bitter End: Pungent Bait": DredgeLocationData("Twisted Strand", 214),
    "The Bitter End: Fetid Bait": DredgeLocationData("Twisted Strand", 215),
    "The Bitter End: Reeking Bait": DredgeLocationData("Twisted Strand", 216),
    "The Bitter End: Chunk of Flesh 1": DredgeLocationData("Twisted Strand", 217),
    "The Bitter End: Chunk of Flesh 2": DredgeLocationData("Twisted Strand", 218),
    "The Bitter End: Chunk of Flesh 3": DredgeLocationData("Twisted Strand", 219),
}

relic_shuffle_locations = {
    "The Collector: Ornate Key": DredgeLocationData("The Marrows", 220),
    "The Collector: Rusted Music Box": DredgeLocationData("Gale Cliffs", 221),
    "The Collector: Jewel Encrusted Band": DredgeLocationData("Stellar Basin", 222),
    "The Collector: Shimmering Necklace": DredgeLocationData("Twisted Strand", 223),
    "The Collector: Antique Pocket Watch": DredgeLocationData("Devil's Spine", 224)
}

messages = {
    "6th, 7th March 1927 Message Bottle": DredgeLocationData("Stellar Basin", 225),
    "1st June 1927 Message Bottle": DredgeLocationData("Devil's Spine", 226),
    "20th August 1927 Message Bottle": DredgeLocationData("The Marrows", 227),
    "21st August 1927 Message Bottle": DredgeLocationData("The Marrows", 228),
    "9th September 1927 Message Bottle": DredgeLocationData("Gale Cliffs", 229),
    "14th September 1927 Message Bottle": DredgeLocationData("Stellar Basin", 230),
    "??? (Twisted Strand) Message Bottle": DredgeLocationData("Twisted Strand", 231),
    "??? (Devil's Spine) Message Bottle": DredgeLocationData("Devil's Spine", 232),
    "Artifact Manifest Message Bottle": DredgeLocationData("Gale Cliffs", 233),
    "Tattered Receipt Message Bottle": DredgeLocationData("Twisted Strand", 234),
    "Fisherman's Note": DredgeLocationData("Open Ocean", 235),
    "Ragged Note": DredgeLocationData("Open Ocean", 236)
}

# Verify ALL Shipwreck locations - there are others I guess
# Include Planewrecks here
shipwrecks = {
    "Shipwreck [J8] Item 1": DredgeLocationData("The Marrows", 237),
    "Shipwreck [J8] Item 2": DredgeLocationData("The Marrows", 238),
    "Shipwreck [J8] Item 3": DredgeLocationData("The Marrows", 239),
    "Shipwreck [J8] Item 4": DredgeLocationData("The Marrows", 240),
    "Shipwreck [J8] Item 5": DredgeLocationData("The Marrows", 241),

    "Shipwreck [G4] Item 1": DredgeLocationData("Stellar Basin", 242),
    "Shipwreck [G4] Item 2": DredgeLocationData("Stellar Basin", 243),
    "Shipwreck [G4] Item 3": DredgeLocationData("Stellar Basin", 244),
    "Shipwreck [G4] Item 4": DredgeLocationData("Stellar Basin", 245),

    "Shipwreck [D3] Item 1": DredgeLocationData("Stellar Basin", 246),
    "Shipwreck [D3] Item 2": DredgeLocationData("Stellar Basin", 247),
    "Shipwreck [D3] Item 3": DredgeLocationData("Stellar Basin", 248),

    "Shipwreck [L10] Item 1": DredgeLocationData("Open Ocean", 249),
    "Shipwreck [L10] Item 2": DredgeLocationData("Open Ocean", 250),
    "Shipwreck [L10] Item 3": DredgeLocationData("Open Ocean", 251),
    "Shipwreck [L10] Item 4": DredgeLocationData("Open Ocean", 252),

    "Shipwreck [M6] Item 1": DredgeLocationData("Open Ocean", 253),
    "Shipwreck [M6] Item 2": DredgeLocationData("Open Ocean", 254),
    "Shipwreck [M6] Item 3": DredgeLocationData("Open Ocean", 255),
    "Shipwreck [M6] Item 4": DredgeLocationData("Open Ocean", 256),

    "Shipwreck [P6] Item 1": DredgeLocationData("Open Ocean", 257),
    "Shipwreck [P6] Item 2": DredgeLocationData("Open Ocean", 258),
    "Shipwreck [P6] Item 3": DredgeLocationData("Open Ocean", 259),

    "Planewreck [E14] Item 1": DredgeLocationData("Twisted Strand", 260),
    "Planewreck [E14] Item 2": DredgeLocationData("Twisted Strand", 261),
    "Planewreck [E14] Item 3": DredgeLocationData("Twisted Strand", 262),

    "Planewreck [D12] Item 1": DredgeLocationData("Twisted Strand", 263),
    "Planewreck [D12] Item 2": DredgeLocationData("Twisted Strand", 264),
    "Planewreck [D12] Item 3": DredgeLocationData("Twisted Strand", 265)
}

shrines = {
    "Cod Shrine": DredgeLocationData("The Marrows", 266),
    "Crab Shrine": DredgeLocationData("Gale Cliffs", 267),
    "Aberration Shrine": DredgeLocationData("Twisted Strand", 268),
    "Shark Shrine": DredgeLocationData("Open Ocean", 269)
}

chests = {
    "Rotten Treasure Chest Item 1": DredgeLocationData("Gale Cliffs", 270),
    "Rotten Treasure Chest Item 2": DredgeLocationData("Gale Cliffs", 271),

    "Floating Treasure Chest Item 1": DredgeLocationData("Open Ocean", 272),
    "Floating Treasure Chest Item 2": DredgeLocationData("Open Ocean", 273),
    "Floating Treasure Chest Item 3": DredgeLocationData("Open Ocean", 274),
    "Floating Treasure Chest Item 4": DredgeLocationData("Open Ocean", 275),
    "Floating Treasure Chest Item 5": DredgeLocationData("Open Ocean", 276),
    "Floating Treasure Chest Item 6": DredgeLocationData("Open Ocean", 277),
}

research_tree = {
    # Fishing Rods
    "Research Tree: Flexible Fishing Pole": DredgeLocationData("Menu", 278),
    "Research Tree: Heat-Resistant Line": DredgeLocationData("Menu", 279),
    "Research Tree: Anti-Tangle Line": DredgeLocationData("Menu", 280),
    "Research Tree: Versatile Rod": DredgeLocationData("Menu", 281),
    "Research Tree: Hydraulic Rod": DredgeLocationData("Menu", 282),
    "Research Tree: Harvesting Platform": DredgeLocationData("Menu", 283),
    "Research Tree: Bottomless Lines": DredgeLocationData("Menu", 284),
    "Research Tree: Fathomless Winch": DredgeLocationData("Menu", 285),

    # Engines
    "Research Tree: Improved Outboard Engine": DredgeLocationData("Menu", 286),
    "Research Tree: Jet Drive Engine": DredgeLocationData("Menu", 287),
    "Research Tree: Refined Outboard Engine": DredgeLocationData("Menu", 288),
    "Research Tree: Twin Prop Engine": DredgeLocationData("Menu", 289),
    "Research Tree: Twin Jet Drive Engine": DredgeLocationData("Menu", 290),
    "Research Tree: Engine Stack": DredgeLocationData("Menu", 291),

    # Crab Pots
    "Research Tree: Efficient Crab Pot": DredgeLocationData("Menu", 292),
    "Research Tree: Hardy Crab Pot": DredgeLocationData("Menu", 293),
    "Research Tree: Large Crab Pot": DredgeLocationData("Menu", 294),
    "Research Tree: Complex Crab Pot": DredgeLocationData("Menu", 295),
    "Research Tree: Massive Crab Pot": DredgeLocationData("Menu", 296),
    "Research Tree: Reinforced Crab Pot": DredgeLocationData("Menu", 297),

    # Trawl Nets
    "Research Tree: Improved Trawl Net": DredgeLocationData("Menu", 298),
    "Research Tree: Silt Filtering Trawl Net": DredgeLocationData("Menu", 299),
    "Research Tree: Large Trawl Net": DredgeLocationData("Menu", 300),
    "Research Tree: Heavy-Duty Trawl Net": DredgeLocationData("Menu", 301),
    "Research Tree: Tempered Mesh Net": DredgeLocationData("Menu", 302)
}

dry_dock = {
    "Ship Upgrade: Tier 1 +2 Rod Spaces": DredgeLocationData("Menu", 303),
    "Ship Upgrade: Tier 1 +4 Net Spaces": DredgeLocationData("Menu", 304),
    "Ship Upgrade: Tier 1 +2 Engine Spaces": DredgeLocationData("Menu", 305),
    "Ship Upgrade: Tier 1 +1 Light Space": DredgeLocationData("Menu", 306),
    "Ship Upgrade: Tier 2 Hull Upgrade": DredgeLocationData("Menu", 307),

    "Ship Upgrade: Tier 2 +3 Rod Spaces": DredgeLocationData("Menu", 308),
    "Ship Upgrade: Tier 2 +4 Cargo Spaces": DredgeLocationData("Menu", 309),
    "Ship Upgrade: Tier 2 +1 Engine Space": DredgeLocationData("Menu", 310),
    "Ship Upgrade: Tier 3 Hull Upgrade": DredgeLocationData("Menu", 311),

    "Ship Upgrade: Tier 3 +2 Rod Spaces": DredgeLocationData("Menu", 312),
    "Ship Upgrade: Tier 3 +2 Net Spaces": DredgeLocationData("Menu", 313),
    "Ship Upgrade: Tier 3 +4 Cargo Spaces": DredgeLocationData("Menu", 314),
    "Ship Upgrade: Tier 3 +1 Engine Space": DredgeLocationData("Menu", 315),
    "Ship Upgrade: Tier 3 +1 Light Space": DredgeLocationData("Menu", 316),
    "Ship Upgrade: Tier 4 Hull Upgrade": DredgeLocationData("Menu", 317),

    "Ship Upgrade: Tier 4 +2 Rod Spaces": DredgeLocationData("Menu", 318),
    "Ship Upgrade: Tier 4 +4 Cargo Spaces": DredgeLocationData("Menu", 319),
    "Ship Upgrade: Tier 4 +2 Engine Spaces": DredgeLocationData("Menu", 320),
    "Ship Upgrade: Tier 4 +1 Light Space": DredgeLocationData("Menu", 321),
}

blackstone_key_locations = {
    "Blackstone Isle Workshop: Arterial Engine": DredgeLocationData("The Marrows", 322),
    "Blackstone Isle Workshop: Sign of Ruin": DredgeLocationData("The Marrows", 323)
}

pale_reach_fish_entries = {
    "Icefish Encyclopedia Entry": DredgeLocationData("Pale Reach", 324),
    "Char Encyclopedia Entry": DredgeLocationData("Pale Reach", 325),
    "Wolffish Encyclopedia Entry": DredgeLocationData("Pale Reach", 326),
    "Stargazer Encyclopedia Entry": DredgeLocationData("Pale Reach", 327),
    "Lizardfish Encyclopedia Entry": DredgeLocationData("Pale Reach", 328),
    "Toothfish Encyclopedia Entry": DredgeLocationData("Pale Reach", 329),
    "Goblin Shark Encyclopedia Entry": DredgeLocationData("Pale Reach", 330),
    "Colossal Squid Encyclopedia Entry": DredgeLocationData("Pale Reach", 331),
    "Sea Stars Encyclopedia Entry": DredgeLocationData("Pale Reach", 332),
    "King Crab Encyclopedia Entry": DredgeLocationData("Pale Reach", 333),
    "Sleeper Shark Encyclopedia Entry": DredgeLocationData("Pale Reach", 334)
}

pale_reach_aberration_entries = {
    "Fractalline Icefish Encyclopedia Entry": DredgeLocationData("Pale Reach", 335),
    "Thawed Icefish Encyclopedia Entry": DredgeLocationData("Pale Reach", 336),
    "Astral Icefish Encyclopedia Entry": DredgeLocationData("Pale Reach", 337),
    "Bubbling Char Encyclopedia Entry": DredgeLocationData("Pale Reach", 338),
    "Hinged Wolffish Encyclopedia Entry": DredgeLocationData("Pale Reach", 339),
    "Craterous Seer Encyclopedia Entry": DredgeLocationData("Pale Reach", 340),
    "Feral Lizardfish Encyclopedia Entry": DredgeLocationData("Pale Reach", 341),
    "Bulbous Toothfish Encyclopedia Entry": DredgeLocationData("Pale Reach", 342),
    "Grisly Shark Encyclopedia Entry": DredgeLocationData("Pale Reach", 343),
    "Pale Grasper Encyclopedia Entry": DredgeLocationData("Pale Reach", 344),
    "Fallen Stars Encyclopedia Entry": DredgeLocationData("Pale Reach", 345),
    "King's Wreath Encyclopedia Entry": DredgeLocationData("Pale Reach", 346)
}

pale_reach_pursuit_rewards = {
    "Figure in White: Book of Astral Symbols": DredgeLocationData("Pale Reach", 347),

    "Icebreaker: Icebreaker": DredgeLocationData("Pale Reach", 348),

    "Ice Shaper: Ice Block 1": DredgeLocationData("Pale Reach", 349),
    "Ice Shaper: Ice Block 2": DredgeLocationData("Pale Reach", 350),

    "Under the Ice: Radiant Trawl Net": DredgeLocationData("Pale Reach", 351),
    "Under the Ice: Aurous Anchor": DredgeLocationData("Pale Reach", 352)
}

pale_reach_quest_items = {
    "Icebreaker: Left Icebreaker Plow Half": DredgeLocationData("Pale Reach", 353),
    "Icebreaker: Right Icebreaker Plow Half": DredgeLocationData("Pale Reach", 354),
    "Icebreaker: Icebreaker Bracing": DredgeLocationData("Pale Reach", 355),

    "Under the Ice: Ice Pick (Central Camp)": DredgeLocationData("Pale Reach", 356),
    "Under the Ice: Ice Pick (Eastern Terminus)": DredgeLocationData("Pale Reach", 357),
    "Under the Ice: Ice Pick (Western Bearing)": DredgeLocationData("Pale Reach", 358),
    "Under the Ice: Ice Pick (Southern Locus)": DredgeLocationData("Pale Reach", 359),
    "Under the Ice: Frozen Heart (Central Camp)": DredgeLocationData("Pale Reach", 360),
    "Under the Ice: Frozen Heart (Eastern Terminus)": DredgeLocationData("Pale Reach", 361),
    "Under the Ice: Frozen Heart (Western Bearing)": DredgeLocationData("Pale Reach", 362),
    "Under the Ice: Frozen Heart (Southern Locus)": DredgeLocationData("Pale Reach", 363)
}

pale_reach_messages = {
    "Captain's Log - 30th May, 1847": DredgeLocationData("Pale Reach", 364),
    "Captain's Log - 1st June, 1847": DredgeLocationData("Pale Reach", 365),
    "Captain's Log - 5th June, 1847": DredgeLocationData("Pale Reach", 366),
    "Leather Journal - 4th June, 1847": DredgeLocationData("Pale Reach", 367),
    "Leather Journal - 7th June, 1847": DredgeLocationData("Pale Reach", 368),
    "Leather Journal - 8th June, 1847": DredgeLocationData("Pale Reach", 369),
    "Tattered Diary - 2nd June, 1847": DredgeLocationData("Pale Reach", 370),
    "Tattered Diary - 4th June, 1847": DredgeLocationData("Pale Reach", 371),
    "Tattered Diary - 5th June, 1847": DredgeLocationData("Pale Reach", 372)
}

"""
# Include flags, trinkets, research parts, materials here
dredging_spots = {
    # Flags
    "Anchor Flag Dredge Spot [G2]": DredgeLocationData("Stellar Basin"),
    "Hook Flag Dredge Spot [H13]": DredgeLocationData("Open Ocean"),
    "Pirate Flag Dredge Spot [N2]": DredgeLocationData("Gale Cliffs"),
    "Eye Flag Dredge Spot [P14]": DredgeLocationData("Devil's Spine"),
    "Serpent Flag Dredge Spot [I10]": DredgeLocationData("Open Ocean"),
    "Ouroboros Flag Dredge Spot [L5]": DredgeLocationData("Open Ocean"),

    # Lumber
    "Lumber Dredge Spot [F15]": DredgeLocationData("Twisted Strand"),
    "Lumber Dredge Spot [G14]": DredgeLocationData("Twisted Strand"),
    "Lumber Dredge Spot [D12]": DredgeLocationData("Twisted Strand"),
    "Lumber Dredge Spot [H14]": DredgeLocationData("Open Ocean"),
    "Lumber Dredge Spot [O15]": DredgeLocationData("Devil's Spine"),
    "Lumber Dredge Spot [O13]": DredgeLocationData("Devil's Spine"),
    "Lumber Dredge Spot [K10]": DredgeLocationData("The Marrows"),
    "Lumber Dredge Spot [L10]": DredgeLocationData("The Marrows"),
    "Lumber Dredge Spot [K8] - North": DredgeLocationData("The Marrows"),
    "Lumber Dredge Spot [K8] - Southeast": DredgeLocationData("The Marrows"),
    "Lumber Dredge Spot [I6]": DredgeLocationData("Open Ocean"),
    "Lumber Dredge Spot [E4]": DredgeLocationData("Stellar Basin"),
    "Lumber Dredge Spot [D3]": DredgeLocationData("Stellar Basin"),
    "Lumber Dredge Spot [G2] - North": DredgeLocationData("Stellar Basin"),
    "Lumber Dredge Spot [G2] - South": DredgeLocationData("Stellar Basin"),
    "Lumber Dredge Spot [M4]": DredgeLocationData("Gale Cliffs"),
    "Lumber Dredge Spot [O5]": DredgeLocationData("Gale Cliffs"),
    "Lumber Dredge Spot [N3]": DredgeLocationData("Gale Cliffs"),
    "Lumber Dredge Spot [O2]": DredgeLocationData("Gale Cliffs"),
}
"""

location_data_table = {
    **fish_entries,
    **aberration_entries,
    **pursuit_rewards,
    **pursuit_quest_items,
    **relic_shuffle_locations,
    **messages,
    **shipwrecks,
    **shrines,
    **chests,
    **research_tree,
    **dry_dock,
    # **dredging_spots,
    **blackstone_key_locations,
    **pale_reach_fish_entries,
    **pale_reach_aberration_entries,
    **pale_reach_pursuit_rewards,
    **pale_reach_quest_items,
    **pale_reach_messages
}

location_name_to_id = {name: data.address + base_id for name, data in location_data_table.items()}
