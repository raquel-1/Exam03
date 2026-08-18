# Valid Anagram

Write a function:
```python
def valid_anagram(s: str, t: str) -> bool:
```

Returns `True` if `s` and `t` are anagrams of each other, `False` otherwise.

Two strings are anagrams if they contain the **exact same characters with the same frequencies**, regardless of order.

## Examples

```
valid_anagram("racecar", "carrace")  → True
valid_anagram("jar", "jam")          → False
valid_anagram("listen", "silent")    → True
valid_anagram("aabbcc", "abcabc")    → True
valid_anagram("abc", "ab")           → False
valid_anagram("", "")                → True
```

## Constraints
- `0 <= len(s), len(t) <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Allowed functions
`sorted()` — or manual frequency counting.
