from simple_roman_numbers.funcs import to_decimal, next_symbol, separate_symbol_in_millars
from simple_roman_numbers import RomanNumber
import pytest

def test_suman_orden_mayor_a_menor():
    assert to_decimal("I") == 1
    assert to_decimal("VII") == 7
    assert to_decimal("LXVII") == 67

    with pytest.raises(ValueError):
        to_decimal("VL")

    assert to_decimal("MCMLVII") == 1957

def test_next_symbol():
    assert next_symbol("I") == {"X", "V", "I", ""}
    assert next_symbol("II") == {"I", ""}
    assert next_symbol("III") == {""}

    assert next_symbol("V") == {"I", ""}
    assert next_symbol("IV") == {""}
    assert next_symbol("X") == {"X", "L", "C", "V", "I", ""}

def test_roman_from_text():
    for i in range(1, 4000):
        assert RomanNumber(str(RomanNumber(i))).value == i

    with pytest.raises(ValueError):
        RomanNumber("IIII")

    with pytest.raises(ValueError):
        RomanNumber("VIIII")
    
    with pytest.raises(ValueError):
        RomanNumber("XIIII")
    
    with pytest.raises(ValueError):
        RomanNumber("IC")
    
    with pytest.raises(ValueError):
        RomanNumber("LL")
    
    with pytest.raises(ValueError):
        RomanNumber("XXL")

    with pytest.raises(ValueError):
        RomanNumber("VL")
    

def test_separate_symbols_in_millars():
    assert separate_symbol_in_millars("VII••DCCCXCVII•CDLVI") == ["CDLVI", "DCCCXCVII", "VII"]
    assert separate_symbol_in_millars("VII••CDLVI") == ["CDLVI", "", "VII"]
    assert separate_symbol_in_millars("VII•••DCCCXCVII•CDLVI") == ["CDLVI", "DCCCXCVII", "", "VII"]
    assert separate_symbol_in_millars("VII•••••DCCCXCVII••CDLVI") == ["CDLVI", "", "DCCCXCVII", "", "", "VII"]

    with pytest.raises(ValueError):
        separate_symbol_in_millars("VI•VII••IV")