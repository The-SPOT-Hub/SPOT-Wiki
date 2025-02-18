# JS130 Questions

Not all these topics will be in the exam but most will be. I wrote these questions to help me prepare for the exam and I haven't taken the written yet, I hope none coincide with any exam questions. I've taken these directly from the course material to help me prepare.

- What is a closure?
- What is in a closure?
- When is a closure created?
- What is the relationship between closures and scope?
- What do we mean when we say that closures are defined lexically?
- What is partial function application?
- What is the order of the closure scope chain?
- Write some code that uses closure to create private data
- Explain why private data is desirable.
- Be able to identify code that gives users of your code a way to alter private data.
- What are IIFEs?
- How do you use IIFEs?
- How do you use IIFEs to create private scopes?
- How do you use blocks to create private scopes?
- How do you use IIFEs to create private data?
- How does `var` differ from `let` and `const`?
- What do we mean by declared scope, visibility scope, and lexical scope?
- What do we mean by global scope and local scope?
- What do we mean by inner scope and outer scope?
- What do we mean by function scope and block scope when talking about declared scope?
- What do we mean by function scope and block scope when talking about visibility scope?
- What is hoisting?
- How do `var`, `let`, and `const` interact with hoisting? How do they differ?
- How do functions and classes interact with hoisting? How do they differ?
- What part does hoisting play in the way a specific program works?
- How does hoisting really work?
- What is the temporal dead zone?
- What is strict mode? How does it differ from sloppy mode?
- How do you enable strict mode at the global or function level?
- Describe how code behaves under both strict and sloppy mode.
- When is strict mode enabled automatically?
- When should you use (or not use) strict mode?
- What are concise property initializers?
- What are concise methods?
- What is object/array destructuring?
- What is spread/rest syntax?
- What are the benefits of using modules?
- How do you use and create CommonJS modules?
- How do CommonJS modules pass exported items to the importing module?
- What are ES6 modules?
- What are the differences between CommonJS and ES6 modules?
- What is the CommonJS variable `module`?
- What are exceptions?
- Given an exception error message, identify the exception type and understand the meaning.
- What are the terms raise, throw, re-throw, and catch?
- What is the syntax for the `throw` and `try/catch` statements?
- What is the program flow for an exception?
- How do you throw an exception?
- What data types can be thrown as an exception?
- What Happens When A Program Throws An Exception?
- When should you use exceptions?
- What 5 side effects can a function have?
- What is a pure function?
- What commands you you need to run to install and set up jest?
- What are the main jest functions?
- What is SEAT?
- What are some common jest matchers?
- Explain `expect` and matchers (`toBe` and `toEqual` especially)
- What does code coverage refer to?
- What do branches refer to when talking about JEST testing?
- What is npm?
- What is npx and when do we use it?
- What is the `package.json` file and how do you initialize one?
- What is Babel and what does it do?
- What is transpilation and what are its advantages?
- What are packages?
- What is the `package.lock.json` file?
- What does the `--save` flag do?
- Where are a programs dependencies stored?
- Should node modules be stored in git? How about package.json?
- What is the difference between local and global modules?
- What's the difference between `dependencies` vs `devDependencies`?
- How can you remove a dependency from `package.json`?
- Where are npm scripts defined and why are they useful?
- What is the difference between synchronus and asynchronus?
- What is `setTimeout` and how do you use it?
- What is `setInterval` and how do you use it?
- What are promises?
- What do the `async` and `await` keywords do?
- What is the event loop?

# Practice code problems

## Partial function applications

### Is this a partial function application?

```jsx
function multiplyBySeven(number) {
  return multiply(7, number);
}

multiplyBySeven(3);
```

### Is this a partial function application?

```jsx
multiply(2, multiply(7, 3));
```

### Is this a partial function application?

```jsx
function makeMultiplier(factor) {
  return function(otherFactor) {
    return multiply(factor, otherFactor);
  };
}

const multiplyBySeven = makeMultiplier(7);
multiplyBySeven(3);
```

### Is this a partial function application?

```jsx
function makeMultiplier() {
  return function(factor) {
    return multiply(7, factor);
  };
}

const multiplyBySeven = makeMultiplier();
multiplyBySeven(3);
```

### Is this a partial function application?

```jsx
function makeLogger(identifier) {
  return function(msg) {
    console.log(identifier + ' ' + msg);
  };
}
```

### Is this a partial function application?

