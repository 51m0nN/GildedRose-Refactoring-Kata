from ..stock import Item


def update_sulfuras_item(item: Item) -> None:
    """Don't do anything to the item
    It is 'special'
    """
    pass


def update_brie_item(item: Item) -> None:
    """Brie's quality goes up by 1
    If Brie is past its sell by date, it goes up 2
    Brie can never have better than 50 quality
    """
    if item.quality < 50:
        item.quality = item.quality + 1
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality < 50:
        item.quality = item.quality + 1
