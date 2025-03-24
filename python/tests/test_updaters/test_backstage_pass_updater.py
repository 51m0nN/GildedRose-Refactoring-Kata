from python.gilded_rose.stock import Item
from python.gilded_rose.strategies.updaters import update_backstage_pass_item


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
