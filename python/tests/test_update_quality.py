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
