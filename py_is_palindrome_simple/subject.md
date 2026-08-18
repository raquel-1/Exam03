# Is Palindrome (Simple)

> ⚠️ **Reconstructed subject** — no original subject file found. Written to match the solution behavior.

Write a function:
```python
def is_palindrome(word: str) -> bool:
```

Returns `True` if `word` reads the same forwards and backwards (exact character match, **case-sensitive**), and `False` otherwise.

Unlike the "echo validator" variant, this version does **not** strip non-alphanumeric characters and is **case-sensitive**.

## Examples

```
is_palindrome("racecar")  → True
is_palindrome("madam")    → True
is_palindrome("hello")    → False
is_palindrome("Ana")      → False   (case-sensitive: 'A' ≠ 'a')
is_palindrome("")         → True
is_palindrome("a")        → True
```

## Constraints
- `0 <= len(word) <= 10^4`
- Input may contain any characters.

## Allowed functions
None (no imports)
