from collections import namedtuple

MILLAR_SYMBOL = "•"

symbols = {
    3: {1: 'M'},
    2: {5: 'D', 1: 'C'},
    1: {5: 'L', 1: 'X'},
    0: {5: 'V', 1: 'I'}
}


class RomanDigit(namedtuple('Rule',('symbol', 'orden', 'valor'))):
    __slots__ = ()

    def __bool__(self):
        return bool(self.symbol)
    
    @property
    def value(self):
        return self.orden * self.valor


rules = {
    "I": RomanDigit("I", 0, 1),
    "V": RomanDigit("V", 0, 5),
    "X": RomanDigit("X", 1, 1),
    "L": RomanDigit("L", 1, 5),
    "C": RomanDigit("C", 2, 1),
    "D": RomanDigit("D", 2, 5),
    "M": RomanDigit("M", 3, 1),
    "": RomanDigit("", 0, 0)
}

def values(s: str):
    r = rules[s]
    return r.valor * 10 ** r.orden

ordered_symbol = list(map(lambda r: r.symbol,
                          sorted(rules.values(), key=lambda r: values(r.symbol), reverse=True)
                          ))

class RomanNumber:
    def __init__(self, value: object):
        if isinstance(value, int):
            self.__value = value
            self.__lit = self.__to_roman()
        elif isinstance(value, float):
            self.__value = value // 1
            self.__lit = self.__to_roman()
        elif isinstance(value, str):
            self.__lit = value
            self.__value = self.to_decimal()
        else:
            raise AttributeError(f"{value} must be integer or string")
                                 
    def __to_roman(self):
        g_miles = self.__separate_in_millars()
        todos = []
        for num_millar, valor in enumerate(g_miles):
            g_unidades = self.__separate_in_units(valor)
            res = []
            for orden, n in enumerate(g_unidades):
                if n <= 3:
                    res.append(n * symbols[orden][1])
                elif n == 4:
                    res.append(symbols[orden][1] + symbols[orden][5])
                elif n < 9:
                    res.append(symbols[orden][5] + (n - 5) * symbols[orden][1])
                else:
                    res.append(symbols[orden][1] + symbols[orden + 1][1])
                
            todos.append("".join(res[::-1]) + MILLAR_SYMBOL * num_millar)
        repr = "".join(todos[::-1])    
        if self.value < 0:
            return "-" + repr
        else:
            return repr
    
    def __separate_in_millars(self):
        n = abs(self.__value)
        res = []
        resto = n % 1000
        n = n // 1000
        while n != 0:
            res.append(resto)
            resto = n % 1000
            n = n // 1000
        res.append(resto)
        
        if len(res) > 1 and res[-1] < 4:
            res[-2] += res[-1] * 1000
            res.pop()
        
        return tuple(res)

    def __separate_symbol_in_millars(self):
        if len(self.lit) and self.lit[0] == "-":
            lit = self.lit[1:]
        else:
            lit = self.lit
        groups = lit.split(MILLAR_SYMBOL)
        res = []
        if len(groups):
            res.append(groups.pop())
        if len(groups):
            res.append(groups.pop())

        ix = 0
        cuenta_blancos = 1
        groups = groups[::-1]
        
        for group in groups:
            if not group:
                cuenta_blancos += 1
            else:
                if cuenta_blancos > len(res):
                    res += [""] * (cuenta_blancos - len(res))
                    cuenta_blancos = 1
                elif cuenta_blancos < len(res) - 1:
                    raise ValueError("Incorrect input, probably order")
                res.append(group)
        
        return res

    def __separate_in_units(self, n):
        if n > 3999:
            raise ValueError(f"{n} must be less of 4000")
        res = []
        resto = n % 10
        n = n // 10
        while n > 0:
            res.append(resto)
            resto = n % 10
            n = n // 10
        res.append(resto)      
        return tuple(res)  
    
    def __before(self, cad, pos):
        try:
            s = cad[-pos]
            return rules[s]
        except IndexError:
            return rules[""]
        except KeyError:
            return rules[""]

    def __absolute_value(self, cad):
        last = self.__before(cad, 1)
        penultimate = self.__before(cad, 2)
        antepenultimate = self.__before(cad, 3)

        if not last:
            return 0
        elif last.valor == 5 and penultimate.valor == 1 and last.orden == penultimate.orden:
            return 4
        elif last.valor == 5:
            return 5
        elif last.valor == 1 and penultimate.valor == 1 and last.orden == penultimate.orden + 1:
            return 9
        elif last.valor == 1 and penultimate.valor == 5 and last.orden == penultimate.orden:
            return 6
        elif last == penultimate == antepenultimate and last.valor == 1:
            return 3
        elif last == penultimate and last.valor == 1:
            return 2
        else:
            return 1
            

    def __next_symbol(self, prev: str) -> tuple:
        res = []
        prev_value = self.__absolute_value(prev)

        if prev_value == 0:
             # Devuelve todos los simbolos
            res += ordered_symbol 
        elif prev_value == 3 or prev_value == 5:
            # Devuelve los simbolos menores que el ultimo
            res = ordered_symbol[ordered_symbol.index(prev[-1]) + 1:] 
        elif prev_value == 4 or prev_value == 9:
            # Devuelve los simbolos menores que el penultimo
            res = ordered_symbol[ordered_symbol.index(prev[-2]) + 1:]
        elif prev_value == 2 or prev_value == 6:
            # Devuelve los simbolos menores o iguales que el ultimo
            res = ordered_symbol[ordered_symbol.index(prev[-1]):] 
        else:
            # Si es uno debe devolver los menores o iguales que el RomanDigit de valor 1 y orden +1
            pos = max(ordered_symbol.index(prev[-1]) - 2, 0)  # Si es 'M' debe devolver todo
            res = ordered_symbol[pos:]
        
        return set(res)
        

    def to_decimal(self):
        millars = self.__separate_symbol_in_millars()
        list_accum = []
        for orden, millar in enumerate(millars):
            accum = 0
            cad = ""
            ant = float('inf')
            for symbol in millar:
                if symbol in self.__next_symbol(cad):
                    valor = values(symbol)
                    if valor > ant:
                        accum -= 2 * ant
                    accum += valor
                    ant = valor
                    cad += symbol
                else:
                    raise ValueError(f"bad {symbol} after {cad}.")
            
            list_accum.append(accum * 1000 ** orden)
        return sum(list_accum) * (-1 if self.lit[0] == "-" else 1)

    @property
    def value(self):
        return self.__value
    
    @property
    def lit(self):
        return self.__lit
    
    def __repr__(self) -> str:
        return f"{self.__lit}"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__): 
            return False
        return self.value == other.value
    
    def __hash__(self) -> int:
        return hash(self.value)


    def __add__(self, other):
        if isinstance(other, self.__class__):
            return RomanNumber(self.value + other.value)
        elif isinstance(other, int):
            return RomanNumber(self.value + other)
        elif isinstance(other, float):
            return RomanNumber(self.value + other // 1)
        raise TypeError(f"unsupported operand type(s) for +: '{self.__class__}' and '{other.__class__}'")
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return RomanNumber(self.value * other.value)
        elif isinstance(other, int):
            return RomanNumber(self.value * other)
        elif isinstance(other, float):
            return RomanNumber(int((self.value * other) // 1))
        raise TypeError(f"unsupported operand type(s) for *: '{self.__class__}' and '{other.__class__}'")
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return RomanNumber(self.value // other.value)
        elif isinstance(other, int):
            return RomanNumber(self.value // other)
        elif isinstance(other, float):
            return RomanNumber((self.value // other))
        raise TypeError(f"unsupported operand type(s) for /: '{self.__class__}' and '{other.__class__}'")
    
    def __rtruediv__(self, other):
        if isinstance(other, self.__class__):
            return RomanNumber(other.value // self.value)
        elif isinstance(other, int):
            return RomanNumber(other // self.value)
        elif isinstance(other, float):
            return RomanNumber((other // self.value))
        raise TypeError(f"unsupported operand type(s) for /: '{self.__class__}' and '{other.__class__}'")

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return RomanNumber(self.value - other.value)
        elif isinstance(other, int):
            return RomanNumber(self.value - other)
        elif isinstance(other, float):
            return RomanNumber(self.value - other // 1)
        raise TypeError(f"unsupported operand type(s) for +: '{self.__class__}' and '{other.__class__}'")
    
    def __rsub__(self, other):
        if isinstance(other, self.__class__):
            return RomanNumber(self.other - other.value)
        elif isinstance(other, int):
            return RomanNumber(other - self.value)
        elif isinstance(other, float):
            return RomanNumber(other - self.value // 1)
        raise TypeError(f"unsupported operand type(s) for +: '{self.__class__}' and '{other.__class__}'") 
    
