# utf8_validation

Given a list of integers, each representing one byte, this challenge determines whether that sequence of bytes forms a valid UTF-8 encoding. The solution inspects the leading bits of each byte: when not already inside a multi-byte character, those bits declare how many continuation bytes should follow (0, 1, 2, or 3); each continuation byte is then checked to make sure it starts with the bit pattern `10`. Any mismatch, or a sequence that ends mid-character, makes the data invalid.

| File | Description |
|---|---|
| `0-validate_utf8.py` | `validUTF8(data)` — returns `True` if `data` represents a valid UTF-8 encoding, `False` otherwise. |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
