import unittest
import hub

class CatalogTests(unittest.TestCase):
    def test_catalog(self):
        items = hub.load_catalog()
        self.assertEqual(len(items), 47)
        self.assertEqual(len({i["repository"] for i in items}), 47)
        self.assertEqual(len(hub.select_items(items, recommended=True)), 7)

if __name__ == "__main__":
    unittest.main()
