import math

import roman


class Integer:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_float(float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return Integer(math.floor(float_value))

    @staticmethod
    def from_roman(value):
        return Integer(roman.fromRoman(value))

    @staticmethod
    def from_string(value:str):
        try:
            if not isinstance(value, str):
                return "wrong type"
            return Integer(int(value))
        except ValueError:
            return "wrong type"