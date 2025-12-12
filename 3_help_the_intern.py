def draw_gift(size, symbol) -> str:
    if size < 2:
        return ""

    borders = size * symbol
    middle = (symbol + " " * (size - 2) + symbol + "\n") * (size - 2)
    return borders + "\n" + middle + borders
