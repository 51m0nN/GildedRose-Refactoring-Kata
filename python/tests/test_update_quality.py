from ..gilded_rose.stock import Item
from ..gilded_rose.manager import GildedRose


def setup_gilded_rose(item: Item) -> (GildedRose, Item):
    gilded_rose = GildedRose([item])
    item = gilded_rose.items[0]
    return gilded_rose, item


def test_foo():
    gilded_rose, item = setup_gilded_rose(Item("foo", 0, 100))
    gilded_rose.update_quality()
    assert "foo" == item.name
    assert item.sell_in == -1
    assert (
        98 == item.quality
    )  # Quality CAN be over 50 if it's initialised at over 50, this is an undocumented behaviour


def run_for_standard_item(name: str):
    """Any non-special item should behave in this way..."""
    gilded_rose, item = setup_gilded_rose(Item(name=name, sell_in=2, quality=4))
    assert item.sell_in == 2
    assert item.quality == 4

    gilded_rose.update_quality()
    assert item.sell_in == 1
    assert item.quality == 3

    gilded_rose.update_quality()
    assert item.sell_in == 0
    assert item.quality == 2

    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0  # Note the reduction in quality by 2

    gilded_rose.update_quality()
    assert item.sell_in == -2
    assert item.quality == 0  # Note the quality stays at 0


def test_vest_item():
    """Once the sell by date has passed, Quality degrades twice as fast
    The Quality of an item is never negative
    """
    run_for_standard_item(name="+5 Dexterity Vest")


def test_brie():
    """ "Aged Brie" actually increases in Quality the older it gets"""
    gilded_rose, item = setup_gilded_rose(Item(name="Aged Brie", sell_in=2, quality=45))
    assert item.sell_in == 2
    assert item.quality == 45

    gilded_rose.update_quality()
    assert item.sell_in == 1
    assert item.quality == 46  # Quality of Brie goes up

    gilded_rose.update_quality()
    assert item.sell_in == 0
    assert item.quality == 47  # Quality of Brie goes up

    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 49  # Quality of Brie goes up twice as fast after the sell by date!

    gilded_rose.update_quality()
    assert item.sell_in == -2
    assert item.quality == 50  # Quality can't exceed 50


def test_elixir():
    run_for_standard_item(name="Elixir of the Mongoose")


def test_sulfuras():
    gilded_rose, item = setup_gilded_rose(Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80))
    gilded_rose.update_quality()
    assert item.sell_in == 2  # Never needs to be sold, and never changes
    assert item.quality == 80  # Quality CAN exceed 50 if it's initialised at over 50


def test_backstage_pass():
    """Docs:-
    "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    Quality drops to 0 after the concert
    """
    gilded_rose, item = setup_gilded_rose(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20)
    )
    gilded_rose.update_quality()
    assert item.sell_in == 10
    assert item.quality == 21  # The sell_in was 11 when the function was called - hence this dropped by 1

    gilded_rose.update_quality()
    assert item.sell_in == 9
    assert item.quality == 23  # Increases by 2

    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert item.sell_in == 5
    assert item.quality == 31

    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 34  # Increases by 3 when sell_in less than 5

    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert item.sell_in == 0
    assert item.quality == 46

    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0  # quality is 0 after the gig

    gilded_rose.update_quality()
    assert item.sell_in == -2
    assert item.quality == 0  # quality is 0 after the gig


def test_conjured_mana_cake():
    run_for_standard_item(name="Conjured Mana Cake")
