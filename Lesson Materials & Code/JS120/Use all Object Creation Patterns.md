**Description**
Each student assigned of the patterns and must satisfy the test cases included by implementing that pattern.

Each pattern creates an instance object which has name & position properties and has access to a info method.

The goal is for the student to not only code the pattern but *also to explain its benefits and drawbacks verbally.*

**I ask the student to explain how their code works as well, making sure that their terminology is correct.

**Solutions (Code Template Below)**

```jsx
// /** 
//  * Use each of the below patterns to create instance objects
//  * which satisfy the following tests below each...
// */

/**======================== Factory Function ================================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *  player1 ==> Object.prototype ==> null
 *
 * 
 * Does this pattern conserve memory?
 *  No, each instance object contains its own definition for common methods (info)
 * 
 * 
 * What relationships (to other objects) can we determine from the instance?
 *  None.
 *  The prototype object for all instances created is Object.prototype.
 *  We can't know which function created the instance object because all
 *  objects created using object literal syntax reference the 'Object'
 *  constructor.
 *  
 */

function createPlayer(name, position) {
  return {
    name, 
    position,

    info() {
      return `${this.name} is a ${this.position} in the NBA`;
    }
  }
}

let player1 = createPlayer('Dennis', 'Forward');

console.log(player1.name === 'Dennis');
console.log(player1.position === 'Forward');
console.log(player1.info() === 'Dennis is a Forward in the NBA');

// Demonstration of prototype chain
console.log(player1.__proto__ === Object.prototype);
console.log(Object.prototype.__proto__ === null);

// Demonstration that memory isn't conserved
let newPlayer1 = createPlayer('Dennis', 'Forward');
console.log(newPlayer1.info === player1.info);

// Demonstration of instance object relationships
console.log(player1.__proto__ === Object.prototype);
console.log(player1.constructor.name);

/**=============== Objects-Linking to Other Objects (OLOO) ==================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *  player2 ==> playerPrototype ==> Object.prototype ==> null
 *
 * Does this pattern conserve memory?
 *  Yes, all instances of this pattern delegate calls to common methods to 
 *  the prototype (playerPrototype).
 *
 * What relationships (to other objects) can we determine from the instance?
 *  The prototype object (playerPrototype) can be determined, and, thereby,
 *  it can be determined which object defines the common methods.
 *  Because the object is defined using the Object.create() function, all
 *  instances created using this pattern reference the 'Object' constructor.
 */

let playerPrototype = {
  init(name, position) {
    this.name = name;
    this.position = position;
    return this;
  },

  info() {
    return `${this.name} is a ${this.position} in the NBA`;
  },

};

let player2 = Object.create(playerPrototype).init('Dennis', 'Forward');

console.log(player2.name === 'Dennis');
console.log(player2.position === 'Forward');
console.log(player2.info() === 'Dennis is a Forward in the NBA');

// Demonstration of prototype chain
console.log(player2.__proto__ === playerPrototype);
console.log(playerPrototype.__proto__ === Object.prototype);
console.log(Object.prototype.__proto__ === null);

// Demonstration that memory is conserved
let newPlayer2 = Object.create(playerPrototype).init('Dennis', 'Forward');
console.log(newPlayer2.info === player2.info);

// Demonstration of instance object relationships
console.log(player1.__proto__ === playerPrototype);
console.log(player1.constructor.name);

/**====================== Constructor (JS225) ===============================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *
 *
 * Does this pattern conserve memory?
 *
 * 
 * What relationships (to other objects) can we determine from the instance?
 *  
 */

// console.log(player3.name === 'Dennis');
// console.log(player3.position === 'Forward');
// console.log(player3.info() === 'Dennis is a Forward in the NBA');

/**============= Constructor & Prototype (Pseudo-Classical) =================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *  instance ==> Player.prototype ==> Object.prototype ==> null
 *
 * Does this pattern conserve memory?
 *  Yes, all instances of this pattern delegate calls to common methods to 
 *  the function prototype (Player.prototye).
 *
 * What relationships (to other objects) can we determine from the instance?
 *  The prototype object (Player.prototype) can be determined and, thereby,
 *  it can be determined which object defines the common methods.
 *  Because the object is created using the Player constructor function, it
 *  can be determined which function created the instance.
 */

function Player(name, position) {
  this.name = name;
  this.position = position;
}

Player.prototype.info = function info() {
  return `${this.name} is a ${this.position} in the NBA`;
}

let player4 = new Player('Dennis', 'Forward')

console.log(player4.name === 'Dennis');
console.log(player4.position === 'Forward');
console.log(player4.info() === 'Dennis is a Forward in the NBA');

// Demonstration of prototype chain
console.log(player4.__proto__ === Player.prototype);
console.log(Player.prototype.__proto__ === Object.prototype);
console.log(Object.prototype.__proto__ === null);

// Demonstration that memory is conserved
let newPlayer4 = new Player('Dennis', 'Forward')
console.log(newPlayer4.info === player4.info);

// Demonstration of instance object relationships
console.log(player4.__proto__ === Player.prototype);
console.log(player4.constructor.name);

/**==================== ES6 Class (Pseudo-Classical) ========================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *  instance ==> Player.prototype ==> Object.prototype ==> null
 *
 * Does this pattern conserve memory?
 *  Yes, all instances of this pattern delegate calls to common methods to 
 *  the function prototype (Player.prototye).
 *
 * What relationships (to other objects) can we determine from the instance?
 *  The prototype object (Player.prototype) can be determined and, thereby,
 *  it can be determined which object defines the common methods.
 *  Because the object is created using the Player constructor function, it
 *  can be determined which function created the instance.
 */

class Players {
  constructor(name, position) {
    this.name = name;
    this.position = position;
  }

  info() {
    return `${this.name} is a ${this.position} in the NBA`;
  }
}

let player5 = new Players('Dennis', 'Forward')

console.log(player5.name === 'Dennis');
console.log(player5.position === 'Forward');
console.log(player5.info() === 'Dennis is a Forward in the NBA');

// Demonstration of prototype chain
console.log(player5.__proto__ === Players.prototype);
console.log(Players.prototype.__proto__ === Object.prototype);
console.log(Object.prototype.__proto__ === null);

// Demonstration that memory is conserved
let newPlayer5 = new Players('Dennis', 'Forward')
console.log(newPlayer5.info === player5.info);

// Demonstration of instance object relationships
console.log(player5.__proto__ === Players.prototype);
console.log(player5.constructor.name);
```

