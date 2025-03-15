from typing import Callable, Optional

from ..stock import Item
from .updaters import (
    update_sulfuras_item,
    update_brie_item,
    update_backstage_pass_item,
    update_standard_item,
    update_conjured_item,
)


class StrategySelector:
    __slots__: ()
    __special_strategies = {
        "Sulfuras, Hand of Ragnaros": update_sulfuras_item,
        "Aged Brie": update_brie_item,
        "Backstage passes to a TAFKAL80ETC concert": update_backstage_pass_item,
        "Conjured Mana Cake": update_conjured_item,
    }

    @staticmethod
    def select(item: Item) -> Optional[Callable]:
        """Will return the appropriate update strategy for the Item

        Currently, no update strategies exist

        Update strategies will begin with edge cases and move to generalisations last
        """
        """"""
        try:
            return StrategySelector.__special_strategies[item.name]
        except KeyError:
            return update_standard_item
