# Workshop Notes — Singly Linked List

## Goal
Implement a basic singly linked list with nodes, append-style insertion, removal by value, and an empty check.

## Structure
- `LinkedList.Node` is a nested class.
- Each node stores `element` and a `next` reference.
- `head` points to the first node, or `None` when the list is empty.
- `length` tracks the number of nodes.

## Methods
- `is_empty()` returns whether the length is zero.
- `add(element)` creates a node and walks to the end before linking it.
- `remove(element)` searches for the first matching element and reconnects the surrounding links. If the value is absent, it returns without changing the list.

## Important concepts
- A reference connects one node to the next.
- Removing the head requires updating `self.head`.
- Removing another node requires updating the previous node's `next`.
- Appending by traversal is O(n); searching/removing by value is O(n) in the worst case.

## Current demonstration
The script checks an empty list, adds 1 and 2, then prints the empty status and length. It does not currently print the node contents.

## Run
```bash
python "Linked list.py"
```
