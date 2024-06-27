from typing import List, Mapping, Any, Dict

from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial, ItemClassification, Region
from .Regions import region_data_table
from .Options import DredgeOptions
from .Items import \
    equipment_items, abilities, ship_upgrades, relics, upgrade_materials, \
    quest_items, filler_items, createable_filler_items,  blackstone_key_items, \
    pale_reach_items, pale_reach_quest_items, pale_reach_filler_items, \
    item_data_table, item_categories, item_name_to_id, DredgeItem
from .Locations import \
    fish_entries, aberration_entries, pursuit_rewards, pursuit_quest_items, \
    relic_shuffle_locations, messages, shipwrecks, shrines, chests, \
    research_tree, dry_dock, blackstone_key_locations, \
    pale_reach_fish_entries, pale_reach_aberration_entries, \
    pale_reach_pursuit_rewards, pale_reach_quest_items, pale_reach_messages, \
    location_data_table, location_name_to_id, DredgeLocation
from .Rules import \
    set_common_rules, set_aberration_rules, set_blackstone_key_rules, \
    set_pale_reach_common_rules, set_pale_reach_aberration_rules, \
    set_quest_item_rules, set_pale_reach_quest_item_rules


class DredgeWebWorld(WebWorld):
    theme = "ocean"

    setup_en = Tutorial(
        tutorial_name="Setup Guide",
        description="A guide to setting up DREDGE",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["Eszenn"]
    )
    tutorials = [setup_en]
    # TBD: options_presets = DredgeOptionPresets


class DredgeWorld(World):
    """DREDGE is a Lovecraftian horror fishing game developed by Black Salt Games. As Greater Marrows' newest fisherman,
    you will explore a vast archipelago to catch a wide variety of fish (and other ...creatures), complete quests for a
    number of NPCs, and dredge up secrets from the past."""

    game = "DREDGE"
    web = DredgeWebWorld()
    options = DredgeOptions
    options_dataclass = DredgeOptions
    base_id = 379366373343000
    filler_count = 0

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def generate_early(self) -> None:
        pass

    def create_regions(self) -> None:

        # Creating regions
        for region_name, region_data in region_data_table.items():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Adding connections
        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)

            for connection in region_data.connecting_regions:
                connection_region = self.multiworld.get_region(connection, self.player)
                region.connect(connection_region)

        # Adding locations based on options
        location_names: List[str] = (list(fish_entries.keys()) +
                                     list(relic_shuffle_locations.keys()) +
                                     list(pursuit_rewards.keys()) +
                                     list(messages.keys()) +
                                     list(shipwrecks.keys()) +
                                     list(shrines.keys()) +
                                     list(chests.keys()) +
                                     list(research_tree.keys()) +
                                     list(dry_dock.keys()))

        if "Blackstone Key" in self.options.enabled_dlc:
            location_names.extend(list(blackstone_key_locations.keys()))

        if "Pale Reach" in self.options.enabled_dlc:
            location_names.extend(list(pale_reach_fish_entries.keys()) +
                                  list(pale_reach_pursuit_rewards.keys()) +
                                  list(pale_reach_messages.keys()))

            if self.options.include_aberrations:
                location_names.extend(list(pale_reach_aberration_entries.keys()))

            if self.options.quest_sanity:
                location_names.extend(list(pale_reach_quest_items.keys()))

        if self.options.include_aberrations:
            location_names.extend(list(aberration_entries.keys()))

        if self.options.quest_sanity:
            location_names.extend(list(pursuit_quest_items.keys()))

        # Adding locations to regions
        for region_name in region_data_table.keys():
            region = self.multiworld.get_region(region_name, self.player)

            locations_in_region = [location_name for location_name in location_names if location_data_table[location_name].region == region_name]

            locations_to_add = {}

            for location_name in locations_in_region:
                locations_to_add[location_name] = location_name_to_id[location_name]

            region.add_locations(locations_to_add)

        victory_region = self.multiworld.get_region("Open Ocean", self.player)
        victory_location = DredgeLocation(self.player, "Victory", None, victory_region)
        victory_location.access_rule = lambda state: state.has_group("Relics", self.player, self.options.number_of_relics)
        victory_location.place_locked_item(DredgeItem("Victory", ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        victory_region.locations.append(victory_location)

    def create_item(self, name: str) -> DredgeItem:
        classification = item_data_table[name].classification
        return DredgeItem(name, classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        item_names: List[str] = (list(equipment_items.keys()) +
                                 list(abilities.keys()) +
                                 list(ship_upgrades.keys()) +
                                 list(filler_items.keys()))
        dredge_item_pool: List[DredgeItem] = []

        if "Blackstone Key" in self.options.enabled_dlc:
            for item_name in blackstone_key_items.keys():
                item_names.append(str(item_name))

        if "Pale Reach" in self.options.enabled_dlc:
            item_names.extend(list(pale_reach_items.keys()) +
                              list(pale_reach_filler_items.keys()))

            if self.options.quest_sanity:
                item_names.extend(list(pale_reach_quest_items.keys()))

        if self.options.quest_sanity:
            item_names.extend(list(quest_items.keys()))

        if self.options.relic_shuffle:
            item_names.extend(list(relics.keys()))
        else:
            relic_names = list(relics.keys())
            for location_name in relic_shuffle_locations.keys():
                location = self.multiworld.get_location(location_name, self.player)
                location.place_locked_item(self.create_item(relic_names[0]))
                relic_names.pop(0)

        for name in item_names:
            data = item_data_table[name]
            for i in range(data.amount):
                item = self.create_item(name)
                dredge_item_pool.append(item)

        """
        for i in range(self.filler_count):
            dredge_item_pool.append(self.create_filler())
        """

        self.multiworld.itempool += dredge_item_pool

    def create_filler(self) -> DredgeItem:
        filler_names: List[str] = list(createable_filler_items.keys())
        return self.create_item(filler_names[self.random.randint(0, 2)])

    def set_rules(self) -> None:
        set_common_rules(self, self.multiworld)

        if self.options.include_aberrations:
            set_aberration_rules(self, self.multiworld)

        if self.options.quest_sanity:
            set_quest_item_rules(self, self.multiworld)

        if "Blackstone Key" in self.options.enabled_dlc:
            set_blackstone_key_rules(self, self.multiworld)

        if "Pale Reach" in self.options.enabled_dlc:
            set_pale_reach_common_rules(self, self.multiworld)

            if self.options.include_aberrations:
                set_pale_reach_aberration_rules(self, self.multiworld)

            if self.options.quest_sanity:
                set_pale_reach_quest_item_rules(self, self.multiworld)

    def fill_slot_data(self) -> Mapping[str, Any]:
        pass

    item_name_groups = item_categories
