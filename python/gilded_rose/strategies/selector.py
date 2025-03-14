from ..stock import Item
from .updaters import (
    SupportsUpdatingItemsStrategy,
    StandardUpdaterStrategy,
    BrieUpdaterStrategy,
    SulfurasUpdaterStrategy,
    BackstagePassUpdaterStrategy,
    ConjuredUpdaterStrategy,
)


class StrategySelector:
    _special_strategies = {
        "Aged Brie": BrieUpdaterStrategy,
        "Sulfuras, Hand of Ragnaros": SulfurasUpdaterStrategy,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdaterStrategy,
        "Conjured Mana Cake": ConjuredUpdaterStrategy,
    }

    @staticmethod
    def select(item: Item) -> SupportsUpdatingItemsStrategy:
        """returns the appropriate update strategy for the Item"""
        try:
            return StrategySelector._special_strategies[item.name]()
        except KeyError:
            return StandardUpdaterStrategy()