```jsx
function makeLogger(identifier) {
  return function(msg) {
    console.log(identifier, msg);
  };
}
```

### Is this a partial function application?

```jsx
function logIt(first, middle, last) {
  console.log(`${last}, ${first} ${middle}`);
}

function fullNameMaker(last) {
  return function(first) {
    logIt(first, 'Luther', last);
  };
}
```

### Is this a partial function application?

```jsx
function calc(x, y, z) {
  return x + y * z;
}

function foo(x) {
  return function bar(y, z) {
    return calc(x, y, z);
  }
}

let plus3 = foo(3);
let plus5 = foo(5);

plus3(5, 7);    // 38
plus5(2, 8);    // 21
```

### Is this a partial function application?

```jsx
function add(first, second) {
  return first + second;
}

function makeAdder(firstNumber) {
  return function(secondNumber) {
    return add(firstNumber, secondNumber);
  };
}

let addFive = makeAdder(5);
let addTen = makeAdder(10);

console.log(addFive(3));  // 8
console.log(addFive(55)); // 60
console.log(addTen(3));   // 13
console.log(addTen(55));  // 65
```

## Hoisting

### What specifically will happen in each of the following code blocks? Refer to the creation phase and the execution phase.

```jsx
bar();             // logs "world"
var bar = 'hello';

function bar() {
  console.log('world');
}
```

```jsx
var bar = 'hello';
bar();             // raises "TypeError: bar is not a function"

function bar() {
  console.log('world');
}
```

```jsx
bar();              // logs undefined
var foo = 'hello';

function bar() {
  console.log(foo);
}
```

```jsx
let foo = "hello";

function foo() {
  console.log("hello");
}
```

```jsx
function foo() {
  if (true) {
    function bar() {
      console.log("bar");
    }
  } else {
    function qux() {
      console.log("qux");
    }
  }

  console.log(bar);
  bar();

  console.log(qux);
  qux();
}
foo();
```

- Answer for previous code block
    
    While JavaScript functions have function scope, the specific hoisting behavior you'll see when you nest a function inside a block (such as an `if` statement) is inconsistent. ES6 standardized how such functions are treated, but it can still vary from depending on how your program is written. Before ES6, the behavior wasn't just inconsistent, it was undefined entirely. Creators of JavaScript engines were free to do whatever they wanted to do.
    
    What do you think happens here? Take a moment to think about it.
    
    Depending on several factors, any of the following results may occur:
    
    ```jsx
    [Function: bar]
    bar
    undefined
    TypeError: qux is not a function
    
    ```
    
    ```jsx
    [Function: bar]
    bar
    [Function: qux]
    qux
    
    ```
    
    ```jsx
    undefined
    TypeError: bar is not a function
    
    ```
    
    ```jsx
    ReferenceError: bar is not defined
    
    ```
    
    You may even get a syntax error with some implementations.
    
    Since you can get different behaviors with the same code, you shouldn't try to nest function declarations inside non-function blocks. If you must nest a function inside a block, use a function expression.
    

### Without running this code, what will it display? Explain your reasoning.

```jsx
var foo = function() {
  console.log("Bye");
};

function foo() {
  console.log("Hello");
}

foo();
```

### Without running this code, what does it print?

```jsx
for (var index = 0; index < 2; index += 1) {
  console.log(foo);
  if (index === 0) {
    var foo = "Hello";
  } else {
    foo = "Bye";
  }
}

console.log(foo);
console.log(index);
```

### Without changing the order of the invocation and function definition, update this code so that it works.

```jsx
bar();

var bar = function() {
  console.log("foo!");
};
```

### Without running the following code, determine what it logs to the console:

```jsx
var bar = 82;
function foo() {
  var bar = bar - 42;
  console.log(bar);
}

foo();
```

### Without running this code to determine your answer, what would this code output if you did run it?

```jsx
var foo = 10;

function bar() {
  if (foo > 20) {
    var foo = 50;
  }

  console.log(foo);
  foo += 10;
}

bar();
bar();
bar();
```

### The following code has console.log calls on lines 1, 4, 8, 10, and 16. In what sequence will those 5 log calls execute?

```jsx
console.log(foo());

function foo() {
  console.log('Waiting for bar!');
}

function foo() {
  console.log(foo);
  function bar() {
    console.log('bar again');
  }

  bar();

  function bar() {
    console.log('bar again and again');
  }
}
```

## Side effects

### What side effects are present in the `foo` function in the following code?

