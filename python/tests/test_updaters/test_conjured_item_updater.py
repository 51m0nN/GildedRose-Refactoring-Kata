from python.gilded_rose.stock import Item
from python.gilded_rose.strategies.updaters import update_conjured_item


def test_conjured_updater_strategy():
    item = Item(name="Conjured Mana Cake", sell_in=2, quality=4)
    assert item.sell_in == 2
    assert item.quality == 4

    update_conjured_item(item)
    assert item.sell_in == 1
    assert item.quality == 2

    update_conjured_item(item)
    assert item.sell_in == 0
    assert item.quality == 0

    update_conjured_item(item)
    assert item.sell_in == -1
    assert item.quality == 0  # Note the reduction in quality by 2

    update_conjured_item(item)
    assert item.sell_in == -2
    assert item.quality == 0  # Note the quality stays at 0
