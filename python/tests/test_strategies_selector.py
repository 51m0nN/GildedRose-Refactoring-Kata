import pytest
from ..gilded_rose.stock import Item
from ..gilded_rose.strategies.selector import StrategySelector

from ..gilded_rose.strategies.updaters import (
    update_sulfuras_item,
    update_brie_item,
)


@pytest.mark.parametrize(
    "item, expected_strategy",
    [
        (Item(name="Elixir of the Mongoose", sell_in=2, quality=4), None),
        (Item(name="Aged Brie", sell_in=2, quality=45), update_brie_item),
        (Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80), update_sulfuras_item),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20), None),
    ],
)
def test_selector(item, expected_strategy):
    update_selector = StrategySelector()
    updater = update_selector.select(item)
    assert updater is expected_strategy