This exercise is meant to consume the entire session.

Depending on time or number of students, I usually only pick two or three patterns instead of trying to attempt all.

**Code Template**

```javascript
/** 
 * Use each of the below patterns to create instance objects
 * which satisfy the following tests below each...
*/

/**======================== Factory Function ================================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *
 *
 * Does this pattern conserve memory?
 *
 * 
 * What relationships (to other objects) can we determine from the instance?
 *  
 */

console.log(player1.name === 'Dennis');
console.log(player1.position === 'Forward');
console.log(player1.info() === 'Dennis is a Forward in the NBA');

/**=============== Objects-Linking to Other Objects (OLOO) ==================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *
 *
 * Does this pattern conserve memory?
 *
 * What relationships (to other objects) can we determine from the instance?
 *  
 */

console.log(player2.name === 'Dennis');
console.log(player2.position === 'Forward');
console.log(player2.info() === 'Dennis is a Forward in the NBA');

/**====================== Constructor (JS225) ===============================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *
 *
 * Does this pattern conserve memory?
 *
 * What relationships (to other objects) can we determine from the instance?
 *  
 */

console.log(player3.name === 'Dennis');
console.log(player3.position === 'Forward');
console.log(player3.info() === 'Dennis is a Forward in the NBA');

/**============= Constructor & Prototype (Pseudo-Classical) =================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *
 *
 * Does this pattern conserve memory?
 *
 * What relationships (to other objects) can we determine from the instance?
 *  
 */

console.log(player4.name === 'Dennis');
console.log(player4.position === 'Forward');
console.log(player4.info() === 'Dennis is a Forward in the NBA');

/**==================== ES6 Class (Pseudo-Classical) ========================
 * ==========================================================================
 * (Write answers to all questions and demonstrate using instance properties)
 * 
 * Show the prototype chain for instances created with this pattern.
 *
 *
 * Does this pattern conserve memory?
 *
 * What relationships (to other objects) can we determine from the instance?
 *  
 */

console.log(player5.name === 'Dennis');
console.log(player5.position === 'Forward');
console.log(player5.info() === 'Dennis is a Forward in the NBA');
```