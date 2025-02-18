### Description

This code demonstrates that a function definition creates an enclosure around all variables that are within the lexical scope within which that function has been defined. 

On line 4, home references the variable at the top level called home. When the `goHome()` function is invoked on line 8, within the body of the `travel()` function, home still references what was in scope at the point in code where `goHome()` is defined, rather than the variable home that's local within the `travel()` function body.

### Code

```jsx
let home = "Denver";

function goHome() {
  console.log(`I made it home, to ${home}!`);
}

function travel() {
  let home = "my hotel";
  goHome();
}

travel();
```