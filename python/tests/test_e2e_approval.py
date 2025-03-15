from approvaltests import verify
from approvaltests.reporters import PythonNativeReporter

from ..gilded_rose.manager import GildedRose


def tests_e2e_approval(all_items):
    reporter = PythonNativeReporter()
    gilded_rose = GildedRose(all_items)
    output = ["OMGHAI!"]
    for day in range(31):
        output.append(f"-------- day {day} --------")
        output.append("name, sellIn, quality")
        for item in all_items:
            output.append(str(item))
        output.append("")
        gilded_rose.update_quality()
    verify("\n".join(output), reporter=reporter)
