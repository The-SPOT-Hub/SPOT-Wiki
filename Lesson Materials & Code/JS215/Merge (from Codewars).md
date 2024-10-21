# Merge (from Codewars)

Course: JS215
Concepts: Objects
Last Edited: June 6, 2022 3:56 PM

// Write a function that takes two or more objects and returns
// a new object which combines all the input objects.

// Objects are combined
// together so that the values of matching keys are added together.

// An example:

const objA = { a: 10, b: 20, c: 30 }
const objB = { a: 3, c: 6, d: 3 }
combine(objA, objB) // Returns { a: 13, b: 20, c: 36, d: 3 }

// The combine function should not mutate the input objects.

```jsx
// Write a function that takes two or more objects and returns 
// a new object which combines all the input objects.

// Objects are combined together so that the values of matching keys are added together.

// An example:

const objA = { a: 10, b: 20, c: 30 }
const objB = { a: 3, c: 6, d: 3 }
combine(objA, objB) // Returns { a: 13, b: 20, c: 36, d: 3 }

// The combine function should not mutate the input objects.
```

Try to merge the objects manually, rather than using built-in methods. For bonus practice, what if the values are a different data type, like strings? Can you add versatility to your solution?