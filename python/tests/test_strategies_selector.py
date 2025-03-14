import pytest
from ..gilded_rose.stock import Item
from ..gilded_rose.strategies.selector import StrategySelector
from ..gilded_rose.strategies.updaters import (
    SupportsUpdatingItemsStrategy,
    StandardUpdaterStrategy,
    BrieUpdaterStrategy,
    SulfurasUpdaterStrategy,
    BackstagePassUpdaterStrategy,
)


@pytest.mark.parametrize(
    "item, expected_strategy",
    [
        (Item(name="Elixir of the Mongoose", sell_in=2, quality=4), StandardUpdaterStrategy),
        (Item(name="Aged Brie", sell_in=2, quality=45), BrieUpdaterStrategy),
        (Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80), SulfurasUpdaterStrategy),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20), BackstagePassUpdaterStrategy),
    ],
)
def test_selector(item, expected_strategy):
    update_selector = StrategySelector()
    updater = update_selector.select(item)
    assert isinstance(updater, expected_strategy)
    assert isinstance(updater, SupportsUpdatingItemsStrategy)