```jsx
const bar = 42;
let qux = [1, 2, 3];
let baz = 3;

function foo(arr) {
  let value = arr.pop();
  console.log(`popped ${value} from the array`);
  return value + bar + baz;
}

foo(qux);
```

### Does this code have side effects?

```jsx
let letters = ['a', 'b', 'c'];
function removeLast() {
  letters.pop(); 
}
```

### Does this code have side effects?

```jsx
function foo(array, callback) {
  for (let index = 0; index < array.length; index += 1) {
    callback(array[index]);
  }
}

foo([1, 2, 3], value => console.log(value));
```

### Does this code have side effects?

```jsx
function getHourOfDay() {
  let date = new Date();   // returns object with current date and time
  return date.getHours();
}

let hourOfDay = getHourOfDay();
```

### Does this code have side effects?

```jsx
let foo = ["bar", "qux"];

function getFoo() {
  return foo;
}

let newFoo = getFoo();
```

### Does this code have side effects?

```jsx
function getBoo(number) {
  return number + Math.random();
}

let boo = getBoo(5);
```

### Which of the following functions are pure functions?

```jsx
function sum(a, b) {
  console.log(a + b);
  return a + b;
}
```

```jsx
function sum(a, b) {
  a + b;
}
```

```jsx
function sum(a, b) {
  return a + b;
}
```

```jsx
function sum(a, b) {
  return a + b + Math.random();
}
```

```jsx
function sum(a, b) {
  return 3.1415;
}
```

## Closures

### What is happening in the following code example?

```jsx
function foo() {
  let name = "Pete";
  return function() {
    console.log(name);
  };
}

let printPete = foo();
printPete(); // Pete
```

### What is happening in the following code example?

```jsx
function makeCounter() {
  let counter = 0;

  return function() {
    counter += 1;
    return counter;
  }
}

let incrementCounter = makeCounter();
console.log(incrementCounter()); // 1
console.log(incrementCounter()); // 2
```

### What do the 4 console.log statements at the end of this program print? Try to answer without running the code:

```jsx
let counter = 0;

function makeCounter() {
  return function() {
    counter += 1;
    return counter;
  }
}

let incrementCounter = makeCounter();
console.log(incrementCounter());
console.log(incrementCounter());

incrementCounter = makeCounter();
console.log(incrementCounter());
console.log(incrementCounter());
```

### What do the 4 console.log statements at the end of this program print? Try to answer without running the code:

```jsx
function makeCounter() {
  return function() {
    let counter = 0;
    counter += 1;
    return counter;
  }
}

let incrementCounter = makeCounter();
console.log(incrementCounter());
console.log(incrementCounter());

incrementCounter = makeCounter();
console.log(incrementCounter());
console.log(incrementCounter());
```

### What do the 4 console.log statements at the end of this program print? Try to answer without running the code:

```jsx
function makeCounter() {
  let counter = 0;

  return function() {
    counter += 1;
    return counter;
  }
}

let incrementCounter = makeCounter();
console.log(incrementCounter());
console.log(incrementCounter());

incrementCounter = makeCounter();
console.log(incrementCounter());
console.log(incrementCounter());
```

### What do the 4 console.log statements at the end of this program print? Try to answer without running the code:

```jsx
function makeCounter() {
  let counter = 0;

  return function() {
    counter += 1;
    return counter;
  }
}

let incrementCounter1 = makeCounter();
let incrementCounter2 = makeCounter();

console.log(incrementCounter1());
console.log(incrementCounter1());

console.log(incrementCounter2());
console.log(incrementCounter2());
```

### Without running the following code, determine what value it logs on the last line. Explain how the program arrived at that final result.

```jsx
function foo(start) {
  let prod = start;
  return function (factor) {
    prod *= factor;
    return prod;
  };
}

let bar = foo(2);
let result = bar(3);
result += bar(4);
result += bar(5);
console.log(result);
```

### What concepts does the following code block demonstrate?

```jsx
function makeList() {
  let items = [];

  return {

    add: function(item) {
      let index = items.indexOf(item);
      if (index === -1) {
        items.push(item);
        console.log(item + " added!");
      }
    },

    list: function() {
      if (items.length === 0) {
        console.log("The list is empty.");
      } else {
        items.forEach(function(item) {
          console.log(item);
        });
      }
    },

    remove: function(item) {
      let index = items.indexOf(item);
      if (index !== -1) {
        items.splice(index, 1);
        console.log(item + " removed!");
      }
    },
  };
}
```

