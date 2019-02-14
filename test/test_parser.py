"""
Unit test for parser
"""
import unittest

from src.model.parser import IngredientParser


class TestIngredientParser(unittest.TestCase):
    def testParse(self):
        parser = IngredientParser()
        self.assertEqual(parser.parse('1 cup of milk chocolate'), {
            'number': '1', 'unit': 'cup', 'item': 'milk chocolate'
        })
        self.assertEqual(parser.parse('4 tsp. Orange juice'), {
            'number': '4', 'unit': 'teaspoon', 'item': 'Orange juice'
        })
        self.assertEqual(parser.parse('5 eggs'), {
            'number': '5', 'unit': '', 'item': 'eggs'
        })
        self.assertEqual(parser.parse('5 cups of salt'), {
            'number': '5', 'unit': 'cup', 'item': 'salt'
        })
        self.assertEqual(parser.parse('salt and pepper to taste'), {
            'number': '', 'unit': '', 'item': 'salt and pepper to taste'
        })
        self.assertEqual(parser.parse('3.5 GRAMS xanthum gum'), {
            'number': '3.5', 'unit': 'gram', 'item': 'xanthum gum'
        })
        self.assertEqual(parser.parse('-3.5 GRAMS xanthum gum'), {
            'number': '', 'item': '-3.5 GRAMS xanthum gum', 'unit': ''
        })

if __name__ == '__main__':
    unittest.main()
