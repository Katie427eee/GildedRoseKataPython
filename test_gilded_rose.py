# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)

        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(5, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras, Hand of Ragnaros", sulfuras_item.name)
        # self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Aged Brie", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()

        # self.assertEquals(["Aged Brie", 5, 80], all_items)
        self.assertEqual(1, len(all_items))
        self.assertEqual("Aged Brie", all_items[0].name)
        self.assertEqual(5, all_items[0].sell_in)
        self.assertEqual(80, all_items[0].quality)

    def test_conjured_item_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_aged_brie_quality_increase_after_sell_in(self):
        items = [Item("Aged Brie", -1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # self.assertEqual(41, items[0].quality)
        self.assertEqual(42, items[0].quality)

    def test_sulfuras_quality_always_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_get_item_names_method_exists(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        names = gilded_rose.get_item_names()
        self.assertEqual(["foo"], names)


if __name__ == '__main__':
    unittest.main()
