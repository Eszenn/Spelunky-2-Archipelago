from typing import TYPE_CHECKING

from BaseClasses import CollectionState, MultiWorld
from worlds.generic.Rules import set_rule
if TYPE_CHECKING:
    from . import DredgeWorld


def has_coastal_rod(state: CollectionState, player: int) -> bool:
    return state.has_group("Coastal Rods", player)


def has_coastal_net(state: CollectionState, player: int) -> bool:
    return state.has_group("Coastal Nets", player)


def has_shallow_rod(state: CollectionState, player: int) -> bool:
    return state.has_group("Shallow Rods", player)


def has_shallow_net(state: CollectionState, player: int) -> bool:
    return state.has_group("Shallow Nets", player)


def has_oceanic_rod(state: CollectionState, player: int) -> bool:
    return state.has_group("Oceanic Rods", player)


def has_oceanic_net(state: CollectionState, player: int) -> bool:
    return state.has_group("Oceanic Nets", player)


def has_abyssal_rod(state: CollectionState, player: int) -> bool:
    return state.has_group("Abyssal Rods", player)


def has_hadal_rod(state: CollectionState, player: int) -> bool:
    return state.has_group("Hadal Rods", player)


def has_mangrove_rod(state: CollectionState, player: int) -> bool:
    return state.has_group("Mangrove Rods", player)


def has_mangrove_net(state: CollectionState, player: int) -> bool:
    return state.has_group("Mangrove Nets", player)


def has_volcanic_rod(state: CollectionState, player: int) -> bool:
    return state.has_group("Volcanic Rods", player)


def has_volcanic_net(state: CollectionState, player: int) -> bool:
    return state.has_group("Volcanic Nets", player)


def has_ice_rod(state: CollectionState, player: int) -> bool:
    return state.has_group("Ice Rods", player)


def has_ice_net(state: CollectionState, player: int) -> bool:
    return state.has_group("Ice Nets", player)


def has_crab_pot(state: CollectionState, player: int) -> bool:
    return state.has_group("Crab Pots", player)


def can_fish(state: CollectionState, player: int) -> bool:
    return (has_coastal_rod(state, player) or has_coastal_net(state, player) or
            has_shallow_rod(state, player) or has_shallow_net(state, player) or
            has_oceanic_rod(state, player) or has_oceanic_net(state, player) or
            has_abyssal_rod(state, player) or has_hadal_rod(state, player) or
            has_mangrove_rod(state, player) or has_mangrove_net(state, player) or
            has_volcanic_rod(state, player) or has_volcanic_net(state, player) or
            has_ice_rod(state, player) or has_ice_net(state, player) or
            has_crab_pot(state, player))


def has_dredging_equipment(state: CollectionState, player: int) -> bool:
    return state.has("Dredging Equipment", player)


def has_enough_parts(state: CollectionState, player: int, count: int) -> bool:
    # May need to also check cleared locations
    # May also need special handling for bottomless lines + fathomless winch
    return state.count("Research Part", player) >= count


def has_enough_materials(state: CollectionState, player: int,
                         lumber: int = 0, scrap: int = 0,
                         cloth: int = 0, metal: int = 0) -> bool:
    return (state.count("Lumber", player) >= lumber and
            state.count("Scrap Metal", player) >= scrap and
            state.count("Cloth", player) >= cloth and
            state.count("Refined Metal", player) >= metal)


