def find_unproductive_non_terminals(grammar):
    productive = set()
    changed = True

    while changed:
        changed = False
        for non_terminal, rules in grammar.items():
            if non_terminal in productive:
                continue
            for rule in rules:
                if all(symbol in productive or symbol.islower() for symbol in rule):
                    productive.add(non_terminal)
                    changed = True
                    break

    return set(grammar.keys()) - productive


def find_unreachable_non_terminals(grammar, start_symbol="S"):
    reachable = set([start_symbol])
    changed = True

    while changed:
        changed = False
        for non_terminal in list(reachable):
            for rule in grammar.get(non_terminal, []):
                for symbol in rule:
                    if symbol.isupper() and symbol not in reachable:
                        reachable.add(symbol)
                        changed = True

    return set(grammar.keys()) - reachable


def find_nullable_non_terminals(grammar):
    nullable = set()
    changed = True

    while changed:
        changed = False
        for non_terminal, rules in grammar.items():
            if non_terminal in nullable:
                continue
            for rule in rules:
                if all(symbol in nullable for symbol in rule):
                    nullable.add(non_terminal)
                    changed = True
                    break

    return nullable


# Example usage
grammar = {
    "S": [["A", "B"], ["C"]],
    "A": [["a", "A"], ["b"]],
    "B": [["b", "B"], []],
    "C": [["c"]],
    "D": [["d", "E"]],
    "E": [["e"]],
    "F": [["G"]],
    "G": [["H"]],
    "H": [["h", "I"]],
    "I": [["i", "J"]],
}

print("Unproductive non-terminals:", find_unproductive_non_terminals(grammar))
print("Unreachable non-terminals:", find_unreachable_non_terminals(grammar, start_symbol="S"))
print("Nullable non-terminals:", find_nullable_non_terminals(grammar))
