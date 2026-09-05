"""
DSA Core - Data Structures & Algorithms from scratch.

This file contains implementations of Linked List, Stack, Queue,
Binary Search, Sort algorithms, and Recursive problems.
Use as a reference — do not execute directly.
"""

# ============================================================================
# 1. LINKED LIST from scratch
# ============================================================================


class Node:
    """A node in a singly linked list."""
    __slots__ = "value", "next"

    def __init__(self, value: object) -> None:
        # Store the value and initialize next pointer to None
        self.value = value
        self.next: Node | None = None


class LinkedList:
    """Singly linked list implementation from scratch."""
    __slots__ = "head", "length"

    def __init__(self) -> None:
        # Start with an empty list (no head node)
        self.head: Node | None = None
        self.length = 0

    def traverse(self) -> list[object]:
        """Return all values in order by following next pointers.
        O(n) time, O(1) extra space."""
        result: list[object] = []
        current = self.head
        # Walk through each node until None
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def insert_at_head(self, value: object) -> None:
        """Insert a new node at the beginning. O(1) time."""
        new_node = Node(value)
        # New node points to current head
        new_node.next = self.head
        # Head becomes the new node
        self.head = new_node
        self.length += 1

    def insert_at_tail(self, value: object) -> None:
        """Append a new node at the end. O(n) time."""
        new_node = Node(value)
        if self.head is None:
            # Empty list: new node becomes head
            self.head = new_node
        else:
            # Walk to the last node
            current = self.head
            while current.next is not None:
                current = current.next
            # Attach new node at the end
            current.next = new_node
        self.length += 1

    def delete_by_value(self, value: object) -> bool:
        """Delete the first node with the given value. O(n) time."""
        if self.head is None:
            return False  # Nothing to delete

        # If the head itself holds the value
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return True

        # Search for the node just before the one to delete
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        # If we found the value
        if current.next is not None:
            current.next = current.next.next  # Bypass the node
            self.length -= 1
            return True
        return False  # Value not found

    def search(self, value: object) -> int:
        """Return the index of the first occurrence, or -1. O(n) time."""
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1


# ============================================================================
# 2. STACK (LIFO) - using a Python list for O(1) operations
# ============================================================================


class Stack:
    """LIFO Stack implementation. push/pop/peek all O(1) time."""

    def __init__(self) -> None:
        # Using a Python list under the hood; could replace with LinkedList
        self._items: list[object] = []

    def push(self, item: object) -> None:
        """Push an item onto the top of the stack. O(1) time."""
        self._items.append(item)

    def pop(self) -> object:
        """Remove and return the top item. O(1) time.
        Raises IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> object:
        """Return the top item without removing it. O(1) time.
        Raises IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check whether the stack contains any items. O(1) time."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the stack. O(1) time."""
        return len(self._items)

    def __len__(self) -> int:
        return self.size()


# ============================================================================
# 3. QUEUE (FIFO) - using collections.deque for O(1) enqueue/dequeue
# ============================================================================


from collections import deque


class Queue:
    """FIFO Queue implementation. enqueue/dequeue both O(1) time."""

    def __init__(self) -> None:
        # deque provides fast appends and pops from both ends
        self._items: deque[object] = deque()

    def enqueue(self, item: object) -> None:
        """Add an item to the rear (right side). O(1) time."""
        self._items.append(item)

    def dequeue(self) -> object:
        """Remove and return the item from the front (left side).
        O(1) time. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self) -> object:
        """Return the front item without removing it. O(1) time."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Check whether the queue is empty. O(1) time."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the queue. O(1) time."""
        return len(self._items)

    def __len__(self) -> int:
        return self.size()


# ============================================================================
# 4. BINARY SEARCH on a sorted list
# ============================================================================


def binary_search_iterative(arr: list, target) -> int:
    """Binary search using a while loop. O(log n) time, O(1) space.
    Returns the index of target, or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # Target is in the right half
            left = mid + 1
        else:
            # Target is in the left half
            right = mid - 1
    return -1


def binary_search_recursive(arr: list, target, left: int = 0, right: int = None) -> int:
    """Binary search using recursion. O(log n) time, O(log n) space (call stack).
    Returns the index of target, or -1 if not found."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1  # Base case: range is empty
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# ============================================================================
# 5. SORT: Merge Sort (stable, O(n log n))
# ============================================================================


def merge_sort(arr: list) -> list:
    """Merge sort — divide and conquer. O(n log n) time, O(n) space.
    Returns a new sorted list; the original list is unchanged."""
    if len(arr) <= 1:
        return arr[:]  # Base case: already sorted

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return _merge(left_half, right_half)


def _merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list. O(n) time, O(n) space."""
    merged: list = []
    i = j = 0
    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements from either list
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# In-place merge sort variant (uses auxiliary array, O(log n) stack space)
def merge_sort_inplace(arr: list, temp: list | None = None, left: int = 0, right: int = None) -> None:
    """Sort the list in place using merge sort. O(n log n) time, O(log n) space."""
    if right is None:
        right = len(arr) - 1
    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, temp, left, mid)
        merge_sort_inplace(arr, temp, mid + 1, right)
        _merge_inplace(arr, left, mid, right)


def _merge_inplace(arr: list, left: int, mid: int, right: int) -> None:
    """In-place merge step. O(n) time, O(1) extra space (uses temp array)."""
    if temp is None:
        temp = [0] * len(arr)
    # Copy both halves into the temporary array
    for i in range(left, right + 1):
        temp[i] = arr[i]

    i = left       # Start of left half
    j = mid + 1    # Start of right half
    for k in range(left, right + 1):
        # If left half is exhausted, take from right
        if i > mid:
            arr[k] = temp[j]
            j += 1
        # If right half is exhausted, take from left
        elif j > right:
            arr[k] = temp[i]
            i += 1
        # Compare and take the smaller element
        elif temp[j] < temp[i]:
            arr[k] = temp[j]
            j += 1
        else:
            arr[k] = temp[i]
            i += 1


# ============================================================================
# 6. RECURSIVE PROBLEMS
# ============================================================================


def factorial(n: int) -> int:
    """Compute n! (factorial) recursively. O(n) time, O(n) space (call stack).
    Base case: 0! = 1! = 1."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n × (n-1)!
    return n * factorial(n - 1)


def factorial_iterative(n: int) -> int:
    """Compute n! iteratively. O(n) time, O(1) space."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Compute the nth Fibonacci number recursively.
    Naive version: O(2^n) time, O(n) space (call stack)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n: int, memo: dict | None = None) -> int:
    """Fibonacci with memoization. O(n) time, O(n) space.
    Stores previously computed values to avoid redundant calls."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


