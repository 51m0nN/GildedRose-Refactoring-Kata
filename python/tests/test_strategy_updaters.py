from ..gilded_rose.stock import Item
from ..gilded_rose.strategies.updaters import update_sulfuras_item, update_brie_item


def test_sulfuras_updater_strategy():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80)
    update_sulfuras_item(item)
    assert item.sell_in == 2  # Never needs to be sold, and never changes
    assert item.quality == 80  # Quality CAN exceed 50 if it's initialised at over 50


def test_brie_updater_strategy():
    item = Item(name="Aged Brie", sell_in=2, quality=45)
    assert item.sell_in == 2
    assert item.quality == 45

    update_brie_item(item)
    assert item.sell_in == 1
    assert item.quality == 46  # Quality of Brie goes up

    update_brie_item(item)
    assert item.sell_in == 0
    assert item.quality == 47  # Quality of Brie goes up

    update_brie_item(item)
    assert item.sell_in == -1
    assert item.quality == 49  # Quality of Brie goes up twice as fast after the sell by date!

    update_brie_item(item)
    assert item.sell_in == -2
    assert item.quality == 50  # Quality can't exceed 50
