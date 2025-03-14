from .stock import Item
from .strategies.selector import StrategySelector


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items
        self.strategy_selector = StrategySelector()

    def update_quality(self):
        for item in self.items:
            update = self.strategy_selector.select(item)
            update(item)
