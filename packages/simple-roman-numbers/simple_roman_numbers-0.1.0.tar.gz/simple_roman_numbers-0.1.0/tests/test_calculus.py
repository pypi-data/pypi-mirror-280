from simple_roman_numbers import RomanNumber

def test_suma():
    assert RomanNumber(7144733) + 1 == RomanNumber(7144734)
    assert 1 + RomanNumber(1) == RomanNumber(2)

def test_resta():
    assert RomanNumber(7) - 3 == RomanNumber("IV")

    assert RomanNumber(3) - 4 == RomanNumber("-I")

def test_producto():
    assert 1000 * RomanNumber(64) == RomanNumber("LXIV•")
    assert 3.5 * RomanNumber(4) == RomanNumber(14)


def test_division_entera():
    RomanNumber("II")
    assert 365 / RomanNumber("XII") == RomanNumber(30)