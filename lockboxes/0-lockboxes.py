#!/usr/bin/python3

def canUnlockAll(boxes):

    if not boxes:
        return False

    unlocked = [0]
    for box_id in unlocked:
        for key in boxes[box_id]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)

    return len(unlocked) == len(boxes)
