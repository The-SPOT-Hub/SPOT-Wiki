# Check your understanding of how concurrancy (async) works in JS

Course: JS230
Concepts: Asynchronous
Last Edited: June 6, 2022 3:56 PM

### Description

What will the following program output?

It will output 'turtles!', then 'dragons!', because even though the callback given to `setTimeout` is added immediately to the event cue, the event loops adds callbacks to the stack to be executed only after the main stack frame is removed (the stack is empty).

### Code

```jsx
function wait(seconds) {
  let start = new Date()
  let secondsElapsted;
  do {
    let now = new Date()
    secondsElapsted = (now - start) / 1000
  } while(secondsElapsted <= seconds)
}

setTimeout(() => {
  console.log('dragons!')
}, 0)

wait(2)

console.log('turtles!');
```