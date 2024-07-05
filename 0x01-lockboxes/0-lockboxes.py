#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): List of boxes where each
        box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    num_boxes = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < num_boxes and key not in opened:
                    stack.append(key)

    return len(opened) == num_boxes
