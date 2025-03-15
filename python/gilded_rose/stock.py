from dataclasses import dataclass


@dataclass
class Item:
    """An Item of stock managing its quality as time flows

    The Ork has long gone, he will never know I converted this to a dataclass - which is a more modern way of dealing
    with this, added this docstring, and the nice type hints...
    """

    name: str
    sell_in: int
    quality: int

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
