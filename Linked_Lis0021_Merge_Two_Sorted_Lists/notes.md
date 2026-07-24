# Merge Two Sorted Lists

**Difficulty:**
Easy

**Pattern:** 
Linked List, Two Pointers

## Approach

- Create a dummy node to simplify building the merged list.
- Maintain a tail pointer that always points to the last node of the merged list.
- Compare the values of the current nodes in `list1` and `list2`.
- Attach the smaller node to `tail.next` and move the corresponding pointer.
- Move `tail` forward after each attachment.
- Once one list becomes empty, attach the remaining nodes of the other list.
- Return `dummy.next` as the head of the merged list.

---

## Time Complexity

- O(n + m)

## Space Complexity

O(1)
  

## Mistakes I Made

- Treated a linked list like a Python list by using:
  - `len(list1)`
  - `list1[i]`
  - `append()`
- Checked for an empty linked list using `[]` instead of `None`.
- Used `self.list1` and `self.list2` instead of the function parameters.
- Initialized `list3 = None` and tried to access `list3.next`.
- Used `.next()` as if it were a function (`list3.next(...)`) instead of assigning to it (`list3.next = node`).
- Forgot to move the `tail` pointer after attaching a node.
- Forgot to move `list2` in the `else` block.
- Tried to add only one remaining node instead of attaching the entire remaining list.
- Returned a Python list / incorrect pointer instead of the head of the merged linked list.
- Initially thought of the problem as **Merge Two Sorted Arrays** instead of **Merge Two Sorted Linked Lists**.


## Similar Questions

- Merge k Sorted Lists
- Merge Sorted Array
- Sort List
- Merge Two 2D Arrays by Summing Values

- Reverse Nodes in k-Group
- Sort List
- Add Two Numbers
