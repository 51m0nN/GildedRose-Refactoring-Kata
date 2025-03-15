from typing import Callable, Optional

from ..stock import Item


class StrategySelector:
    __slots__: ()
    __special_strategies = {}

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
            return None
