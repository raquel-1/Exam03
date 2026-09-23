def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    try:
        if not 2 <= from_base <= 36:
            return "ERROR"
        if not 2 <= to_base <= 36:
            return "ERROR"
        
        n_decimal = int(number, from_base)
        if n_decimal == 0:
            return "0"
        
        res = ""
        while n_decimal:
            res += digits[n_decimal % to_base]
            n_decimal //= to_base
        
        return res[::-1]
    except Exception:
        return "ERROR"

print(number_base_converter("FF", 16, 10)) # "255"
print(number_base_converter("00FF", 16, 2)) # "11111111"
print(number_base_converter("Z", 36, 10)) # "35"
print(number_base_converter("0000", 7, 10)) # "0"
print(number_base_converter("0001", 2, 10)) # "1"
print(number_base_converter("1010", 2, 16)) # "A"
print(number_base_converter("133742", 8, 42)) #ERROR