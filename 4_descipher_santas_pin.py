def decode_santa_pin(code: str) -> str:
    pin = []
    blocks = code[1:-1].split("][")

    for block in blocks:
        if block[0] == "<":
            pin.append(pin[-1])
        else:
            num = int(block[0])
            for op in block[1:]:
                num = (num + 1) % 10 if op == "+" else (num - 1) % 10
            pin.append(num)

    if len(pin) >= 4:
        return "".join(map(str, pin))
    return None
