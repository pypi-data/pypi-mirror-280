from simple_roman_numbers import symbols, rules, values, ordered_symbol

def groups(n: int) -> tuple:
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

def unidades(n):
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

def to_roman(n):
    g_miles = groups(n)
    todos = []
    for num_millar, valor in enumerate(g_miles):
        g_unidades = unidades(valor)
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
            
        todos.append("".join(res[::-1]) + "•" * num_millar)
    return "".join(todos[::-1])    


def to_decimal(rn: str) -> int:
    accum = 0
    cad = ""
    ant = float('inf')
    for symbol in rn:
        if symbol in next_symbol(cad):
            valor = values(symbol)
            if valor > ant:
                accum -= 2 * ant
            accum += valor
            ant = valor
            cad += symbol
        else:
            raise ValueError(f"bad {symbol} after {cad}.")
    return accum

def before(cad, pos):
    try:
        s = cad[-pos]
        return rules[s]
    except IndexError:
        return ""


def next_symbol(prev: str) -> tuple:
    last = before(prev, 1)
    penultimate = before(prev, 2)
    antepenultimate = before(prev, 3)
    if not last:
        return tuple(rules.keys())

    res = []
    if last.valor == 1:
        if antepenultimate == penultimate == last:
            pass
        elif penultimate == last:
            res.append(last.symbol)
        elif penultimate and penultimate.orden == last.orden:
            res.append(last.symbol)
        elif penultimate and penultimate.orden < last.orden:
            last = penultimate
        else:
            pos = ordered_symbol.index(last.symbol)
            if pos > 1:
                res.append(ordered_symbol[pos - 2])
                res.append(ordered_symbol[pos - 1])
            res.append(last.symbol)
    elif penultimate and penultimate.valor == 1 and penultimate.orden == last.orden:
        last = rules[ordered_symbol[ordered_symbol.index(last.symbol) + 1]]
    res += ordered_symbol[ordered_symbol.index(last.symbol) + 1:]
    return set(res)
    
def separate_symbol_in_millars(cad):
    groups = cad.split("•")
    res = []
    res.append(groups.pop())
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