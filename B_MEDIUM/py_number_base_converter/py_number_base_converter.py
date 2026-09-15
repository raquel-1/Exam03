def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    line = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    # base in range
    if from_base < 2 or from_base > 36:
        return "ERROR"
    if to_base < 2 or to_base > 36:
        return "ERROR"

    # int to decimal
    try:
        num_decimal = int(number, from_base)
    except ValueError:
        return "ERROR"

    if num_decimal == 0:
        return str(0)

    while num_decimal > 0:
        resto = num_decimal  % to_base
        result = line[resto] + result
        num_decimal = num_decimal // to_base

    return result

if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("123", 10, 2))
    print(number_base_converter("Z", 36, 10))
    print(number_base_converter("35", 10, 36))
    print(number_base_converter("123", 1, 10))
    print(number_base_converter("G", 16, 10))
