from python.gilded_rose.stock import Item
from python.gilded_rose.strategies.updaters import update_sulfuras_item


def test_sulfuras_updater_strategy():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80)
    update_sulfuras_item(item)
    assert item.sell_in == 2  # Never needs to be sold, and never changes
    assert item.quality == 80  # Quality CAN exceed 50 if it's initialised at over 50