def set_common_rules(world: "DredgeWorld", multiworld: MultiWorld):
    player = world.player

    # The Marrows Encyclopedia Entries
    set_rule(multiworld.get_location("Blue Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Cod Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Arrow Squid Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Grey Eel Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Gulf Flounder Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Black Grouper Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Stingray Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Sailfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Bronze Whaler Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Blacktip Reef Shark Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Common Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Fiddler Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))

    # Gale Cliffs Encyclopedia Entries
    set_rule(multiworld.get_location("Oceanic Perch Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Tiger Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Black Sea Bass Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Stonefish Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Blackmouth Salmon Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Conger Eel Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Devil Ray Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Sturgeon Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Wreckfish Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Rock Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Decorator Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Oarfish Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))

    # Stellar Basin Encyclopedia Entries
    set_rule(multiworld.get_location("Aurora Jellyfish Encyclopedia Entry", player),
             lambda state: has_coastal_net(state, player))
    set_rule(multiworld.get_location("Fangtooth Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Barreleye Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Firefly Squid Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Red Snapper Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Giant Amphipod Encyclopedia Entry", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Loosejaw Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Snailfish Encyclopedia Entry", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Coral Grouper Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Glowing Octopus Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_crab_pot(state, player))
    set_rule(multiworld.get_location("Anglerfish Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Barracuda Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Hammerhead Shark Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player))
    set_rule(multiworld.get_location("Crown of Thorns Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Blue Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Spiny Lobster Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Gulper Eel Encyclopedia Entry", player),
             lambda state: has_hadal_rod(state, player))

    # Twisted Strand Encyclopedia Entries
    set_rule(multiworld.get_location("Grey Mullet Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Tarpon Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Sergeant Fish Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player) or has_mangrove_net(state, player))
    set_rule(multiworld.get_location("Gar Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player) or has_mangrove_net(state, player))
    set_rule(multiworld.get_location("Longfin Eel Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player))
    set_rule(multiworld.get_location("Catfish Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player) or has_mangrove_net(state, player))
    set_rule(multiworld.get_location("Horseshoe Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Giant Mud Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Goliath Tigerfish Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player))

    # Devil's Spine Encyclopedia Entries
    set_rule(multiworld.get_location("Armored Searobin Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Cusk Eel Encyclopedia Entry", player),
             lambda state: has_volcanic_rod(state, player) or has_volcanic_net(state, player))
    set_rule(multiworld.get_location("Snake Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Pale Skate Encyclopedia Entry", player),
             lambda state: has_volcanic_rod(state, player) or has_volcanic_net(state, player))
    set_rule(multiworld.get_location("Ghost Shark Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Frilled Shark Encyclopedia Entry", player),
             lambda state: has_volcanic_rod(state, player))
    set_rule(multiworld.get_location("Volcano Snail Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Squat Lobster Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Spider Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Coelacanth Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))

    # Oceanic Encyclopedia Entries
    set_rule(multiworld.get_location("Anchovy Encyclopedia Entry", player),
             lambda state: has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Scarlet Prawn Encyclopedia Entry", player),
             lambda state: has_oceanic_net(state, player) or has_crab_pot(state, player))
    set_rule(multiworld.get_location("Blackfin Tuna Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Viperfish Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Moonfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player))
    set_rule(multiworld.get_location("Rattail Encyclopedia Entry", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Ocean Sunfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player))

    # Pursuit Rewards
    set_rule(multiworld.get_location("A Place to Rest: Research Part 1", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("A Place to Rest: Research Part 2", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("A Place to Rest: The Engineer's Companion", player),
             lambda state: has_dredging_equipment(state, player))

    set_rule(multiworld.get_location("Best Before: $150", player),
             lambda state: has_shallow_rod(state, player))

    set_rule(multiworld.get_location("Castaway: Signet Ring", player),
             lambda state: True)

    set_rule(multiworld.get_location("Craven Courier: Getting Over it with Mind and Body", player),
             lambda state: True)  # Requires the Large Package if questsanity

    set_rule(multiworld.get_location("Caught to Order: Basic Crab Pot", player),
             lambda state: (has_coastal_rod(state, player) or has_coastal_net(state, player)) and
                           (has_shallow_rod(state, player) or has_shallow_net(state, player)))
    set_rule(multiworld.get_location("Caught to Order: Research Part 1", player),
             lambda state: (has_coastal_rod(state, player) or has_coastal_net(state, player)) and
                           (has_shallow_rod(state, player) or has_shallow_net(state, player)) and
                           has_crab_pot(state, player))

    set_rule(multiworld.get_location("Figure in Blue: Haggling and Bartering: A Guide", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Figure in Gold: Advanced Fishing", player),
             lambda state: (has_coastal_rod(state, player) or has_coastal_net(state, player)) and
                           has_abyssal_rod(state, player) and has_crab_pot(state, player))
    set_rule(multiworld.get_location("Figure in Purple: Pushing the Limits: Engines", player),
             lambda state: (has_shallow_net(state, player) or has_shallow_net(state, player)) and
                           has_crab_pot(state, player) and has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Figure in Red: Nautical Engineering", player),
             lambda state: (has_oceanic_rod(state, player) or has_oceanic_net(state, player)) and
                           has_volcanic_rod(state, player))

    set_rule(multiworld.get_location("Flames of the Deep: Ghost Rock Slab Research Part", player),
             lambda state: (has_volcanic_rod(state, player) or has_volcanic_net(state, player)) and
                           has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Ghost Rock Slab Refined Metal 1", player),
             lambda state: (has_volcanic_rod(state, player) or has_volcanic_net(state, player)) and
                           has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Ghost Rock Slab Refined Metal 2", player),
             lambda state: (has_volcanic_rod(state, player) or has_volcanic_net(state, player)) and
                           has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Crab Rock Slab Research Part", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Crab Rock Slab Lumber", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Crab Rock Slab TRINKET 1", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Crab Rock Slab TRINKET 2", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Aberration Rock Slab Encrusted Talisman", player),
             lambda state: can_fish(state, player))

    set_rule(multiworld.get_location("Grotesque Fish: Dredging Equipment", player),
             lambda state: can_fish(state, player))  # Requires the handkerchief if questsanity

    set_rule(multiworld.get_location("Lost at Sea: Research Part", player),
             lambda state: has_dredging_equipment(state, player))  # Requires the bronze belt buckle if questsanity

    set_rule(multiworld.get_location("Lost Dog: TRINKET", player),
             lambda state: True)

    set_rule(multiworld.get_location("Package Delivery: Sustainable Fishing", player),
             lambda state: can_fish(state, player))  # Requires the small package if questsanity

    set_rule(multiworld.get_location("Recording Rarities: Oarfish Research Part 1", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Recording Rarities: Oarfish Research Part 2", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Recording Rarities: Gulper Eel Research Part 1", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Recording Rarities: Gulper Eel Research Part 2", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Recording Rarities: Goliath Tigerfish Research Part 1", player),
             lambda state: has_mangrove_rod(state, player))
    set_rule(multiworld.get_location("Recording Rarities: Goliath Tigerfish Research Part 2", player),
             lambda state: has_mangrove_rod(state, player))
    set_rule(multiworld.get_location("Recording Rarities: Coelacanth Research Part 1", player),
             lambda state: has_abyssal_rod(state, player))  # Add event for clearing Hermitage pursuit - can buy explosives
    set_rule(multiworld.get_location("Recording Rarities: Coelacanth Research Part 2", player),
             lambda state: has_abyssal_rod(state, player))

    set_rule(multiworld.get_location("Research Assistant: Sampling Device", player),
             lambda state: (has_shallow_rod(state, player) or has_crab_pot(state, player)) and
                           has_coastal_net(state, player))
    set_rule(multiworld.get_location("Research Assistant: Research Part", player),
             lambda state: (has_shallow_rod(state, player) or has_crab_pot(state, player)) and
                           has_coastal_net(state, player))  # Requires Prototype Parts + Repulsion Machine if questsanity
    set_rule(multiworld.get_location("Research Assistant: A Plan for the Future", player),
             lambda state: (has_shallow_rod(state, player) or has_crab_pot(state, player)) and
                           has_coastal_net(state, player) and has_abyssal_rod(state, player) and
                           has_hadal_rod(state, player))

    set_rule(multiworld.get_location("Stone Tablets: Flame of the Sky", player),
             lambda state: has_dredging_equipment(state, player))  # Requires the fused tablet if questsanity
    set_rule(multiworld.get_location("Stone Tablets: Goblet 1", player),
             lambda state: has_dredging_equipment(state, player))  # Same as above
    set_rule(multiworld.get_location("Stone Tablets: Goblet 2", player),
             lambda state: has_dredging_equipment(state, player))  # Same as above
    set_rule(multiworld.get_location("Stone Tablets: Citrine Ring 1", player),
             lambda state: has_dredging_equipment(state, player))  # Same as above
    set_rule(multiworld.get_location("Stone Tablets: Citrine Ring 2", player),
             lambda state: has_dredging_equipment(state, player))  # Same as above

    set_rule(multiworld.get_location("The Collector: Haste", player),
             lambda state: state.has_group("Relics", player, 1))
    set_rule(multiworld.get_location("The Collector: Manifest", player),
             lambda state: state.has_group("Relics", player, 2))
    set_rule(multiworld.get_location("The Collector: Banish", player),
             lambda state: state.has_group("Relics", player, 3))
    set_rule(multiworld.get_location("The Collector: Atrophy", player),
             lambda state: state.has_group("Relics", player, 4))

    set_rule(multiworld.get_location("The Collector: Ornate Key", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("The Collector: Rusted Music Box", player),
             lambda state: has_dredging_equipment(state, player))  # Add event for clearing Hermitage pursuit

    set_rule(multiworld.get_location("The Collector: Jewel Encrusted Band", player),
             lambda state: (has_shallow_rod(state, player) or has_crab_pot(state, player)) and
                           has_coastal_net(state, player) and has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("The Collector: Shimmering Necklace", player),
             lambda state: (has_coastal_rod(state, player) or has_coastal_net(state, player)) and
                            has_mangrove_rod(state, player) and has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("The Collector: Antique Pocket Watch", player),
             lambda state: (has_volcanic_rod(state, player) or has_volcanic_net(state, player)) and
                           has_abyssal_rod(state, player) and has_crab_pot(state, player))
    """
    set_rule(multiworld.get_location("The Collector: Shimmering Necklace", player),
             lambda state: state.has_all(["Mortar Barrel", "Mortar Frame", "Pungent Bait",
                                          "Fetid Bait", "Reeking Bait"], player) and
                           (has_coastal_rod(state, player) or has_coastal_net(state, player)) and
                           has_mangrove_rod(state, player) and state.has("Chunk of Flesh", player, 3))
    set_rule(multiworld.get_location("The Collector: Antique Pocket Watch", player),
             lambda state: state.has("Fathomless Flame", player, 3))
    """

    set_rule(multiworld.get_location("6th, 7th March 1927 Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("1st June 1927 Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("20th August 1927 Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("21st August 1927 Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("9th September 1927 Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("14th September 1927 Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("??? (Twisted Strand) Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("??? (Devil's Spine) Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("Artifact Manifest Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("Tattered Receipt Message Bottle", player),
             lambda state: True)
    set_rule(multiworld.get_location("Fisherman's Note", player),
             lambda state: True)
    set_rule(multiworld.get_location("Ragged Note", player),
             lambda state: True)

    set_rule(multiworld.get_location("Shipwreck [J8] Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [J8] Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [J8] Item 3", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [J8] Item 4", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [J8] Item 5", player),
             lambda state: True)

    set_rule(multiworld.get_location("Shipwreck [G4] Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [G4] Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [G4] Item 3", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [G4] Item 4", player),
             lambda state: True)

    set_rule(multiworld.get_location("Shipwreck [D3] Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [D3] Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [D3] Item 3", player),
             lambda state: True)

    set_rule(multiworld.get_location("Shipwreck [L10] Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [L10] Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [L10] Item 3", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [L10] Item 4", player),
             lambda state: True)

    set_rule(multiworld.get_location("Shipwreck [M6] Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [M6] Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [M6] Item 3", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [M6] Item 4", player),
             lambda state: True)

    set_rule(multiworld.get_location("Shipwreck [P6] Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [P6] Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Shipwreck [P6] Item 3", player),
             lambda state: True)

    set_rule(multiworld.get_location("Planewreck [E14] Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Planewreck [E14] Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Planewreck [E14] Item 3", player),
             lambda state: True)

    set_rule(multiworld.get_location("Planewreck [D12] Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Planewreck [D12] Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Planewreck [D12] Item 3", player),
             lambda state: True)

    set_rule(multiworld.get_location("Cod Shrine", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Crab Shrine", player),
             lambda state: has_crab_pot(state, player))

    set_rule(multiworld.get_location("Rotten Treasure Chest Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Rotten Treasure Chest Item 2", player),
             lambda state: True)

    set_rule(multiworld.get_location("Floating Treasure Chest Item 1", player),
             lambda state: True)
    set_rule(multiworld.get_location("Floating Treasure Chest Item 2", player),
             lambda state: True)
    set_rule(multiworld.get_location("Floating Treasure Chest Item 3", player),
             lambda state: True)
    set_rule(multiworld.get_location("Floating Treasure Chest Item 4", player),
             lambda state: True)
    set_rule(multiworld.get_location("Floating Treasure Chest Item 5", player),
             lambda state: True)
    set_rule(multiworld.get_location("Floating Treasure Chest Item 6", player),
             lambda state: True)

    # Logic is for non-dredgesanity. Will need to update once dredgesanity is ready
    set_rule(multiworld.get_location("Research Tree: Flexible Fishing Pole", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Heat-Resistant Line", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Anti-Tangle Line", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Versatile Rod", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Hydraulic Rod", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Harvesting Platform", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Bottomless Lines", player),
             lambda state: has_dredging_equipment(state, player) and
                           state.has("Sampling Device", player))
    set_rule(multiworld.get_location("Research Tree: Fathomless Winch", player),
             lambda state: has_dredging_equipment(state, player) and
                           state.has("Sampling Device", player))

    set_rule(multiworld.get_location("Research Tree: Improved Outboard Engine", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Jet Drive Engine", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Refined Outboard Engine", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Twin Prop Engine", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Twin Jet Drive Engine", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Engine Stack", player),
             lambda state: has_dredging_equipment(state, player))

    set_rule(multiworld.get_location("Research Tree: Efficient Crab Pot", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Hardy Crab Pot", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Large Crab Pot", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Complex Crab Pot", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Massive Crab Pot", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Reinforced Crab Pot", player),
             lambda state: has_dredging_equipment(state, player))

    set_rule(multiworld.get_location("Research Tree: Improved Trawl Net", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Silt Filtering Trawl Net", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Large Trawl Net", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Heavy-Duty Trawl Net", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Research Tree: Tempered Mesh Net", player),
             lambda state: has_dredging_equipment(state, player))

    # Since upgrades are gated by hull upgrades (aside from tier 1), all upgrades require
    # enough materials to purchase every upgrade in that tier + however many of each material
    # up until the most recent hull upgrade. Hull upgrades require the cumulative costs of all
    # upgrades, including their own.
    set_rule(multiworld.get_location("Ship Upgrade: Tier 1 +2 Rod Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=6, scrap=4, cloth=3))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 1 +4 Net Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=6, scrap=4, cloth=2))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 1 +2 Engine Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=6, scrap=4, cloth=3))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 1 +1 Light Space", player),
             lambda state: has_enough_materials(state, player, lumber=6, scrap=4, cloth=3))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 2 Hull Upgrade", player),
             lambda state: has_enough_materials(state, player, lumber=10, scrap=6, cloth=6, metal=1))

    set_rule(multiworld.get_location("Ship Upgrade: Tier 2 +3 Rod Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=15, scrap=12, cloth=9, metal=1))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 2 +4 Cargo Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=15, scrap=12, cloth=9, metal=1))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 2 +1 Engine Space", player),
             lambda state: has_enough_materials(state, player, lumber=15, scrap=12, cloth=9, metal=1))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 3 Hull Upgrade", player),
             lambda state: has_enough_materials(state, player, lumber=19, scrap=13, cloth=12, metal=3))

    set_rule(multiworld.get_location("Ship Upgrade: Tier 3 +2 Rod Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=32, scrap=22, cloth=17, metal=3))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 3 +2 Net Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=32, scrap=22, cloth=17, metal=3))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 3 +4 Cargo Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=32, scrap=22, cloth=17, metal=3))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 3 +1 Engine Space", player),
             lambda state: has_enough_materials(state, player, lumber=32, scrap=22, cloth=17, metal=3))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 3 +1 Light Space", player),
             lambda state: has_enough_materials(state, player, lumber=32, scrap=22, cloth=17, metal=3))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 4 Hull Upgrade", player),
             lambda state: has_enough_materials(state, player, lumber=36, scrap=25, cloth=21, metal=6))

    set_rule(multiworld.get_location("Ship Upgrade: Tier 4 +2 Rod Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=49, scrap=37, cloth=26, metal=6))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 4 +4 Cargo Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=49, scrap=37, cloth=26, metal=6))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 4 +2 Engine Spaces", player),
             lambda state: has_enough_materials(state, player, lumber=49, scrap=37, cloth=26, metal=6))
    set_rule(multiworld.get_location("Ship Upgrade: Tier 4 +1 Light Space", player),
             lambda state: has_enough_materials(state, player, lumber=49, scrap=37, cloth=26, metal=6))

    """
    set_rule(multiworld.get_location("", player),
             lambda state:)
    """


def set_aberration_rules(world: "DredgeWorld", multiworld: MultiWorld):
    player = world.player

    # The Marrows Aberration Encyclopedia Entries
    set_rule(multiworld.get_location("Grotesque Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Lumpy Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Many-Eyed Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("All-Seeing Cod Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Fanged Cod Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Three-Headed Cod Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Brood Squid Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Snag Squid Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Barbed Eel Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Host Eel Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Cyclopean Flounder Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Riddled Flounder Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Tusked Grouper Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Voltaic Grouper Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Shard Ray Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Sallow Sailfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Hooked Sailfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Bloodskin Shark Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Cleft-Mouth Shark Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Cerebral Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Malignant Pincer Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))

    # Gale Cliffs Aberration Encyclopedia Entries
    set_rule(multiworld.get_location("Gnashing Perch Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Flayed Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Bearded Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Scouring Bass Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Gelatinous Stonefish Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Enthralled Stonefish Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Decaying Blackmouth Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Sprouting Eel Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Withered Ray Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Translucent Sturgeon Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Shattered Wreckfish Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Bony Wreckfish Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Splintered Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Cortex Decorator Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))

    # Stellar Basin Aberration Encyclopedia Entries
    set_rule(multiworld.get_location("Parhelion Jellyfish Encyclopedia Entry", player),
             lambda state: has_coastal_net(state, player))
    set_rule(multiworld.get_location("Cursed Fangtooth Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Voideye Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Radiant Squid Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Blood Snapper Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Latching Snapper Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Ruptured Vessel Encyclopedia Entry", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Perished Loosejaw Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Calcified Snailfish Encyclopedia Entry", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Seizing Snailfish Encyclopedia Entry", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Consumed Grouper Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Medusa Octopus Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_crab_pot(state, player))
    set_rule(multiworld.get_location("Bursting Anglerfish Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Savage Barracuda Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Concertina Barracuda Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player))
    set_rule(multiworld.get_location("Gazing Shark Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player))
    set_rule(multiworld.get_location("Crown of Nadir Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Entangled Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Imperious Lobster Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))

    # Twisted Strand Aberration Encylopedia Entries
    set_rule(multiworld.get_location("Entwined Mullet Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Gleaming Mullet Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Blistered Tarpon Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Vortex Interloper Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player) or has_mangrove_net(state, player))
    set_rule(multiworld.get_location("Clawfin Gar Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player) or has_mangrove_net(state, player))
    set_rule(multiworld.get_location("Grinning Gar Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player) or has_mangrove_net(state, player))
    set_rule(multiworld.get_location("Twinned Eels Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player))
    set_rule(multiworld.get_location("Nightwing Catfish Encyclopedia Entry", player),
             lambda state: has_mangrove_rod(state, player) or has_mangrove_net(state, player))
    set_rule(multiworld.get_location("Effigy Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Mire Screecher Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))

    # Devil's Spine Aberration Encylopedia Entries
    set_rule(multiworld.get_location("Ossified Searobin Encyclopedia Entry", player),
             lambda state: has_shallow_rod(state, player) or has_shallow_net(state, player))
    set_rule(multiworld.get_location("Infernal Eel Encyclopedia Entry", player),
             lambda state: has_volcanic_rod(state, player) or has_volcanic_net(state, player))
    set_rule(multiworld.get_location("Serpentine Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Tattered Mackerel Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player) or has_coastal_net(state, player))
    set_rule(multiworld.get_location("Defaced Skate Encyclopedia Entry", player),
             lambda state: has_volcanic_rod(state, player) or has_volcanic_net(state, player))
    set_rule(multiworld.get_location("Rapt Shark Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Twisted Shark Encyclopedia Entry", player),
             lambda state: has_volcanic_rod(state, player))
    set_rule(multiworld.get_location("Grasping Snail Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Sable Reacher Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Umbral Puppet Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))

    # Oceanic Aberration Encyclopedia Entries
    set_rule(multiworld.get_location("Anchovy King Encyclopedia Entry", player),
             lambda state: has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Leeching Prawn Encyclopedia Entry", player),
             lambda state: has_oceanic_net(state, player) or has_crab_pot(state, player))
    set_rule(multiworld.get_location("Razormouth Tuna Encyclopedia Entry", player),
             lambda state:has_oceanic_rod(state, player) or has_oceanic_net(state, player))
    set_rule(multiworld.get_location("Decrepit Viperfish Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Collapsed Viperfish Encyclopedia Entry", player),
             lambda state: has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Skeletal Moonfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player))
    set_rule(multiworld.get_location("Beaked Moonfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player))
    set_rule(multiworld.get_location("Congealed Rattail Encyclopedia Entry", player),
             lambda state: has_hadal_rod(state, player))
    set_rule(multiworld.get_location("Charred Sunfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player))
    set_rule(multiworld.get_location("Glaring Sunfish Encyclopedia Entry", player),
             lambda state: has_oceanic_rod(state, player))


def set_blackstone_key_rules(world: "DredgeWorld", multiworld: MultiWorld):
    player = world.player

    set_rule(multiworld.get_location("Blackstone Isle Workshop: Arterial Engine", player),
             lambda state: True)
    set_rule(multiworld.get_location("Blackstone Isle Workshop: Sign of Ruin", player),
             lambda state: True)


def set_pale_reach_common_rules(world: "DredgeWorld", multiworld: MultiWorld):
    player = world.player

    # Pale Reach Encyclopedia Entries
    set_rule(multiworld.get_location("Icefish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player) or has_ice_net(state, player))
    set_rule(multiworld.get_location("Char Encyclopedia Entry", player),
             lambda state: has_coastal_rod(state, player))
    set_rule(multiworld.get_location("Wolffish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player))
    set_rule(multiworld.get_location("Stargazer Encyclopedia Entry", player),
             lambda state: has_ice_net(state, player))
    set_rule(multiworld.get_location("Lizardfish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player) or has_ice_net(state, player))
    set_rule(multiworld.get_location("Toothfish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player))
    set_rule(multiworld.get_location("Goblin Shark Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player))
    set_rule(multiworld.get_location("Colossal Squid Encyclopedia Entry", player),
             lambda state: state.has("Radiant Trawl Net", player))
    set_rule(multiworld.get_location("Sea Stars Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("King Crab Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Sleeper Shark Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player))

    # Pale Reach Pursuit Rewards
    set_rule(multiworld.get_location("Icebreaker: Icebreaker", player),
             lambda state: has_dredging_equipment(state, player) and  # Requires all 3 icebreaker pieces if questsanity
                           can_fish(state, player))

    set_rule(multiworld.get_location("Ice Shaper: Ice Block 1", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player) and
                           state.has("Icebreaker", player))  # Requires ice shaper if questsanity
    set_rule(multiworld.get_location("Ice Shaper: Ice Block 2", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player) and
                           state.has("Icebreaker", player))  # Requires ice shaper if questsanity

    set_rule(multiworld.get_location("Under the Ice: Radiant Trawl Net", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player) and
                           state.has("Icebreaker", player))  # Requires 4x Frozen Hearts if questsanity
    set_rule(multiworld.get_location("Under the Ice: Aurous Anchor", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player) and
                           state.has("Icebreaker", player))  # Requires 4x Ice Axes if questsanity

    # Pale Reach Quest Items
    set_rule(multiworld.get_location("Figure in White: Book of Astral Symbols", player),
             lambda state: has_ice_net(state, player) and has_crab_pot(state, player))

    set_rule(multiworld.get_location("Captain's Log - 30th May, 1847", player),
             lambda state: can_fish(state, player))
    set_rule(multiworld.get_location("Captain's Log - 1st June, 1847", player),
             lambda state: can_fish(state, player))
    set_rule(multiworld.get_location("Captain's Log - 5th June, 1847", player),
             lambda state: can_fish(state, player))
    set_rule(multiworld.get_location("Leather Journal - 4th June, 1847", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Leather Journal - 7th June, 1847", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Leather Journal - 8th June, 1847", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Tattered Diary - 2nd June, 1847", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Tattered Diary - 4th June, 1847", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Tattered Diary - 5th June, 1847", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player))


def set_pale_reach_aberration_rules(world: "DredgeWorld", multiworld: MultiWorld):
    player = world.player

    # Pale Reach Aberration Encyclopedia Entries
    set_rule(multiworld.get_location("Fractalline Icefish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player) or has_ice_net(state, player))
    set_rule(multiworld.get_location("Thawed Icefish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player) or has_ice_net(state, player))
    set_rule(multiworld.get_location("Astral Icefish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player) or has_ice_net(state, player))
    set_rule(multiworld.get_location("Bubbling Char Encyclopedia Entry", player),
             lambda state:has_coastal_rod(state, player))
    set_rule(multiworld.get_location("Hinged Wolffish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player))
    set_rule(multiworld.get_location("Craterous Seer Encyclopedia Entry", player),
             lambda state: has_ice_net(state, player))
    set_rule(multiworld.get_location("Feral Lizardfish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player) or has_ice_net(state, player))
    set_rule(multiworld.get_location("Bulbous Toothfish Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player))
    set_rule(multiworld.get_location("Grisly Shark Encyclopedia Entry", player),
             lambda state: has_ice_rod(state, player))
    set_rule(multiworld.get_location("Pale Grasper Encyclopedia Entry", player),
             lambda state: state.has("Radiant Trawl Net", player))
    set_rule(multiworld.get_location("Fallen Stars Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("King's Wreath Encyclopedia Entry", player),
             lambda state: has_crab_pot(state, player))


def set_quest_item_rules(world: "DredgeWorld", multiworld: MultiWorld):
    player = world.player

    set_rule(multiworld.get_location("Craven Courier: Large Package", player),
             lambda state: True)

    set_rule(multiworld.get_location("Flames of the Deep: Ghost Rock Slab Fathomless Flame", player),
             lambda state: (has_volcanic_rod(state, player) or has_volcanic_net(state, player)) and
                           has_abyssal_rod(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Crab Rock Slab Fathomless Flame", player),
             lambda state: has_crab_pot(state, player))
    set_rule(multiworld.get_location("Flames of the Deep: Aberration Rock Slab Fathomless Flame", player),
             lambda state: can_fish(state, player))

    set_rule(multiworld.get_location("Grotesque Fish: Handkerchief", player),
             lambda state: can_fish(state, player))

    set_rule(multiworld.get_location("Hermitage: Family Crest", player),
             lambda state: has_dredging_equipment(state, player))

    set_rule(multiworld.get_location("Lost at Sea: Bronze Belt Buckle", player),
             lambda state: has_dredging_equipment(state, player))

    set_rule(multiworld.get_location("Package Delivery: Small Package", player),
             lambda state: can_fish(state, player))

    set_rule(multiworld.get_location("Research Assistant: Prototype Parts", player),
             lambda state: (has_shallow_rod(state, player) or has_crab_pot(state, player)) and
                           has_coastal_net(state, player))
    set_rule(multiworld.get_location("Research Assistant: Repulsion Machine", player),
             lambda state: (has_shallow_rod(state, player) or has_crab_pot(state, player)) and
                           has_coastal_net(state, player) and state.has("Prototype Parts", player))

    set_rule(multiworld.get_location("Stone Tablets: Stone Tablet 1", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Stone Tablets: Stone Tablet 2", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Stone Tablets: Stone Tablet 3", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("Stone Tablets: Fused Tablet", player),
             lambda state: state.has("Stone Tablet", player, 3))

    set_rule(multiworld.get_location("The Bitter End: Mortar Barrel", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("The Bitter End: Mortar Frame", player),
             lambda state: has_dredging_equipment(state, player))
    set_rule(multiworld.get_location("The Bitter End: Pungent Bait", player),
             lambda state: state.has_all(["Mortar Barrel", "Mortar Frame"], player) and
                           (has_coastal_rod(state, player) or has_coastal_net(state, player)) and
                           (has_mangrove_rod(state, player) or has_mangrove_net(state, player)))
    set_rule(multiworld.get_location("The Bitter End: Fetid Bait", player),
             lambda state: state.has_all(["Mortar Barrel", "Mortar Frame"], player) and
                           (has_coastal_rod(state, player) or has_coastal_net(state, player)) and
                           (has_mangrove_rod(state, player) or has_mangrove_net(state, player)))
    set_rule(multiworld.get_location("The Bitter End: Reeking Bait", player),
             lambda state: state.has_all(["Mortar Barrel", "Mortar Frame"], player) and
                           has_mangrove_rod(state, player))
    set_rule(multiworld.get_location("The Bitter End: Chunk of Flesh 1", player),
             lambda state: state.has("Pungent Bait", player) and has_mangrove_rod(state, player) and
                           (has_coastal_rod(state, player) or has_coastal_net(state, player)))
    set_rule(multiworld.get_location("The Bitter End: Chunk of Flesh 2", player),
             lambda state: state.has("Fetid Bait", player) and has_mangrove_rod(state, player) and
                           (has_coastal_rod(state, player) or has_coastal_net(state, player)))
    set_rule(multiworld.get_location("The Bitter End: Chunk of Flesh 3", player),
             lambda state: state.has("Reeking Bait", player) and has_mangrove_rod(state, player) and
                           (has_coastal_rod(state, player) or has_coastal_net(state, player)))


def set_pale_reach_quest_item_rules(world: "DredgeWorld", multiworld: MultiWorld):
    player = world.player

    set_rule(multiworld.get_location("Under the Ice: Ice Pick (Central Camp)", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Under the Ice: Ice Pick (Eastern Terminus)", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Under the Ice: Ice Pick (Western Bearing)", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Under the Ice: Ice Pick (Southern Locus)", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player) and
                           state.has("Icebreaker", player))
    set_rule(multiworld.get_location("Under the Ice: Frozen Heart (Central Camp)", player),
             lambda state: can_fish(state, player) and
                           state.has("Ice Pick", player, 4))
    set_rule(multiworld.get_location("Under the Ice: Frozen Heart (Eastern Terminus)", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player) and
                           state.has("Ice Pick", player, 4))
    set_rule(multiworld.get_location("Under the Ice: Frozen Heart (Western Bearing)", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player) and
                           state.has("Ice Pick", player, 4))
    set_rule(multiworld.get_location("Under the Ice: Frozen Heart (Southern Locus)", player),
             lambda state: can_fish(state, player) and
                           state.has("Icebreaker", player) and
                           state.has("Ice Pick", player, 4))

    set_rule(multiworld.get_location("Icebreaker: Left Icebreaker Plow Half", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player))
    set_rule(multiworld.get_location("Icebreaker: Right Icebreaker Plow Half", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player))
    set_rule(multiworld.get_location("Icebreaker: Icebreaker Bracing", player),
             lambda state: has_dredging_equipment(state, player) and
                           can_fish(state, player))
