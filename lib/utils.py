def to_binstr(value: int, length: int) -> str:
    return bin(value)[2:].zfill(length)[-length:]
