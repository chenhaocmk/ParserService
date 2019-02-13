"""
Parser classes
"""
import string

from src.common.unit import Unit

__author__ = 'haochen'


MAX_ELEMENTS_IN_INPUT = 3
UNIT_DICT = {
    'cup': Unit.CUP,
    'cups': Unit.CUP,
    'tsp': Unit.TEASPOON,
    'tsp.': Unit.TEASPOON,
    'teaspoon': Unit.TEASPOON,
    'teaspoons': Unit.TEASPOON,
    'g': Unit.GRAM,
    'gram': Unit.GRAM,
    'grams': Unit.GRAM
}


class Parser(object):
    def parse(self, input_string: str) -> dict:
        """
        Parse the input str to dict as output. Required be implemented for child classes.
        :param input_string: Input string.
        :return: Output dict.
        """
        raise NotImplementedError("You have to set this method on subclasses")


class IngredientParser(Parser):
    def __init__(self):
        """
        This parser parse the input string to dict with number, unit and item
        """
        self.number = None
        self.unit = None
        self.item = None

        self.input_list = []
        self.curr_index = 0

    def parse(self, input_string: str):
        """
        Parse input string to dict with number, unit and item
        :param input_string: Input string
        :return: Desired structure of parsed info
        """
        self._clear()
        self.input_list = input_string.split(maxsplit=MAX_ELEMENTS_IN_INPUT)
        self.curr_index = 0

        self._parse_number()
        self._parse_unit()
        self._parse_item()

        return self._output()

    def _parse_number(self):
        """
        Try parse number of the input for element at current index of input list
        Increase index if number is found
        """
        # Only digit and dot are accepted. Oct and Hex not supported.
        if self.number is None and set(self.input_list[self.curr_index]).issubset(string.digits + '.'):
            if '.' in self.input_list[self.curr_index]:
                self.number = float(self.input_list[self.curr_index])
            else:
                self.number = int(self.input_list[self.curr_index])
            self.curr_index += 1

    def _parse_unit(self):
        """
        Try parse unit of the input for element at current index of input list
        Increase index if unit is found
        """
        if self.unit is None and self.input_list[self.curr_index].lower() in UNIT_DICT:
            self.unit = UNIT_DICT[self.input_list[self.curr_index].lower()]
            self.curr_index += 1

            # remove the coming up "of"
            if self.input_list[self.curr_index].lower() == 'of':
                self.curr_index += 1

    def _parse_item(self):
        """
        Parse item of the input for elements start at current index
        """
        if self.item is None:
            self.item = ' '.join(self.input_list[self.curr_index:])

    def _clear(self):
        """
        Clear current parser
        """
        self.__init__()

    def _output(self):
        """
        Output a dict of number/unit/item
        :return: dict
        """
        return {
            'number': str(self.number) if self.number is not None else '',
            'unit': self.unit.name.lower() if self.unit is not None else '',
            'item': self.item if self.item else ''
        }
