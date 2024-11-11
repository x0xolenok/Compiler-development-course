def find_unproductive_non_terminals(grammar):
    productive_non_terminals = set()

    # Iterate through all rules and collect productive non-terminals
    for _ in range(len(grammar)):
        for non_terminal, rules in grammar.items():
            if non_terminal in productive_non_terminals:
                continue
            if any(all(symbol in productive_non_terminals or symbol.islower() for symbol in rule) for rule in rules):
                productive_non_terminals.add(non_terminal)

    return set(grammar.keys()) - productive_non_terminals


def find_unreachable_non_terminals(grammar, start_symbol="S"):
    reachable_non_terminals = set()

    def dfs(non_terminal):
        if non_terminal in reachable_non_terminals:
            return
        reachable_non_terminals.add(non_terminal)
        for rule in grammar.get(non_terminal, []):
            for symbol in rule:
                if symbol.isupper():
                    dfs(symbol)

    # Start DFS from the start symbol
    dfs(start_symbol)
    return set(grammar.keys()) - reachable_non_terminals


def find_nullable_non_terminals(grammar):
    nullable_non_terminals = set()
    stack = [non_terminal for non_terminal, rules in grammar.items() if [] in rules]

    # Initially add all rules that can derive empty to nullable set
    nullable_non_terminals.update(stack)

    # Process stack and determine other nullable non-terminals
    while stack:
        current = stack.pop()
        for non_terminal, rules in grammar.items():
            if non_terminal in nullable_non_terminals:
                continue
            if any(all(symbol in nullable_non_terminals for symbol in rule) for rule in rules):
                nullable_non_terminals.add(non_terminal)
                stack.append(non_terminal)

    return nullable_non_terminals


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
