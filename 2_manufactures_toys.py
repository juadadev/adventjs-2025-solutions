def manufacture_gifts(gifts_to_produce):
    result = []

    for item in gifts_to_produce:
        toy = item.get("toy")
        quantity = item.get("quantity")

        if isinstance(quantity, (int, float)) and quantity > 0:
            result.extend([toy] * int(quantity))

    return result
