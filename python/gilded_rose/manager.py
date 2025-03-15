from .stock import Item
from .strategies.selector import StrategySelector


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items
        self.strategy_selector = StrategySelector()

    def update_quality(self):
        for item in self.items:
            update = self.strategy_selector.select(item)

            if update:
                update(item)
            else:
                self.update_item_legacy(item)

    @staticmethod
    def update_item_legacy(item: Item) -> None:
        """***DEPRECATED***

        Add update item functionality via strategies.updaters and strategies.selector

        I would add @deprecated to this function a\t this point if I was running in 3.13.2

        Separate the legacy code path into its own function

        Here be dragons!
        :param item:
        """
        print("***DEPRECATED***")

        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
