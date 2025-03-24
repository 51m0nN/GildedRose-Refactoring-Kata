from python.gilded_rose.stock import Item
from python.gilded_rose.strategies.updaters import update_standard_item


def test_item_updater_strategy():
    item = Item(name="+5 Dexterity Vest", sell_in=2, quality=4)
    assert item.sell_in == 2
    assert item.quality == 4

    update_standard_item(item)
    assert item.sell_in == 1
    assert item.quality == 3

    update_standard_item(item)
    assert item.sell_in == 0
    assert item.quality == 2

    update_standard_item(item)
    assert item.sell_in == -1
    assert item.quality == 0  # Note the reduction in quality by 2

    update_standard_item(item)
    assert item.sell_in == -2
    assert item.quality == 0  # Note the quality stays at 0
