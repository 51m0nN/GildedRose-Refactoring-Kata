from typing import Protocol, runtime_checkable
from ..stock import Item


@runtime_checkable
class SupportsUpdatingItemsStrategy(Protocol):
    """This protocol defines the interface required by an update strategy class"""

    def update_item(self, item: Item) -> None: ...


class StandardUpdaterStrategy:
    @staticmethod
    def update_item(item: Item) -> None:
        """An item's quality goes down by one
        Once its past its sell by date it quality goes down by 2 each time
        """
        item.sell_in = item.sell_in - 1
        if item.quality > 0:
            item.quality = item.quality - 1
        if item.sell_in < 0 < item.quality:
            item.quality = item.quality - 1


class BrieUpdaterStrategy:
    @staticmethod
    def update_item(item: Item) -> None:
        """Brie's quality goes up by 1
        If Brie is past its sell by date, it goes up 2
        Brie can never have better than 50 quality
        """
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality = item.quality + 1


class SulfurasUpdaterStrategy:
    @staticmethod
    def update_item(item: Item) -> None:
        """Don't do anything to the item
        It is 'special'
        """
        pass


class BackstagePassUpdaterStrategy:
    @staticmethod
    def update_item(item: Item) -> None:
        """Quality cannot exceed 50
        Quality goes up by 1
        Quality goes up by 2 if there are 10 or fewer days to the gig
        Quality goes up by 3 if there are 5 or fewer days to the gig
        Quality goes to 0 after the gig
        """
        item.sell_in = item.sell_in - 1

        if item.quality < 50:
            item.quality = item.quality + 1

            if item.sell_in < 10 and item.quality < 50:
                item.quality = item.quality + 1

            if item.sell_in < 5 and item.quality < 50:
                item.quality = item.quality + 1

        if item.sell_in < 0:
            item.quality = 0
