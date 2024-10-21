# JS225 Study Group Idea + Questions

Course: JS225
Last Edited: June 6, 2022 3:56 PM

Suggestion: At the beginning of the lesson, have a student use one of the object creation patterns to create "student" objects. Each object should have a name property and access to a function that generates a number between 1-44.

Students each create an instance of themselves, then take turns generating their random number. They have to answer the number of the question they receive, (with examples if applicable).

Note: If the group is a mixture of JS120 students, there's a separate set of questions that corresponds closer to their material in the JS120 section.

1. What is an object factory? Give an example of one.
2. What are some of the disadvantages of an object factory?
3. What is `this`?
4. What is execution context?
5. What is strict mode, and how does it change how a program runs? 
6. What are the benefits to using strict mode? When should you use it?
7. What is implicit function execution context?
8. What is explicit function execution context?
9. How can we change a function's execution context at execution time?
10. What do `call()` and `apply()` do, and how are they different? Give an example of using each.
11. What is the global object, and how can we access it?
12. What is the `bind()` method, and how does it differ from `call()` an `apply()`?
13. Bind pp
14. What do we mean when we say a function can "lose it's context"? What are two ways a function can experience context loss? 
15. Context loss pp
16. Context loss pp
17. What is a closure? What are the benefits of closures, and how can we create one?
18. How can we use closures to create private data? Demonstrate how we can make a variable, `secretNumber` private, using a closure. Why should we use closures to make data private?
19. What is garbage collection? Which values in JS participate in GC? Why do we need to be aware of garbage collection, as software engineers?
20. In the following code, how can we retain access to the value `"Steve"`? When can JS garbage collect `"Steve"`? 

```jsx
function makeHello(name) {
  return function() {
    console.log("Hello, " + name + "!");
  };
}

let helloSteve = makeHello("Steve");
```

- Notes
    - After the code runs, `helloSteve` references a function that closed over the local variable `name`, which right now contains the string `"Steve"`. Since the closure must keep `name` around, the reference to `"Steve"` must also stick around, which means JS can't GC `"Steve"`. When we call `helloSteve` sometime later, it still has access to `name` and can log its value.
    
    ```jsx
    helloSteve();  // => Hello, Steve!
    ```
    
    - Before JS can garbage collect `"Steve"`, you must ensure nothing else in the program references `"Steve"`; that includes every closure that has access to the `"Steve"` string. That's not typically a concern, but if you find that you must remove a closure or other reference explicitly, you can assign `null` to the item that references it. For instance:
    
    ```jsx
    helloSteve = null;
    ```
    
    - That dereferences the closure shown above, which in turn dereferences `"Steve"` through the `name` variable. If nothing else now has a reference to `"Steve"`, JS is free to garbage collect it.
    - If we modify the code above by introducing a variable prior to returning the anonymous function, the code returns an anonymous function that closes over both the `name` *and* `message` variables. Those variables, in turn, reference the strings `"Steve"` and `"Hello, Steve!"` respectively.
    
    ```jsx
    function makeHello(name) {
      let message = "Hello, " + name + "!";
      return function() {
        console.log(message);
      };
    }
    
    let helloSteve = makeHello("Steve");
    ```
    
    - Theoretically, this will prevent garbage collection on both strings. However, since `name` isn't referenced within the `helloSteve` function, depending on the browser, `"Steve"` might or might not be garbage collected.

21. What is an IIFE? Give an example. Why would we use an IIFE in code?

22. How can you call an IIFE with an argument? 

23. How can you use an IIFE to create a private scope? What problems does this solve?

24. What is a first-class function? Give an example.

25. What concept(s) does the following code demonstrate? How does this work?

```jsx
function multiply(first, second) {
  return first * second;
}

function makeMultiplyN(multiplicand) {
  return function(number) {
    return multiply(multiplicand, number);
  }
}
```

26. What is partial function application, and what are the benefits of using it?

27. Create a reusable function using partial function application.

28. What is the difference between a constructor function and a regular function?

29. What does the `new` operator do?

30. What does the following code log to the console? Note: Remember we're running it in coderpad.

```jsx
let a = 1;
let foo;
let obj;

function Foo() {
  this.a = 2;
  this.bar = function() {
    console.log(this.a);
  };
  this.bar();
}

foo = new Foo();

foo.bar();
Foo();

obj = {};
Foo.call(obj);
obj.bar();

console.log(this.a);
```

31. What will the following code log and why?

```jsx
let ninja;
function Ninja() {
  this.swung = true;
}

ninja = new Ninja();

Ninja.prototype.swingSword = function() {
  return this.swung;
};

console.log(ninja.swingSword());
```

- Answer
    - True: Even though the swingSword method is defined on the prototype after the ninja object is created, the prototype chain lookup happens when the swingSword method is called on the object, and it can be found.

32. Implement the method described in the comments:

```jsx
let ninjaA;
let ninjaB;
function Ninja() {
  this.swung = false;
}

ninjaA = new Ninja();
ninjaB = new Ninja();

// Add a swing method to the Ninja prototype which
// returns the calling object and modifies swung

console.log(ninjaA.swing().swung);      // must log true
console.log(ninjaB.swing().swung);      // must log true
```

- Answer
    
    ```jsx
    let ninjaA;
    let ninjaB;
    function Ninja(){
      this.swung = false;
    }
    
    ninjaA = new Ninja();
    ninjaB = new Ninja();
    
    Ninja.prototype.swing = function() {
      this.swung = true;
      return this;
    };
    
    console.log(ninjaA.swing().swung);
    console.log(ninjaB.swing().swung);
    ```
    

33. What does `Object.create` do, and how is it used?

34. What is the `function.prototype`? 

35. What is behavior delegation? How does JS implement inheritance differently than Ruby?

36. What is OLOO? Give an example. What are the benefits to organizing your code this way?

37. What is the Pseudo-Classical Pattern? Give an example. What are the benefits to organizing your code this way?

38. What are some things we need to consider when designing our code? 

39. What's the difference between using OLOO/ the Pseudo-Classical Pattern and using factory functions? 

40. How does ES6 `class` syntax work? Give an example.

41. How does inheritance work with `class` syntax?

42. Write a constructor function. 

43. What is the prototype chain?

44. What is the `.constructor` property?