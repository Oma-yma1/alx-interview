#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """You have n number of locked boxes"""
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                stack.append(key)
                visited[key] = True

    return all(visited)
