from simple_roman_numbers.funcs import groups, unidades
from simple_roman_numbers import RomanNumber

def test_grupos_menor_1000():
    assert groups(999) == (999,)
    assert groups(87) == (87,)
    assert groups(4) == (4,)

def test_grupos_mayor_1000():
    assert groups(1999) == (1999,)
    assert groups(2999) == (2999,)
    assert groups(3999) == (3999,)
    assert groups(4999) == (999, 4)
    assert groups(4000) == (0, 4)

def test_grupos_mayor_1000000():
    assert groups(1000999) == (999, 1000)
    assert groups(2000999) == (999, 2000)
    assert groups(3000999) == (999, 3000)
    assert groups(4000999) == (999, 0, 4)

def test_decimal_to_roman_menor_10():
    assert str(RomanNumber(0)) == ""
    assert str(RomanNumber(1)) == "I"
    assert str(RomanNumber(2)) == "II"
    assert str(RomanNumber(3)) == "III"
    assert str(RomanNumber(4)) == "IV"
    assert str(RomanNumber(5)) == "V"
    assert str(RomanNumber(6)) == "VI"
    assert str(RomanNumber(7)) == "VII"
    assert str(RomanNumber(8)) == "VIII"
    assert str(RomanNumber(9)) == "IX"

def test_romper_en_unidades():
    assert unidades(1987) == (7, 8, 9, 1)
    assert unidades(2007) == (7, 0, 0, 2)

def test_decimal_to_roman_menor_100():
    assert str(RomanNumber(0)) == ""
    assert str(RomanNumber(10)) == "X"
    assert str(RomanNumber(20)) == "XX"
    assert str(RomanNumber(30)) == "XXX"
    assert str(RomanNumber(40)) == "XL"
    assert str(RomanNumber(50)) == "L"
    assert str(RomanNumber(60)) == "LX"
    assert str(RomanNumber(70)) == "LXX"
    assert str(RomanNumber(80)) == "LXXX"
    assert str(RomanNumber(90)) == "XC"
 
def test_numeros_compuestos_menores_4000():
    assert str(RomanNumber(39)) == "XXXIX"
    assert str(RomanNumber(3499)) == "MMMCDXCIX"

    assert RomanNumber("DCCCXCVII").value == 897

def test_numeros_romanos_iguales():
    assert RomanNumber(4) == RomanNumber("IV")

def test_numeros_compuestos_mayores_3999():
    assert str(RomanNumber(4000)) == "IV•"
    assert str(RomanNumber(4004004)) == "IV••IV•IV"
    assert str(RomanNumber(7897456)) == "VII••DCCCXCVII•CDLVI"

    assert RomanNumber(7897456) == RomanNumber("VII••DCCCXCVII•CDLVI")

    