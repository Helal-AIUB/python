# Short Note: List and Tuple in Python

### 1. What is a List?

A **list** is an ordered and mutable (changeable) collection of items in Python. It is created using square brackets `[]`.

**Example:**

```python
fruits = ["Apple", "Banana", "Mango"]
```

### 2. What is a Tuple?

A **tuple** is an ordered but immutable (unchangeable) collection of items in Python. It is created using parentheses `()`.

**Example:**

```python
fruits = ("Apple", "Banana", "Mango")
```

### 3. Difference Between List and Tuple

| List                                     | Tuple                                   |
| ---------------------------------------- | --------------------------------------- |
| Uses `[]`                                | Uses `()`                               |
| Mutable (can be changed)                 | Immutable (cannot be changed)           |
| Items can be added, removed, or modified | Items cannot be modified after creation |

### 4. Five Useful List Methods

* `append()` – Adds an item to the end of the list.
* `insert()` – Inserts an item at a specified position.
* `remove()` – Removes a specified item.
* `pop()` – Removes and returns an item by index (or the last item).
* `sort()` – Sorts the list in ascending order.

**Example:**

```python
numbers = [3, 1, 2]
numbers.append(4)
numbers.sort()
print(numbers)   # Output: [1, 2, 3, 4]
```
