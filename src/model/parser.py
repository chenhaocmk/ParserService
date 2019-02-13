"""
Parser classes
"""
import string

import src.config.parserConfig as parser_config

__author__ = 'haochen'


class Parser(object):
    def parse(self, input: str) -> dict:
        """
        Parse the input str to dict as output. Required be implemented for child classes.
        :param input: Input string.
        :return: Output dict.
        """
        raise NotImplementedError("You have to set this method on subclasses")


class IngredientParser(Parser):
    def __init__(self):
        self.number = ""
        self.unit = None

    def starts_with_number(self, txt):
        if txt[0] in string.digits:
            return True
        else:
            return False

    def parse_remainder(self, num_chars, txt):
        return self.parse(txt[num_chars:].strip())

    def parse(self, txt):
        if self.starts_with_number(txt):
            self.number += txt[0]
            return self.parse_remainder(1, txt)
        else:
            # maybe it's a unit
            for unit in parser_config.UNITS:
                for suffix in ['s', '.', '']:
                    suf_unit = unit + suffix
                    l = len(suf_unit)
                    if txt[:l].lower() == suf_unit:
                        self.unit = unit
                        return self.parse_remainder(len(suf_unit), txt)

            # we must be at the item
            return {"n": int(self.number) if self.number != "" else None,
                    "u": self.unit,
                    "f": txt.strip()}