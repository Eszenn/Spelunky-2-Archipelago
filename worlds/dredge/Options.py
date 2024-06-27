from Options import Toggle, Range, Choice, OptionSet, PerGameCommonOptions
from dataclasses import dataclass


class EnabledDLC(OptionSet):
    """
    Which DLC content should be included. Valid options are:
    Blackstone Key,
    Pale Reach,
    Iron Rig
    """
    display_name = "Enabled DLC"
    default = {}
    valid_keys = ["Blackstone Key", "Pale Reach", "Iron Rig"]
    valid_keys_casefold = True


class IncludeAberrations(Toggle):
    """Whether to include aberration encyclopedia entries."""
    display_name = "Include Aberrations"


class Goal(Choice):
    """
    Relic Hunt: Requires collecting a specified amount of relics.
    Fish 'em All: Requires collecting a specified percentage of fish.
    """
    option_relic_hunt = 0
    option_fish_em_all = 1
    default = 0


class RelicShuffle(Toggle):
    """Whether relics should be shuffled into the item pool."""
    display_name = "Relic Shuffle"


class NumberOfRelics(Range):
    """How many Relics are required to finish the game. Ignored if goal is not Relic Hunt"""
    display_name = "Number of Relics"
    range_start = 1
    range_end = 5
    default = 5


class PercentageOfFish(Range):
    """What percentage of fish are required to finish the game. Ignored if goal is not Fish 'em All"""
    range_start = 20
    range_end = 100
    default = 80


class QuestSanity(Toggle):
    """Whether quest items should be included in the item pool."""
    display_name = "Quest Item Shuffle"


class DredgeSanity(Toggle):
    """Whether dredge spots should be added to locations"""
    display_name = "Include Dredge Spots"


class EnableTraps(Toggle):
    """Whether traps should be added to the item pool"""
    display_name = "Enable Traps"


class TrapPercentage(Range):
    """What percentage of filler items should be replaced by traps"""
    range_start = 5
    range_end = 30
    default = 20

# Add a trap weights class(es)


@dataclass
class DredgeOptions(PerGameCommonOptions):
    enabled_dlc: EnabledDLC
    include_aberrations: IncludeAberrations
    goal: Goal
    relic_shuffle: RelicShuffle
    number_of_relics: NumberOfRelics
    percent_of_fish: PercentageOfFish
    quest_sanity: QuestSanity
    # dredge_sanity: DredgeSanity // not implemented yet
    # traps_enabled: EnableTraps // not implemented yet
    # trap_percentage: TrapPercentage // not implemented yet
