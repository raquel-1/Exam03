# Convert Base

Write a function:
```python
def convert_base(number: str, from_base: int, to_base: int) -> str:
```

Convert `number` (a string representation) from `from_base` to `to_base` and **return** the result as a string.

## Rules
- Both bases must be in the range **[2, 36]**; return `"ERROR"` otherwise.
- Digits use `0–9` then `A–Z` (case-insensitive input, uppercase output).
- If `number` contains a character invalid for `from_base`, return `"ERROR"`.
- If the value is zero, return `"0"`.

## Examples

```
convert_base("1010", 2, 10)   → "10"
convert_base("10",  2, 10)    → "2"
convert_base("ff",  16, 2)    → "11111111"
convert_base("1A",  16, 10)   → "26"
convert_base("ZZZ", 36, 10)   → "46655"
convert_base("0",   10, 2)    → "0"
convert_base("2",   2,  10)   → "ERROR"   (digit '2' invalid in base-2)
convert_base("1g",  16, 10)   → "ERROR"   (digit 'g' invalid in base-16)
```

## Constraints
- `2 <= from_base, to_base <= 36`
- `1 <= len(number) <= 50`

## Allowed functions
None (no imports). Using Python's built-in `int(x, base)` is allowed.
