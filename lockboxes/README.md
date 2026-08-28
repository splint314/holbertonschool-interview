# lockboxes

Given a list of boxes, each containing a set of keys to other boxes, this challenge determines whether every box can eventually be unlocked starting from box `0` (which is always unlocked). The solution performs a reachability traversal: it maintains a growing list of opened boxes, seeded with box `0`, and repeatedly walks through the keys found in each newly opened box, adding any box they unlock that hasn't been reached yet. All boxes are unlockable exactly when this process ends up covering every box in the list.

| File | Description |
|---|---|
| `0-lockboxes.py` | `canUnlockAll(boxes)` — returns `True` if every box can be opened, `False` otherwise. |
| `main_0.py` | Sample driver script exercising `canUnlockAll` on a few box configurations. |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
