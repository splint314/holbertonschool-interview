#!/usr/bin/python3

"""Determines if all the boxes can be opened."""


def canUnlockAll(boxes):

    list = [0]
    for i in list:
        for j in boxes[i]:
            if j not in list and j < len(boxes):
                list.append(j)
    return len(list) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], []]
    print(canUnlockAll(boxes))
    boxes = [[1, 3], [3, 0, 1], [2], [0]]
    print(canUnlockAll(boxes))
