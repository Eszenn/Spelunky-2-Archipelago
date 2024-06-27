from typing import Dict, List, NamedTuple, Callable
from BaseClasses import CollectionState


class DredgeRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, DredgeRegionData] = {
    "Menu": DredgeRegionData(["The Marrows"]),
    "The Marrows": DredgeRegionData(["Open Ocean"]),
    "Gale Cliffs": DredgeRegionData(["Open Ocean"]),
    "Stellar Basin": DredgeRegionData(["Open Ocean"]),
    "Twisted Strand": DredgeRegionData(["Open Ocean"]),
    "Devil's Spine": DredgeRegionData(["Open Ocean"]),
    "Pale Reach": DredgeRegionData(["Open Ocean"]),
    "Open Ocean": DredgeRegionData(["The Marrows", "Gale Cliffs", "Stellar Basin",
                                    "Twisted Strand", "Devil's Spine", "Pale Reach"])
}
