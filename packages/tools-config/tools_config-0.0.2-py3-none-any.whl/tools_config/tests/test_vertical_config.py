import unittest

from ..vertical import VerticalConfigStore
from ..vertical import VerticalConfig


class VerticalTest(unittest.TestCase):

    def setUp(self):
        self.verticalStore = VerticalConfigStore()

    def test_save(self):
        assert isinstance(self.verticalStore.save(1,
                                                  "globalVertical1",
                                                  "displayVertical1",
                                                  {"addnlVKey1": "addnlVValue1",
                                                   "addnlVKey2": "addnlVValue2"}),
                          VerticalConfig)
        assert isinstance(self.verticalStore.save(2, "globalVertical2"),
                          VerticalConfig)

    def test_bulk_save(self):
        vertical_partner_dict = [{"partner": 3,
                                  "vertical": "globalVertical3",
                                  "display_vertical": "displayVertical3",
                                  "additional": {"addnlVKey3": "addnlVValue3",
                                                 "addnlVKey4": "addnlVValue4"}},
                                 {"partner": 4, "vertical": "globalVertical4"}]
        saved_verticals = self.verticalStore.bulk_save(vertical_partner_dict)
        assert isinstance(saved_verticals, list)
        self.assertEqual(len(saved_verticals), 2)
        assert isinstance(saved_verticals[0], VerticalConfig)
        assert isinstance(saved_verticals[1], VerticalConfig)

    def test_find(self):
        partner = 1
        fetched_vertical = self.verticalStore.find(partner)
        if fetched_vertical is not None:
            assert isinstance(fetched_vertical, VerticalConfig)

    def test_bulk_find(self):
        partner_list = [1, 2, 3, 4]
        fetched_verticals = self.verticalStore.bulk_find(tuple(partner_list))

        assert isinstance(fetched_verticals, list)
        self.assertEqual(len(fetched_verticals), 4)

        if fetched_verticals[0] is not None:
            assert isinstance(fetched_verticals[0], VerticalConfig)

        if fetched_verticals[1] is not None:
            assert isinstance(fetched_verticals[1], VerticalConfig)

        if fetched_verticals[2] is not None:
            assert isinstance(fetched_verticals[2], VerticalConfig)

        if fetched_verticals[3] is not None:
            assert isinstance(fetched_verticals[3], VerticalConfig)

    def test_update(self):
        updated = self.verticalStore.update(1, display_vertical="displayVerticalUpdated",
                                            additional={"updatedKey": "updatedValue"})
        if updated is not None:
            self.assertTrue(updated)

    def test_bulk_update(self):
        vertical_partner_dict = [{"partner": 3},
                                 {"partner": 4, "vertical": "updatedVertical"}]
        updated_vertical_results = self.verticalStore.bulk_update(vertical_partner_dict)

        assert isinstance(updated_vertical_results, list)
        self.assertEqual(len(updated_vertical_results), 2)

        if updated_vertical_results[0] is not None:
            self.assertTrue(updated_vertical_results[0])

        if updated_vertical_results[1] is not None:
            self.assertTrue(updated_vertical_results[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
