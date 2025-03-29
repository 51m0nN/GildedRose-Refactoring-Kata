from ..stock import Item


def _decrease_item_quality(item: Item, amount: int = 1, min_quality=0) -> None:
    """Item quality is reduced by amount, but can never drop below 0"""
    item.quality = max(min_quality, item.quality - amount)


def _increase_item_quality(item: Item, amount: int = 1, max_quality: int = 50) -> None:
    """Item quality is increased by amount, but can never be greater than max_amount"""
    item.quality = min(max_quality, item.quality + amount)


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
    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        _increase_item_quality(item, amount=2)
    else:
        _increase_item_quality(item, amount=1)


def update_backstage_pass_item(item: Item) -> None:
    """Quality cannot exceed 50
    Quality goes up by 1
    Quality goes up by 2 if there are 10 or fewer days to the gig
    Quality goes up by 3 if there are 5 or fewer days to the gig
    Quality goes to 0 after the gig
    """
    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        item.quality = 0
    elif item.sell_in < 5:
        _increase_item_quality(item, amount=3)
    elif item.sell_in < 10:
        _increase_item_quality(item, amount=2)
    elif item.sell_in >= 10:
        _increase_item_quality(item, amount=1)


def update_standard_item(item: Item) -> None:
    """An item's quality goes down by one
    Once its past its sell by date it quality goes down by 2 each time
    """
    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        _decrease_item_quality(item, amount=2)
    else:
        _decrease_item_quality(item, amount=1)


def update_conjured_item(item: Item) -> None:
    """Quality declines at twice the rate of a normal item"""
    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        _decrease_item_quality(item, amount=4)
    else:
        _decrease_item_quality(item, amount=2)
