# array instance inheritance diagram

Course: JS225
Last Edited: June 6, 2022 3:56 PM

Here is an improved version of the example 4 diagram of the [100 minute video]([https://www.youtube.com/watch?v=-N9tBvlO9Bo&ab_channel=RyanSchaul](https://www.youtube.com/watch?v=-N9tBvlO9Bo&ab_channel=RyanSchaul)). The original diagram is shown around the 25 minute mark.

![improved_array_inheritance_diagram.JPG](improved_array_inheritance_diagram.jpg)

I also wrote some test code to validate this diagram:

```jsx
"use strict";

console.log(Object.prototype.hasOwnProperty('__proto__')); // true
console.log(Object.prototype.__proto__); // null
console.log(Array.prototype.hasOwnProperty('__proto__')); // false

let arr = ['a', 'b'];

console.log(arr.__proto__ === Array.prototype); // true
console.log(Array.prototype === Array.prototype.__proto__); // false
console.log(Object.prototype.constructor === Object); // true
console.log(arr.hasOwnProperty('__proto__')); // false
console.log(Object.getPrototypeOf(Array.prototype) === Object.prototype); // true
console.log(Object.hasOwnProperty('constructor')); // false

console.log(Function.prototype.hasOwnProperty('__proto__')); // false
console.log(Function.prototype.hasOwnProperty('constructor')); // true
console.log(Function.prototype.constructor === Function); // true
console.log(Object.getPrototypeOf(Function.prototype) === Object.prototype); // true
console.log(Object.getPrototypeOf(Array)); // {}
console.log(Array.constructor === Function); // true
// Where is the Array.constructor defined?
// The prototype of Array seems to be an empty object
// But it is not really an empty object.
console.log(Array.hasOwnProperty('constructor')); // false
console.log({}.constructor === Object); // true
console.log(Object.getPrototypeOf(Array).constructor === Function); // true

let ArrayPrototype = Object.getPrototypeOf(Array);
console.log(Object.getPrototypeOf(ArrayPrototype)  === Object.prototype); // true
console.log(ArrayPrototype.hasOwnProperty('constructor')); // true
console.log(ArrayPrototype.constructor === Function); // true

console.log(Object.constructor === Function); // true
console.log(Object.hasOwnProperty('constructor')); // false
console.log(Function.constructor === Function); // true
console.log(Function.hasOwnProperty('constructor')); // false

let FunctionPrototype = Object.getPrototypeOf(Function);
console.log(Object.getPrototypeOf(FunctionPrototype)  === Object.prototype); // true
console.log(FunctionPrototype.hasOwnProperty('constructor')); // true
console.log(FunctionPrototype.constructor === Function); // true
console.log(ArrayPrototype === FunctionPrototype); // true
let ObjectPrototype = Object.getPrototypeOf(Object);
console.log(ArrayPrototype === ObjectPrototype); // true

console.log(ArrayPrototype === Function.prototype); // true!!

// now I still want to find out how __proto__ works.
// It seems like it is only a property on Object.prototype but returns the [[Prototype]]
// of the current execution context.

console.log(Object.getPrototypeOf(Object.prototype)); // null
```