from typing import Callable

from ..stock import Item
from .updaters import (
    update_backstage_pass_item,
    update_brie_item,
    update_sulfuras_item,
    update_standard_item,
    update_conjured_item,
)


class StrategySelector:
    __slots__: ()
    __special_strategies = {
        "Aged Brie": update_brie_item,
        "Sulfuras, Hand of Ragnaros": update_sulfuras_item,
        "Backstage passes to a TAFKAL80ETC concert": update_backstage_pass_item,
        "Conjured Mana Cake": update_conjured_item,
    }

    @staticmethod
    def select(item: Item) -> Callable:
        """returns the appropriate update strategy for the Item"""
        try:
            return StrategySelector.__special_strategies[item.name]
        except KeyError:
            return update_standard_item
