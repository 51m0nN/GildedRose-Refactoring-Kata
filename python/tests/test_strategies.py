from ..gilded_rose.stock import Item
from ..gilded_rose.update_strategies import (
    SupportsUpdatingItemsStrategy,
    StandardUpdaterStrategy,
    BrieUpdaterStrategy,
    SulfurasUpdaterStrategy,
    BackstagePassUpdaterStrategy,
)


def test_item_updater_strategy():
    updater = StandardUpdaterStrategy()
    isinstance(updater, SupportsUpdatingItemsStrategy)
    item = Item(name="+5 Dexterity Vest", sell_in=2, quality=4)
    assert item.sell_in == 2
    assert item.quality == 4

    updater.update_item(item)
    assert item.sell_in == 1
    assert item.quality == 3

    updater.update_item(item)
    assert item.sell_in == 0
    assert item.quality == 2

    updater.update_item(item)
    assert item.sell_in == -1
    assert item.quality == 0  # Note the reduction in quality by 2

    updater.update_item(item)
    assert item.sell_in == -2
    assert item.quality == 0  # Note the quality stays at 0


def test_brie_updater_strategy():
    updater = BrieUpdaterStrategy()
    isinstance(updater, SupportsUpdatingItemsStrategy)
    item = Item(name="Aged Brie", sell_in=2, quality=45)
    assert item.sell_in == 2
    assert item.quality == 45

    updater.update_item(item)
    assert item.sell_in == 1
    assert item.quality == 46  # Quality of Brie goes up

    updater.update_item(item)
    assert item.sell_in == 0
    assert item.quality == 47  # Quality of Brie goes up

    updater.update_item(item)
    assert item.sell_in == -1
    assert item.quality == 49  # Quality of Brie goes up twice as fast after the sell by date!

    updater.update_item(item)
    assert item.sell_in == -2
    assert item.quality == 50  # Quality can't exceed 50


def test_sulfuras_updater_strategy():
    updater = SulfurasUpdaterStrategy()
    isinstance(updater, SupportsUpdatingItemsStrategy)
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80)
    updater.update_item(item)
    assert item.sell_in == 2  # Never needs to be sold, and never changes
    assert item.quality == 80  # Quality CAN exceed 50 if it's initialised at over 50


def test_test_backstage_pass_updater_strategy():
    updater = BackstagePassUpdaterStrategy()
    isinstance(updater, SupportsUpdatingItemsStrategy)
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20)

    updater.update_item(item)
    assert item.sell_in == 10
    assert item.quality == 21  # The sell_in was 11 when the function was called - hence this dropped by 1

    updater.update_item(item)
    assert item.sell_in == 9
    assert item.quality == 23  # Increases by 2

    updater.update_item(item)
    updater.update_item(item)
    updater.update_item(item)
    updater.update_item(item)
    assert item.sell_in == 5
    assert item.quality == 31

    updater.update_item(item)
    assert item.sell_in == 4
    assert item.quality == 34  # Increases by 3 when sell_in less than 5

    updater.update_item(item)
    updater.update_item(item)
    updater.update_item(item)
    updater.update_item(item)
    assert item.sell_in == 0
    assert item.quality == 46

    updater.update_item(item)
    assert item.sell_in == -1
    assert item.quality == 0  # quality is 0 after the gig

    updater.update_item(item)
    assert item.sell_in == -2
    assert item.quality == 0  # quality is 0 after the gig