### Without running this code, determine what value gets logged to the console.

```jsx
function foo(initialValue) {
  let total = initialValue;
  return function (adjustmentValue) {
    total += adjustmentValue;
    return total;
  };
}

let bar = foo(10);
let result = bar(-2);
result += bar(5);
result += bar(3);
result += bar(-4);
console.log(result);
```

## IIFEs

### What is happening in this code block?

```jsx
let foo = (function() {
  return (function() {
    return 10;
  })() + 5;
})();

console.log(foo);       // => 15
```

### What concepts are demonstrated in this code?

```jsx
((first, second) => first * second)(5, 6); // => 30
```

### Explain what's happening in this code:

```jsx
const makeUniqueId = (function() {
  let count = 0;
  return function() {
    ++count;
    return count;
  };
})();

makeUniqueId(); // => 1
makeUniqueId(); // => 2
makeUniqueId(); // => 3
```

### Will the following code execute without error? Try to answer without running it.

```jsx
function() {
  console.log("Sometimes, syntax isn't intuitive!");
}();
```

### Why does this code produce an error? Correct the problem by using an IIFE.

```jsx
var sum = 0;
sum += 10;
sum += 31;

let numbers = [1, 7, -3, 3];

function sum(arr) {
  return arr.reduce((sum, number) => {
    sum += number;
    return sum;
  }, 0);
}

sum += sum(numbers);  // ?
```

### Is the named function inside in this IIFE accessible in the global scope?

```jsx
(function foo() {
  console.log('Bar');
})();

foo() // ?
```

### Rewrite this code using an IIFE. Your solution should no longer need the name foo.

```jsx
function foo(start) {
  let prod = start;
  return function (factor) {
    prod *= factor;
    return prod;
  };
}

let bar = foo(2);
let result = bar(3);
result += bar(4);
result += bar(5);
console.log(result);
```

## Exceptions

### Explain what's happening in the following code block:

```jsx
function div(first, second) {
  if (second === 0) {
    throw new Error("Divide by zero!");
  }

  return first / second;
}

let result = div(1, 0); // Error: Divide by zero!
console.log(result);    // not run
```

### Explain what's happening in the following code block:

```jsx
class DivideByZeroError extends Error {}

function div(first, second) {
  if (second === 0) {
    throw new DivideByZeroError("Divide by zero!");
  }

  return first / second;
}

function divideOneBy(divisor) {
  try {
    let result = div(1, divisor);
    console.log(result);
  } catch (error) {
    if (error instanceof DivideByZeroError) {
      console.log(`${error.message} ignored`);
    } else {
      throw error;
    }
  }
}

divideOneBy(1); // 1
divideOneBy(0); // Divide by zero! ignored
```

### Is this a valid IIFE?

```jsx
let sum = (function() {
  return left + right;
});
```

### Is this a valid IIFE?

```jsx
let sum = (function() {
  return left + right;
});

sum();
```

### Is this a valid IIFE?

```jsx
(function() {
  return left + right;
}());
```

## Asynchronus

### In what order do the following lines of code run?

```jsx
setTimeout(function() {        
  console.log('!');            
}, 3000);

setTimeout(function() {        
  console.log('World');        
}, 1000);

console.log('Hello');          
```

### What is logged to the console and in what order?

```jsx
setTimeout(function() {
  console.log('!');
}, 0);

setTimeout(function() {
  console.log('World');
}, 0);

console.log('Hello');
```

### In what sequence will the JavaScript runtime run the following lines of code?

```jsx
setTimeout(function() {   //
  console.log('Once');    //
}, 1000);

setTimeout(function() {   //
  console.log('upon');    //
}, 3000);

setTimeout(function() {   //
  console.log('a');       //
}, 2000);

setTimeout(function() {   //
  console.log('time');    //
}, 4000);
```

### In what sequence does the JavaScript runtime run the functions q(), d(), n(), z(), s(), f(), and g() in the following code?

```jsx
setTimeout(function() {
  setTimeout(function() {
    q(); 
  }, 15);

  d(); 

  setTimeout(function() {
    n(); 
  }, 5);

  z(); 
}, 10);

setTimeout(function() {
  s(); 
}, 20);

setTimeout(function() {
  f(); 
});

g(); 
```

1. Write a function named `startCounting` that logs a number to the console every second, starting with `1`. Each output number should be one greater than the previous one.
    
    
2. Extend the code from the previous problem with a `stopCounting` function that stops the logger when called.