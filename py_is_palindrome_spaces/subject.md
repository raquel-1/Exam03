# Is Palindrome (Ignore Spaces, Case-Insensitive)

> ⚠️ **Reconstructed subject** — no original subject file found. Written to match the solution behavior.

Write a function:
```python
def is_palindrome(text: str) -> bool:
```

Returns `True` if `text` is a palindrome after:
1. Converting all characters to **lowercase**.
2. Removing all **spaces** (but keeping other non-alpha characters).

Returns `False` otherwise.

> **Note:** This variant removes only spaces, not all non-alphanumeric characters.  
> For a version that strips all punctuation too, see `valid_palindrome`.

## Examples

```
is_palindrome("racecar")                      → True
is_palindrome("A man a plan a canal Panama")  → True
is_palindrome("Was it a car or a cat I saw")  → True
is_palindrome("Never odd or even")            → True
is_palindrome("hello")                        → False
is_palindrome("hello world")                  → False
is_palindrome("")                             → True
```

## Constraints
- `0 <= len(text) <= 10^4`

## Allowed functions
None (no imports)
