# Short Note: Loops in Python

### 1. What is a Loop?

A loop is used to execute a block of code repeatedly until a condition is met.

### 2. Difference Between `for` Loop and `while` Loop

| For Loop                                     | While Loop                                     |
| -------------------------------------------- | ---------------------------------------------- |
| Used when the number of iterations is known. | Used when the number of iterations is unknown. |
| Iterates over a sequence.                    | Runs as long as a condition is true.           |

### 3. What is `range()`?

`range()` is a built-in function that generates a sequence of numbers, commonly used with loops.

**Example:**

```python
for i in range(5):
    print(i)
```

### 4. What is `break`?

The `break` statement immediately stops a loop and exits it.

**Example:**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### 5. What is `continue`?

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

**Example:**

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

### What I Learned

I learned how to use loops, the `range()` function, and the `break` and `continue` statements in Python.
