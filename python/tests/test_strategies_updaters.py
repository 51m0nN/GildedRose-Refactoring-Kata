from ..gilded_rose.stock import Item
from ..gilded_rose.strategies.updaters import (
    update_backstage_pass_item,
    update_brie_item,
    update_sulfuras_item,
    update_standard_item,
    update_conjured_item,
)


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


def test_sulfuras_updater_strategy():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80)
    update_sulfuras_item(item)
    assert item.sell_in == 2  # Never needs to be sold, and never changes
    assert item.quality == 80  # Quality CAN exceed 50 if it's initialised at over 50


def test_test_backstage_pass_updater_strategy():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20)

    update_backstage_pass_item(item)
    assert item.sell_in == 10
    assert item.quality == 21  # The sell_in was 11 when the function was called - hence this dropped by 1

    update_backstage_pass_item(item)
    assert item.sell_in == 9
    assert item.quality == 23  # Increases by 2

    update_backstage_pass_item(item)
    update_backstage_pass_item(item)
    update_backstage_pass_item(item)
    update_backstage_pass_item(item)
    assert item.sell_in == 5
    assert item.quality == 31

    update_backstage_pass_item(item)
    assert item.sell_in == 4
    assert item.quality == 34  # Increases by 3 when sell_in less than 5

    update_backstage_pass_item(item)
    update_backstage_pass_item(item)
    update_backstage_pass_item(item)
    update_backstage_pass_item(item)
    assert item.sell_in == 0
    assert item.quality == 46

    update_backstage_pass_item(item)
    assert item.sell_in == -1
    assert item.quality == 0  # quality is 0 after the gig

    update_backstage_pass_item(item)
    assert item.sell_in == -2
    assert item.quality == 0  # quality is 0 after the gig


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
