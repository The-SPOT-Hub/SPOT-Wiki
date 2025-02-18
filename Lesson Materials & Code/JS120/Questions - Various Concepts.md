1. **What is** **Object Oriented Programming in context of JavaScript?**
2. **Is JavaScript object oriented? Why or why not?**
3. What are the advantages of OOP?
4. What are the disadvantages of OOP? 
5. What is encapsulation in context of OOP? Present an example that illustrates this concept.
6. In JavaScript, how does encapsulation differ from encapsulation in most other OO languages?
7. What is inheritance in context of JS?
8. What makes JavaScript different from other OOP languages?
9. What is **prototypal inheritance**? Present an example that illustrates this concept.
10. What is the role of `[[Prototype]]` property?
11. Let say we want to have a `dog` object. We want `dog` to be able to have access to method `makeSound()` (`makeSound(){console.log('sound')}`), but we don't want to declare it on `dog`. How many ways do you know that can make it possible?
    
    Use this to test your code:
    
    ```
    dog.makeSound(); // sound
    dog.hasOwnProperty('makeSound'); //false
    
    ```
    
12. What is a difference between `Object.create()` and `Object.assign()` methods? Use examples to present differences.
13. What is `setPrototypeOf()` method and what does it do? Give an example.
14. Compare prototypal inheritance with pseudo-classical inheritance. What are the similarities and differences? Are those concept relates or not?
15. What is the difference between single and multiple inheritance?
16. How is JavaScript dealing with the lack of multiple inheritance? Give an example.
17. What is polymorphism and what are its benefits?
18. There are two types of polymorphism in JS. What are they? Choose one of them and explain how it works on an example.
19. We say that any data type can be a collaborator even a primitive value. Can you give an example of a string as a collaborator?
20. What is a mixin? What would we use it for?
21. When should we use mixins and when inheritance?
22. What is the difference between Member access notation and Computed member access notation?
23. In JS there are some confusions about prototypes and many terms that sound or look similar. Explain shortly what the following concepts relate to:
    - prototype
    - .prototype property
    - `[[Prototype]]` property
    - `__proto__`
    - Object prototype
    - Function prototype
24. How does delegation work in JS?
25. What is a prototype chain?
26. What is a bare object? How to create one?
27. What is the global object? How can we print its value?
28. What is Execution Context?
29. What is implicit execution context?
30. What is explicit execution context and how can we set it?
31. What is `this` keyword?
32. Why is the context lost in this situation? Fix it.
    
    ```
    let shirt = {
      a : 'Hello',
      b : 'World',
      foo : function () {
        console.log(this.a + this.b)
      }
    }
    
    shirt.foo(); //'Hello World'
    let someVar = shirt.foo;  
    someVar(); // ?
    
    ```
    
33. Why is the context lost in the following situation? Fix it.
    
    ```
    function printHello(func) {
      func();
    }
    
    let shirt = {
      a : 'Hello',
      b : 'World',
      foo : function (){
        printHello(function() {
          console.log(this.a + this.b)
          })
      }
    }
    
    shirt.foo();
    
    ```
    
34. What does `new` keyword do?
35. Do we always have to use `new` keyword with constructors? Why or why not?
36. Describe the following object creation pattern and give an example: F**actory function / object factories**
37. Describe the following object creation pattern and give an example: **Constructors / Object constructors**
38. Describe the following object creation pattern and give an example: **Constructors with prototypes (Pseudo-classical pattern)**
39. Describe the following object creation pattern and give an example: **OLOO (Objects Linking to Other Objects.)**
40. Describe following object creation pattern and give an example: **ES6** **classes**
41. What is `super()` keyowrd? What is it used for?
42. What are build-in constructors?
43. Are strings primitives or objects in JavaScript?
44. What are scope safe constructors? Create one.