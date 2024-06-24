CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"
CHAR_TO_VALUE = {char: index for index, char in enumerate(CHARS)}

def _base36_to_int(base36_integer):
    """Converts a base36 integer to its corresponding decimal value."""

    integer_value = 0
    for char in base36_integer:
        integer_value = integer_value * 36 + CHAR_TO_VALUE[char]
    return integer_value


def _base36_to_frac(base36_fractional):
    """Converts a base36 fractional value to a decimal fraction."""
    
    fractional_value = 0
    base = 1 / 36
    for char in base36_fractional:
        fractional_value += CHAR_TO_VALUE[char] * base
        base /= 36
    return fractional_value


def _int_to_base36(integer_part):
    """Converts an integer to a base36 string representation."""
    
    if integer_part == 0:
        return "0"
    
    base36_integer = []
    
    while integer_part > 0:
        remainder = integer_part % 36
        base36_integer.append(CHARS[remainder])
        integer_part //= 36
        
    return ''.join(reversed(base36_integer))


def _frac_to_base36(fractional_part, precision=8):
    """Converts the fractional part of a number to base36 representation.

    Args:
        fractional_part (float): The fractional part of the number.
        precision (int, optional): The number of digits to include in the base36 representation. Defaults to 8.
    """

    base36_fraction = []
    
    for _ in range(precision):
        fractional_part *= 36
        integer_part = int(fractional_part)
        base36_fraction.append(CHARS[integer_part])
        fractional_part -= integer_part
        
    return ''.join(base36_fraction)


def encode(number, precision=8):
    """
    Encodes a given number into a base36 string representation.

    Args:
        number (int or float): The number to be encoded.
        precision (int): The precision of the fractional part. Default is 8.

    
        str: The base36 string representation of the given number.
    """
    if not isinstance(number, (int, float)):
        raise TypeError("number must be an int or float")
    
    integer_part = int(number)
    fractional_part = number - integer_part
    
    base36_integer = _int_to_base36(integer_part)
    base36_fractional = _frac_to_base36(fractional_part, precision)
    
    return base36_integer + base36_fractional


def decode(base36_number, precision=8):
    """
    Decode a base36 number into its decimal representation.

    Args:
        base36_number (str): The base36 number to decode.
        precision (int, optional): The number of digits after the decimal point. Defaults to 8.

    Returns:
        float: The decimal representation of the base36 number.

    """
    base36_integer = base36_number[:-precision]
    base36_fractional = base36_number[-precision:]
    
    integer_value = _base36_to_int(base36_integer)
    fractional_value = _base36_to_frac(base36_fractional)
    
    return integer_value + fractional_value
