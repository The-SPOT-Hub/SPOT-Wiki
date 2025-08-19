# **Organize Pair Coding Challenges**

Pair Coding Challenges (PCC) are events organized by LS students who would like to lead a session like this once or numerous times. The aim of PCC is to provide a hands-on, mini-project experience that will be both fun and educative. On the contrary to other, regular SPOT sessions, PCC is not specified for any particular level. It's completely up to you, as an organizer to decide what is the minimum level required to participate. 

# Ideas

The topics may vary and are completely up to you as an organizer, but some ideas are:

- CodeWars challenges
- Simple games (either in a terminal or with UI)  (I.E. battleship,  snake, hangman etc.)
- **creating micro-libraries**
  <details>
  - **JS micro-library**
    - **description and examples:**
        
        **Task:** Building a micro, vanilla JS library
        **Groups:** 2-3 ppl
        
        We are going to build a string manipulation micro-library. 
        
        1. You will need to set up a node project on one of the student's machines:
        - remember about the correct file structure for your files
        - what files and folders should node project include? // lib test
        
        2. You will need to create three files:
        - library module: stringis.js
        - file main.js that will use the functions from the module. `main.js` should simply call the functions and console log the result. If any of the functions throws an error main.js should handle that error and log to console ‘invalid input’. 
        - stringis.test.js that checks if all your functions return what they should
        
        3. stringis.js needs to include the following functions and each function has to throw an error if the input is NOT a string:
        
        ```jsx
        caseSwitchis
        // change all the upper case characters to lower case characters and lowercase characters to uppercase characters. Leave all the other characters unchanged. 
        // ex. Abcd_xkLL? => aBCD_Xkll?
        
        alphaOrderis
        // sort all the characters in a string to be in an alphabetical order. Leaves all non alphabetical characters in the same place. Case insensitive. 
        // // ex. Hello, have a nice day!  => aaacd, eeeH h illn ovy!
        
        compresingis
        // takes a string and compress it. It changes all consecutive same characters into one and their cout
        // ex.  ‘Hello Woooorld’ => ‘Hel(2)o Wo(4)rld’
        
        gRamsayTranslateis
        // takes a string and translating it to Gordon Ramsay talk: change all characters to uppercase. End all the sentence with ‘!!!’. Add ‘YOU IDIOT SANDWICH’  after each ‘,’
        // ex. “This pizza is so disgusting, if you take it to Italy you’ll get arrested.”
        // => “THIS PIZZA IS SO DISGUSTING, YOU IDIOT SANDWICH,  IF YOU TAKE IT TO ITALY YOU’LL GET ARRESTED!!!”
        ```
        
        [Untitled](https://www.notion.so/b3f16a1a543b4ed19715e28280179603?pvs=21)
        
        [Untitled](https://www.notion.so/601b9d8e982045ef97ccb16ffb152245?pvs=21)
        
    - **bonus features:**
        - A bonus if you use regex at least once!
        - Bonus functions:
            - firstLetterSwichis 
            takes two strings and returns and array with two strings with switched first letters of each word.
                
                ```jsx
                
                // Ex: firstLetterSwichis(‘I like eating icecream’, ‘What a nice day!’)
                // => [‘W aike neating dcecream’, ‘Ihat l eice iay’];
                ```
                
            - vowelSwitchis
            Takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string.
            
            ```jsx
            // ex. 'this is my string' => 'th3s 6s my str15ng'
            ```
            
            - removisDuplicatis
            Removing all consecutive duplicate words from a string, leaving only first words entries.
    - **solutions (some):**
        
        ```jsx
        function alphaOrderis(givenString) {
          let cleaned = givenString.replace(/[^a-z]/gi, '')
          // return cleaned;
          
          let sorted = cleaned.split('').sort((a,b)=>{
            a = a.toLowerCase();
            b = b.toLowerCase();
            if(a < b){
              return -1;
            } else if(a > b){
              return 1;
            } else{
              return 0;
            }
          })
          
        
        givenString.split('').forEach((ogChar, idx) => {
          if (ogChar.match(/[^a-z]/gi)) {
            sorted.splice(idx, 0, ogChar)
          }
        })
          return sorted.join('');
        }
                              
        // console.log(alphaOrderis('Hello, have a nice day!')) // aaacd, eeeH h illn ovy!                 
        
        function caseSwitchis(string) {
          return string.split('').map(char => {
            if (char.match(/[a-z]/)) {
              return char.toUpperCase();
            } else if (char.match(/[A-Z]/)) {
              return char.toLowerCase();
            } else {
              return char;
            }
          }).join('')
          
        }
        
        // console.log(caseSwitchis('Abcd_xkLL?')); // aBCD_Xkll?
        
        module.exports = {alphaOrderis, caseSwitchis}
        ```
  </details>          
- simple application (I.E. calculator, food ordering app)
<details>
- **mini-programs**
  - **Personal Finance App**
      - **Description:**
          - You will be divided into two groups.
          - Your task for today is to cooperate in order to create a plan for a mini Personal Finance App.
          - A big plus is if your team will be able to make the app working.
          - Your app can work in node or browser. It’s entirely up to you.
          - You have to use at least one of the object creation patterns but you cannot use classes.
          - Your team has to decide what functionalities are needed and how will organize yourself.
          - You have time until 12:50 pm (or 45 min) EST so plan your time wisely :)
          - In the end of the session we will present and discuss:
              - present how far did your team go
              - what functionalities does your app have
              - if you got the app working present how it works
              - what was the most challenging part
              - what went well
              
      - The s**olution from previous groups:**
          
          ```jsx
          //Programs that we have created: 
          
          //First group: Leena and Daniel
          
          // function FinanceApp(initalBalance = 0, ) {
          //   this.balance = initalBalance;
          //   this.expenses = [];
          //   this.income = [];
          // }
          
          // FinanceApp.prototype = {
          //   getBalance() {
          //     return this.balance;
          //   },
          //   getIncome() {
          //     return this.income.map(current => current.toString());
          //   },
          //   getExpenses() {
          //     return this.expenses.map(current => current.toString());
          //   },
          //   addExpense(value = 0, category = 'Generic', date = 'today') {
          //     this.expenses.push(new Record(value, category, date));
          //     this.balance -= value;
          //   },
          //   addIncome(value = 0, category = 'Generic', date = 'today') {
          //     this.balance += value;
          //     this.income.push(new Record(value, category, date));
          //   }
          // }
          
          // function Record (value, category, date) {
          //   this.value = value;
          //   this.category = category;
          //   this.date = date;
          // }
          
          // Record.prototype.toString = function() {
          //   return `value: ${this.value} - category: ${this.category} - date: ${this.date}`;
          // }
          
          // let danielFinanceApp = new FinanceApp(0);
          // console.log(danielFinanceApp.addExpense(40, 'gas'));
          // console.log(danielFinanceApp.addExpense(130, 'costoc'));
          
          // console.log(danielFinanceApp.getIncome());
          // console.log(danielFinanceApp.addIncome(1000));
          
          // console.log(danielFinanceApp.getExpenses());
          // console.log(danielFinanceApp.addExpense(100, 'food', 'today'))
          // console.log(danielFinanceApp.addExpense(10, 'food', 'February 3'));
          // console.log(danielFinanceApp.getIncome());
          // console.log(danielFinanceApp.getExpenses());
          // console.log(danielFinanceApp.getBalance());
          
          // Second group: Carl and Kyle
          
          // Budget Class
          function Budget(budget) {
            this.budget = budget;
            this.expenses = [];
          }
          
          Budget.prototype.getBudget = function () {
            return this.budget;
          }
          
          Budget.prototype.addExpense = function (name, total) {
            let expense = new Expense(name, total);
            this.expenses.push(expense);
          }
          
          Budget.prototype.getExpense = function (name) {
            let filteredExpenses = this.expenses.filter(expense => expense.getName() === name);
            Object.keys(filteredExpenses).forEach(key => {
              console.log(`${filteredExpenses[key].info()}`)
            });
          }
          
          // do we want this to return the object, or render a display?
          Budget.prototype.getExpenses = function () {
            console.log('Current expenses are: ');
          
            this.expenses.forEach(expense => {
              console.log(`${expense.info()}`);
            });
          
          }
          
          Budget.prototype.getTotalExpenses = function () {
            let total = 0;
            this.expenses.forEach(expense => {
              total += expense.getTotal();
            });
            return total;
          }
          
          Budget.prototype.redOrBlack = function () {
            let exp = this.getTotalExpenses();
            return (this.budget >= exp) ? 'In the black!' : 'In the red...';
          };
          
          // Expense Class
          function Expense(name, total) {
            this.name = name;
            this.total = total;
          }
          
          Expense.prototype.getName = function () {
            return this.name;
          }
          
          Expense.prototype.getTotal = function () {
            return this.total;
          }
          
          Expense.prototype.info = function () {
            return `${this.name} : ${this.total}`;
          }
          
          let myBudget = new Budget(2000);
          console.log(myBudget.getBudget());
          myBudget.addExpense('gas', 25);
          myBudget.addExpense('gas', 36);
          myBudget.addExpense('takeout', 75);
          myBudget.addExpense('groceries', 2500);
          
          console.log(myBudget.getExpenses());
          console.log(myBudget.getExpense('gas'));
          console.log(myBudget.getExpense('takeout'));
          console.log(myBudget.getExpense('groceries'));
          
          console.log(myBudget.getTotalExpenses());
          console.log(myBudget.redOrBlack());
          ```
  </details>          
- mini-websites
<details>
- **mini Express.js application**
    
    [Pair Coding Challenge](https://www.notion.so/Pair-Coding-Challenge-6bb6abd0d812447cab1fcf80097073ac?pvs=21)
</details> 


# Organization

### Time:
It's up to you how long do you want a session like this to last. From other's experience, anything between 1 and 3 hours (depending on the projects) is what's recommended. 

### Place
There are several options of software that you can choose from to host your session:
- Use the SPOT rooms and/or Breakout rooms in [Gather](https://shorturl.at/YgIKB).
- **Zoom** (with break-out rooms) - if you have access to the paid version. Unfortunately, we don't have paid Zoom with the possibility for break-out rooms at the SPOT.
- **Google Meets:** You can simulate break-out rooms by simply creating several links where each corresponds to a room. You can then keep the links in a place where everyone has access to them, such as common coderPad or chat. For example:
    - Main Room: link1
    - Group1: link2
    - Group2: link3
    - Group3: link4
- **Discord Server:** You can create a Discord Server for your event, and create a separate room for each group


### Software for Collaborative Coding
There are several options that can be used for collaborative coding:

- **CoderPad** (we all know this one 🙂
- [**repl.it**](http://repl.it) (works similar to coderPad but it has an option of uploading files, which can be useful if you need some graphics or several files for the project
- **Visual Studio Code** `live share` plugin: [Here](https://visualstudio.microsoft.com/services/live-share/) are more details on what it is and how to install it.
    
    ps. VScode live share has the option to make a call as well!  
    

### Instruction for the participants
It's always a good idea to prepare some instructions for the participants before head. 

<details>
- **Feel free to use this template:**
    
    ## Before the session:
    
    **Set-up (directories and modules)**
    
    - directory set-up
    - installation of modules and libraries
    - other
    
    ## During the session:
    
    Details: (how much time?, links to repl etc.) 
    
    Task: (describe what the groups will do)
    
    Steps or hints: *optional (describe what could be some steps that the groups should do) 
</details>
  
<details>  
- **Here is an example of instruction:**
    
    ### Before the session:
    
    1. **Set-up (directories and modules)**
        - **directory set-up:**
            
            ```jsx
            dir_name:
              index.js
              .gitignore
              public
                -images
                - stylesheets
                  - application.css
              views
                - layout.pug
                - index.pug
                - menu.pug
            ```
            
        - **npm init**
        - **place node_modules in `.gitignore`**
        - **install libraries**
            
            ```jsx
            npm install express morgan express-flash express-session connect-loki express-validator pug --save
            ```
            
        - **install nodemon**
            
            ```jsx
            npm install nodemon --save-dev
            ```
            
            - script in `package.json` :
            
            ```jsx
            "scripts": {
                "start": "npx nodemon hello.js",
            ```
            
        - **require modules**
            
            ```jsx
            const express = require("express");
            const morgan = require("morgan");
            const flash = require("express-flash");
            const session = require("express-session");
            const { body, validationResult } = require("express-validator");
            
            const store = require("connect-loki");
            
            const app = express();
            const LokiStore = store(session);
            
            app.set("views", "./views");
            app.set("view engine", "pug");
            
            app.use(morgan("common"));
            ```
            
    2. **Visual Studio:**
        - install `life share` extension
    
    ### During The session
    
    **Task:**
    
    Your task for today will be to create a simple application for a local restaurant. The final application should have the following:
    
    - home page with:
        - a title
        - an image (of a hamburger??)
        - a link to a menu
        
        ![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/92b5e768-33f8-4a6b-bf7a-08665d1e6281/Screenshot_from_2021-06-09_15-51-15.png)
        
    - a menu page:
        - with some items and prices:
            - for inspiration:
                
                ```jsx
                const menu_items = [
                  {
                    header: 'Appetizers',
                    dishes: [{
                      name: 'tomato salad',
                      price: '$10'
                    },
                    {
                      name: 'mashed potatos',
                      price: '$5'
                    }],
                  },
                  {
                    header: 'Soups',
                    dishes: [{
                      name: 'vegetable soup',
                      price: '$12'
                    },
                    {
                      name: 'tomato soup',
                      price: '$15'
                    }]
                  },
                  {
                    header: 'Main',
                    dishes: [{
                      name: 'hamburger',
                      price: '$20'
                    },
                    {
                      name: 'chicken burger',
                      price: '$16'
                    },
                    {
                      name: 'vegetable burger',
                      price: '$13'
                    }]
                  }
                ];
                ```
                
        - a link to 'make orders' page
        - a link to home page
        
        ![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4da7626-b501-4568-af8f-9415f2e06969/Screenshot_from_2021-06-09_15-52-20.png)
        
    - orders page:
        - with a simple form to take orders: (name, order) (You can add other fields if you want)
        - a link to go back to main page
        
        ![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d42d0691-215d-4adb-b048-395915f46d62/Screenshot_from_2021-06-09_15-52-23.png)
        
    - don't worry about CSS
    - don't worry about form validation at this stage
    
    **Steps:**
    
    1. create templates for `index.pug` and `layout.pug`. You can use this bolierplates:
        - for index.pug:
            
            ```jsx
            doctype html
            
            html(lang="en-US")
              head
                title Todo App
              body
                header
                  h1 Todo Tracker
            ```
            
        - for layout.pug:
            
            ```jsx
            doctype html
            
            html(lang="en-US")
            
              head
                title Your Restaurant Title
                meta(charset="UTF-8")
                
            
              body
                header
                  h1 Name of your Restaurant 
            
                main
                  block main
            ```
            
    2. create the first route for the home page and call Express to listen on port 3000
    3. creates a route and a template for the menu page
    4. create a route and a template for `order-food` page 
    5. create a post route for the `order-food`  
    6. store all orders in an `orders` array
    
    **If you have time:** 
    
    - validate and sanitize user input
    - display an error message if the input is incorrect and a success message if the order has been completed.
    - preserve user input while displaying error messages
    - provide session persistence
    - provide storage to store all orders
    - provide flash error messages
    - create a new page `all orders` and display all orders there
</details> 

### Dividing participants into groups
The number of people in the groups is entirely up to you, but what works best is to have groups of two or three people. 

<details>
- **Feel free to use this script to randomly divide people into groups: (JavaScript)**
    
    ```jsx
    function divideIntoGroups(arrOfStudents, groupSize) {
      let groups = {}
      
        for (let i = 0; i < groupSize; i++) {
          groups[`Group ${i}`] = [];
        }  
      while (arrOfStudents.length > 0) {
        for (let key in groups) {
          arrOfStudents.sort(() => Math.random() - 0.5);
          groups[key].push(arrOfStudents[0]);
          arrOfStudents.shift();
        }
      }
      return groups;
    }  
    
    divideIntoGroups(['Ally','John','Mary' ,'Adam'], 2)); // => {Group1: ['Ally', 'Adam'], Group2: ['Mary, 'John']}
    ```
</details>

<details>
- **Feel free to use this script to randomly divide people into groups: (Ruby)**
    
    ***(Big thanks to Jordan Whistler for sharing his script!)*** 
    
    ```jsx
    #!/usr/share/rvm/rubies/ruby-2.7.1/bin/ruby
    require 'csv'
    file = CSV.read('/home/jordan/Desktop/ChallengePairs.csv', {headers: true})
    people_by_track = file.group_by { |person| person[1] }
    pairs = [people_by_track['Javascript'], people_by_track['Ruby'], people_by_track['None']]
    pairs.map! do |pair|
      pair.shuffle unless pair.nil?
    end
    pairs = pairs.flatten(1).each_slice(2).to_a
    room = 1
    puts "Pairs:\n\n"
    pairs.each do |pair|
      person1 = pair[0] || [ "Unpaired", "None" ]
      person2 = pair[1] || [ "Unpaired", "None" ] 
      puts "#{person1[0]} (#{person1[1]}) & #{person2[0]} (#{person2[1]}) in Room #{room}"
      room += 1
    end
    ```
    
    You'll have to:
    
     1) change the shebang to match your ruby install (do a `which ruby` then copy that over) if you want to do a `chmod +x` on it. Otherwise just run it with ruby `pairmaker.rb`
    
    2) make sure your csv file path goes in the CSV.read method there on the third line
    
    I just formatted the csv like this:
    
    ```jsx
    Name	JS/Ruby Track
    Katarina Rosiak	Javascript
    Ainaa Sakinah	Ruby
    Tzvi	Javascript
    Marc Hermann	Javascript
    Ricky Viejo	Ruby
    Arun Paul Gopal	Ruby
    Andrew Moore	Ruby
    Parker Young	Ruby
    Iuliu Pop	Ruby
    Sean Richardson	Ruby
    Pauline Tanzman	Ruby
    Isaak	Ruby
    Steve Gontzes	Ruby
    Stefano Schmidt	Javascript
    Lisa Melo	Ruby
    ```
    
    when you run it in terminal it'll output something like this:
    
    ```jsx
    Pairs:
    Unpaired (None) & Steve Gontzes (Ruby) in Room 1
    Ricky Viejo (Ruby) & Arun Paul Gopal (Ruby) in Room 2
    Ainaa Sakinah (Ruby) & Parker Young (Ruby) in Room 3
    Andrew Moore (Ruby) & Sean Richardson (Ruby) in Room 4
    Iuliu Pop (Ruby) & Pauline Tanzman (Ruby) in Room 5
    Isaak (Ruby) & Lisa Melo (Ruby) in Room 6
    Unpaired (None) & Unpaired (None) in Room 7
    ```
</details>
