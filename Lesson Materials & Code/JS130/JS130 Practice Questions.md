- What does strict mode do?
- Describe hoisting for variables declared with `let` and `const`
- Describe how variables declared with `var` are hoisted.
- Describe how classes are hoisted
- Define closure. When are closures created?
- Define partial function application, and write an example of a partial function application
- What is a benefit of using IIFE's?
- Given this code containing ES6 shorthand, rewrite without any shorthand:
    
    ```jsx
    let student = {
      name: 'Jane Doe',
      age: 20,
      phone: 1112223333,
      email: 'jane@email.com'
    };
    
    let {name, email, age} = student;
    
    // Answer:
    // let name = student.name;
    // let email = student.email;
    // let age = student.age;
    ```
    
- What will this code log to the console?
    
    ```jsx
    let foo = [1, 2, 3];
    let bar = [4, 5, 6];
    let qux = [...foo, ...bar];
    console.log(qux);  
    // Answer: [1, 2, 3, 4, 5, 6]
    ```
    
- What is the difference between **spread** syntax and **rest** syntax?
- When should you and should you not **throw** exceptions?
- When would you use CommonJS/Node modules vs JS/ES/ECMA modules?
- Define what a **pure function** is
- Is this a pure function?

```jsx
function calcNum(num) {
	return 5 + num + Math.random();
}
// Answer: no
```

```jsx
let tax = 20;
function calculateTota(productPrice) {
   return productPrice * (tax / 100) + productPrice;
}
// Answer: no
```

```jsx
function calcTip(bill, percent) {
   return bill * percent / 100;
}
// Answer: yes
```

- Describe what happens when running the terminal command `npm install` in a project directory.
- Define **transpilation**
- In Jest, what is the difference between the `describe()` function, the `test()` function, and the `expect()` function?
- In Jest, what is the `beforeEach()` method and when would you use it?