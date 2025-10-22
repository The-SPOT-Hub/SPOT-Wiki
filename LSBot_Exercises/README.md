# SPOT Wiki Exercise Formatting & Contribution Guide

This document defines the standard format for all course exercise Markdown files and provides comprehensive guidelines for contributing to the SPOT Wiki.

## Quick Navigation

- [Exercise Template](#exercise-template) - Copy this format for new exercises
- [Template Components](#template-components) - What each part does
- [Complete Example](#complete-example) - See it in action
- [How to Contribute](#how-to-contribute) - Adding exercises to the wiki

## Exercise Formatting

### Exercise Naming

Exercises should be numbered markdown files. Single digits should be padded with a zero (e.g., `02.md`) for better sorting.

### Exercise Template

When adding new exercises, please use the following template:

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

### Template Components

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

### Complete Example

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

## How to Contribute

### GitHub Workflow

1. **Fork the Repository**: Click "Fork" on the SPOT-Wiki GitHub page
2. **Clone Your Fork**: `git clone https://github.com/YOUR-USERNAME/SPOT-Wiki.git`
3. **Create a Branch**: `git checkout -b add-js101-exercise-15`
4. **Make Your Changes**: Add or edit exercise files
5. **Commit Changes**: `git add .` then `git commit -m "Add JS101 exercise 15"`
6. **Push to Your Fork**: `git push origin add-js101-exercise-15`
7. **Create Pull Request**: Go to your fork on GitHub and click "New Pull Request"

### Adding New Exercises

1. **Choose the Right Location**: Navigate to the appropriate course folder (e.g., `LSBot_Exercises/Javascript/JS101/`)
2. **Follow Naming**: Use numbered files with zero-padding (`01.md`, `02.md`, `15.md`)
3. **Use the Template**: Copy the format above
4. **Test Your Exercise**: Make sure it works as intended

### Quality Checklist

Before submitting, verify:
- Problem description is clear
- Examples show expected behavior  
- Solution is correct if present
- Navigation links work
- File follows the template
