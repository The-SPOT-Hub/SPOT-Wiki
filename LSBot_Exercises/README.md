# Exercise Formatting

This document defines the standard format for all course exercise Markdown files for the SPOT Wiki. When adding new exercises, please use the following template:

```
# Course Label
## Problem N : description

Problem description/requirements

## Examples:

<details>
  <summary>Hints:</summary>
  Optional hints.
</details>

<details>
  <summary>Solution:</summary>
  Optional solution code or text.
</details>

---

[Previous](N-1.md) | [Next](N+1.md)
```

Many components are optional, here's a description of each:

1. **Course label (required):** This should be an H1. E.g., `# PY101` or `#LS250`. You should always reference the main course rather than the assessment course. It's assumed that exercises for the course are appropriate for the associated assessment.

2. **Problem N : Description (required):** Having an H2 with `Problem N` is required. E.g., `## Problem 42`. If you'd like to add a description, you may. E.g., `## Problem 42: Truthiness and Arrays`.

3. **Problem Description (required):** The actual exercise text. E.g., `Write a function that calculates the Nth fibonacci number recursively.`

4. **Examples (optional):** If there are test cases or expected behavior, it should go here under an H2: `## Examples:`

5. **Hints (optional)**: If an exercise includes hints, you can place them in this drop-down box. It should be formatted as such:

```md
<details>
  <summary>Hints:</summary>
  Think about how each Fibonacci number relates to the two before it.
</details>
```

6. **Solution (optional)**: Most exercises should have solutions, but sometimes they don't. If there is a solution, either code or text, place it in this collapse box:

````md
<details>
  <summary>Solution:</summary>
  ```python
  def fibonacci(n):
      if n <= 1:
          return n
      return fibonacci(n - 1) + fibonacci(n - 2)
   ```
</details>
````

> **Note:** For code blocks to render within `<details>` elements, you need to include a blank line before and after the code fences.


7. **Navigation Links (required)**: Links that go to the previous exercise if present and the next exercise, if present.

Here's a complete example for our Fibonacci example:

# PY130
## Problem 3 : Recursive Fibonacci

Write a function that calculates the Nth fibonacci number recursively.

## Examples:

```python
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(6))  # 8
```

<details>
  <summary>Hints:</summary>

  Think about how each Fibonacci number relates to the two before it.

</details>

<details>
  <summary>Solution:</summary>

  ```python
  def fibonacci(n):
      if n <= 1:
          return n
      return fibonacci(n - 1) + fibonacci(n - 2)
  ```

</details>

---

[Previous](N-1.md) | [Next](N+1.md)
