# Valid Palindrome (Echo Validator)

Write a function:
```python
def valid_palindrome(s: str) -> bool:
```

Returns `True` if `s` is a palindrome after:
1. Keeping only **alphanumeric** characters (`isalnum()`).
2. Converting everything to **lowercase**.

Returns `False` otherwise.

## Examples

```
valid_palindrome("Was it a car or a cat I saw?")     → True
valid_palindrome("A man, a plan, a canal: Panama")   → True
valid_palindrome("No lemon, no melon")               → True
valid_palindrome("tab a cat")                        → False
valid_palindrome("race a car")                       → False
valid_palindrome("")                                 → True
valid_palindrome("a")                                → True
```

## Constraints
- `0 <= len(s) <= 2 * 10^5`
- `s` consists of printable ASCII characters.

## Allowed functions
`str.isalnum()`, `str.lower()`
