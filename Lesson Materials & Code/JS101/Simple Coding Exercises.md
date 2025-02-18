### Generating:

- generate an array of numbers from `startNum` to `endNum`
    - **Excercise:**
        
        Create a function that takes two arguments: starting number and end number and returns an array with numbers starting from `startNumber` and ending on `endNumber`. For example: 
        
        ```jsx
        generateArr(3, 10); // [3, 4, 5, 6, 7, 8, 9, 10]
        ```
        

### Counting:

- **letters/characters in a string**
    - **Exercise1:**
        
        Create a function that takes a string as an argument and return an object with letters of the string and their occurrence as properties:
        
        eg: `{a:2, b: 3}`
        
        ```
        countOccurencies('abbab'); => {a:2, b: 3}
        
        ```
        
        - **Explore more:**
            
            Create a function that takes the object that your function returned as an argument and returns a string in with all the letters that appears in the object, in alphabetical order appearing as many times as the value states. Order doesn't matter. For example:
            
            ```
            {a:1, k:3, g:2} => 'aggkkk'
            
            ```
            
        
- **words in a string**
    - **Exercise**:
        
        Create a function that takes a string a s an argument and returns a number of words in that string
        
        For example:
        
        ```
        countWords('hello world'); // => 2
        
        ```
        
        - **Explore more:**
            
            Create a function that takes a string as an argument and returns an object containing all of the words from the string and count occurrences of that word. For example:
            
            ```
            countWords('Hello, hello wolrd'); // => {'hello' : 2, 'world' : 1};
            
            ```
            
- **specific characters in a string**
    - **Exercise:**
        
        Create a function that takes a string aas an argument and returns
        
        ```
        countChar('hello, world', ); //=>
        
        ```
        
- **specific sub-strings in a string or array of strings**
    - **Exercises**:
        
        Create a function that takes two strings as an argument and returns a number representing occurrences of the second argument as a sub-string of the first argument, for example:
        
        ```
        countSubstr('Hello, Hello! How are you doing Mellody?', 'ello' );// => 3
        
        ```
        
- **specific elements of an array**
    - Exercises:
        
        Create a function that takes an array and a string as an arg
        
        ```
        countEle(['name', 'year', 'age', 'name'], 'name'); // => 2
        countEle([1,2,3,4,5,1,2,3,4], 2); //=> 2
        
        ```
        
- **duplicates**
    - **Exercises:**
        - Create a function that takes a string as an argument and returns a number representing number of words that occurred more than once in that string, for example:
            
            ```
            countDuplic('one two one three two'); //=> 2
            countDuplic('flower cat cat dog flower dog'); //=> 3
            
            ```
            
        - Create a function that takes a string as an argument and returns a number representing occurrences of all letters that appears exactly twice, for example:
            
            ```
            countDuplic('123123'); //=> 3
            countDuplic('abcdea ab'); //=> 1
            
            ```
            
- **pairs in an array**
    - **exercise**:
        
        Create a function that takes an array as an argument and returns an new array containing all of the array elements that appears twice, for example:
        
        ```
        appearTwice([1, 2, undefined, 'hello', 2, undefined]); //=> [2, undefined];
        
        ```
        
- **Additional** **Exercises:**
    - count how many uppercase letters in a string
    - count how many numbers in a string
    - count how many each characters in a string
    - how many words in a string
    - how many , in a string
    - how many sub-strings 'hel' in a string
    - how many 'car' in an array
    - how many different types of car in an array and how many of each type: ['Lambo', 'Tesla', 'Mercedes', 'Mercedes', 'Fiat', 'Lambo', 'Lambo']

### Sorting

- **sorting elements (numbers, strings) descendant / ascendant / alphabetical / length / numerical / lexicographical order**
    - **Exercises:**
        - Create a function that takes an array as an argument and returns the same array with all elements sorted in alphabetical order. For example:
            
            ```
            sorting(['a', 'd', 'a', 'b']); //=> ['a', 'a', 'b', 'd'];
            sorting('banana', 'apple', 'pear'); //=> ['apple', 'banana', 'pear']
            
            ```
            
        - Create a function that takes an array as an argument and returns the same array with all elements sorted in descending order. For example:
            
            ```
            sorting([3,5,1,2,11,456]); //=> [456,11,5,3,2,1];
            
            ```
            
        - Create a function that takes an array as an argument and returns the same array with all elements sorted in ascending order. For example:
            
            ```
            sorting([3,5,1,2,11,456]); //=> [1,2,3,5,11,456];
            
            ```
            
        - Create a function that takes an array of strings as an argument and returns the same array with all elements sorted according to length of the string in ascending order. For example:
            
            ```
            sorting(['o', 'hello', 'llo', 'ello','lo' ]); // => ['o', 'lo', 'llo', 'ello', 'hello']
            
            ```
            
        - Create a function that takes an array of strings as an argument and returns the same array with all elements sorted according to length of the string in descending order. For example:
            
            ```
            sorting(['o', 'hello', 'llo', 'ello','lo' ]); //=> ['hello', 'ello', 'llo', 'lo', 'o']
            
            ```
            
        - Create a function that takes an array of strings as an argument and returns the same array with all elements sorted according to length of the string in alphabetical order, case insensitive. For example:
            
            ```
            sorting(['goo', 'A', 'aB', 'Ab', 'c', 'C']); // => ['A', 'aB', 'Ab', 'c', 'C', 'goo']
            
            ```
            
- **sorting arrays of object by key or value**
    - **Exercises**:
        - Create a function that takes an array of objects as argument and return the same array with all the elements sorted according to it's value in ascending order. For example:
            
            ```
            sorting([{a: 1}, {a: 0}, {a : 3}]); //=> [{a:0}, {a:1}, {a:3}];
            
            ```
            
        - Create a function that takes an array of objects as argument and return the same array with all the elements sorted according to it's key in descending order. For example:
            
            ```
            sorting([{0: 1}, {3: 1}, {1 : 1}]); //[{3:1}, {1:1}, {0:1}]
            
            ```
            
- **sorting array elements by sum of the inner array elements**
    - **Exercises:**
        - Create a function that takes an multidimensional array as an argument and returns the same array sorted according to the sum of elements of inner arrays., in ascending order For example:
            
            ```
            sorting([[1,2,3], [0,1], [2,1]]); //=> [[0,1], [2,1], [1,2,3]]
            
            ```
            
        - Create a function that takes an multidimensional array as an argument and returns the same array sorted according to the product of elements of inner arrays in descending order. For example:
            
            ```
            sorting([[1,2,3], [0,1], [2,1]]); //=> [[1,2,3], [2,1], [0,1]]
            
            ```
            
- **Additional exercises:**
    - Create a function that takes an multidimensional array and returns an array sorted in descending order according to length of the array. For example:
        
        ```
        sortArrLength([[1,2,undefined], [null, 0, 'hello wolrd', 11], [{1:1}]]); //[[null, 0, 'hello wolrd', 11], [1,2,undefined], [{1:1}] ];
        sortArrLength(['a'], ['ab', 'a', null], [101, 1]); //[['ab', 'a', null], [101, 1], ['a']]
        
        ```
        
    - Create a function that takes an array of objects as an argument and return sorted array in ascending order depending on sum of an array stored as a value of key `arr`. For example:
        
        ```
        sortArrOfObj([{arr : [1,2]}, {arr: [11]}, {arr: 1,2,3,0}]); // [{arr : [1,2]}, {arr: 1,2,3,0}, {arr: [11]}];
        
        ```
        
    - Create a function that takes an array of arrays as argument and returns a sorted array in ascending order depending on how many `undefined` exist in the array. For example:
        
        ```
        sortUndefined([[11, undefined, undefined, null, 0], [NaN, {}, ''], [undefined]]); // [[NaN, {}, ''], [undefined], [11, undefined, undefined, null, 0] ]
        
        ```
        

### Sub-strings

- **creating all leading sub-strings from a string**
    - **Exercises:**
        - Create a function that takes a string as an argument and returns an array with all leading sub-strings of that string. For example:
            
            ```
            allLeadSubstr('abcd'); // => ['a', 'ab', 'abc', 'abcd'];
            
            ```
            
        - Create a function that takes a string as an argument and returns an array with all leading sub-strings of that string that are 3 letters or longer. For example:
            
            ```
            allLeadSubstr('abcdef'); //=> ['abc', 'abcd', 'abce', 'abcdef'];
            
            ```
            
        - Create a function that takes a string as an argument and returns an array with all leading sub-strings of that string that are shorter than 5 letters, starting from the longest to the shortest. For example:
            
            ```
            allLeadSubstr('abcdefg'); //=> ['abcd', 'abc', 'ab', 'a'];
            
            ```
            
- **creating all sub-string from a string**
    - **Exercises:**
        - Create a function that takes a string as an argument and returns an array with all the sub-string of given string. For example:
            
            ```
            allSubstr('abcd'); //=> ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
            
            ```
            
        - Create a function that takes a string as an argument and returns an array with all the sub-string of given string that are longer than 1 letter. For example:
            
            ```
            allSubstr('abcd');//=> ['ab', 'abc', 'abcd', 'bc', 'bcd', 'cd'];
            
            ```
            
        - Create a function that takes a string as an argument and returns an array with all the sub-string of given string that are exactly 3 letters long. For example:
            
            ```
            allSubstr('abcd'); // => ['abc', 'bcd'];
            
            ```
            

### Playing with words

- **Anagram**
    
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    
    - Excercises:
        - Create a function that takes two strings as arguments and returns a boolean value of two words are anagrams and false if they are not anagrams. For example:
        
        ```
        isAnagram('aba', 'aab'); // true
        isAnagram('aba', 'aa'); //false
        
        ```
        
- **Pangram**
    
    A phrase or sentence containing all 26 letters of the alphabet (ideally repeating as few letters as possible). You may remember this one from typing class: "The quick brown fox jumped over the lazy sleeping dog," but Willard Espy came up with a shorter and more interesting one: "Bawds jog, flick quartz, vex nymphs." An abundance of pangrams, using some very obscure words or initials can be found here.
    
    - Exercise:
        
        Create a function that takes a string as an argument and returns a boolean value, true if the word is a pangram and false if it's not. For example:
        
        ```
        isPangram("The quick brown fox jumped over the lazy sleeping dog,"); //true
        isPanagram('abcd'); //false
        
        ```
        
- **Isogram**
    
    A word in which no letter of the alphabet occurs more than once. Dimitri Borgmann's longest example: dermatoglyphics, the study of skin markings or patterns on fingers, hands, and feet, and its application, especially in criminology.
    
    - exercise:
        
        Create a function that takes one string as an argument and returns a boolean value, true if the word is a isogram and false if it's not. For example:
        
        ```
        isIsogram('dermatoglyphics'); // true
        isIsogram('alabama'); //false
        
        ```
        
- **Palindrome**
    
    A word, sentence, or longer written work that reads the same backwards. Example: A declaration facetiously attributed to Napoleon, "Able was I ere I saw Elba." Weird Al Yankovic's song "Bob" spoofs Bob Dylan's "Subterranean Homesick Blues" using a slew of palindromes. Need more palindromes? Find a huge stash here.
    
    - exercise:
        
        Create a function that takes one string as an argument and returns a boolean value, true if the string is a palindrome and false if it's not. For example:
        
        ```
        isPalindrome('kayak'); //true
        isPalindrome('apple'); //false
        
        ```
        
- **Lipogram**
    
    A written work composed of words chosen to avoid the use of one or more letters. You may hail F. Scott Fitzgerald's Gatsby as great, but in 1939 Ernest Vincent Wright produced the phenomenal Gadsby: A Story of Over 50,000 Words Without Using the letter "E," a scarcely believable achievement considering that "E" is the most common letter in English. Imagine an entire novel without he, she, the, or the past tense marker —ed.
    
    - exercise:
        
        Create a function that takes two strings as  arguments and return a boolean value if the first string contains all of the letters of alphabet except the one that is the second argument. For example:
        
        ```
        isLipogram('abcdefghijklmnopqrstuvwxy', 'z'); //true
        isLipogram('abc', 'd'); //false
        
        ```
        
- **Tautonym**
    
    a word or name made up of two identical parts, such as so-so, tom-tom or Pago Pago.
    
    - exercise:
        
        Create a function that takes a string as an argument and returns a boolean value, true if the word is a tautonym and false if it's not. For example:
        
        ```
        isTatutonym("Pago Pago"); //true
        isTautonym('abcd'); //false
        
        ```
        
- **Ambigram**
    
    A term coined by John Langdon for words made to look the same when inverted with the help of calligraphy. Willard Espy calls a word that looks the same upside down an invertogram and Schaaf calls a number like that strobogrammatic. Examples: NOON, SWIMS, SIS; 1881, 1961, 91016.
    
    - exercise:
        
        Create a function that takes a string as an argument and returns a boolean value if the word is a amibgram and false if it's not. For example:
        
        ```
        isAmbigram('NOON'); //true
        isAmbigram('sun'); //false
        
        ```
        

### Strings

- **checking if is in alphabetical order**
    - **exercise:**
        
        Create a function that takes a string as a an argument and returns a boolean, true if the string is in alphabetical order and false if it's not. For example:
        
        ```
        isAlphabetical('abcdefg'); //true
        isAlphabetical('adegttksn'); //false
        
        ```
        
- **checking if a string** **has only vowels / consonants / numbers / upper or lowercase / any specific character**
    - **exercises:**
        - **vowels:**
            
            Create a function that takes a string as an argument and return a boolean, true if the string contains only vowels and false otherwise. For example:
            
            ```
            hasOnlyVowels('aaeuiooae'); //true
            hasOnlyVowels('tgbhrrf_00&'); //false
            
            ```
            
        - **consonants**
            
            Create a function that takes a string as an argument and return a boolean, true if the string contains only vowels and false otherwise. For example:
            
            ```
            hasOnlyConsonants('typRRWQQL'); //true
            hasOnlyConsonants('AccdE4$$ __ '); //fa;se
            
            ```
            
        - **numbers**
            
            Create a function that takes a string as an argument and return a boolean, true if the string contains only vowels and false otherwise. For example:
            
            ```
            hasOnlyNumbers('12311'); //true
            hasOnlyNumbers('Pdd00_4a11'); //false
            
            ```
            
        - **upper and lowercase**
            - Create a function that takes a string as an argument and return a boolean, true if the string contains only upper case letters and false otherwise. For example:
                
                ```
                hasUpperC('OOPDDBW'); //true
                hasUpperC('dujjJJD'); //false
                
                ```
                
            - Create a function that takes a string as an argument and return a boolean, true if the string contains only lower case letters and false otherwise. For example:
                
                ```
                hasLowerC('opddghrr'); //true
                hasLowerC('dujjJJDdd'); //false
                
                ```
                
        - **any specific character**
            
            Create a function that takes two strings as an argument and returns a boolean value, true if the first string contains the second one. For example:
            
            ```
            hasString('abcd', 'd'); //true
            hasString('abcd', 'f'); //false
            
            ```
            
- **segregating**
    
    Create a function that takes a string as an argument and returns an object containing strings segregated as follows: numbers, upper case letters, lower case letters, other symbols. For example:
    
    ```
    segregate('aad559 $%,'); //{lettersUpper: '', lettersLower: 'aad', numbers: '559', other characters: '$%,' }
    segregate('11AB'); //{lettersUpper: 'AB', lettersLower: '', numbers: '', other characters: '' }
    
    ```
    
- **checking if a string** **includes only the same characters**
    - **exercises:**
        
        Create a function that takes a string as an argument and return a boolean, true if all characters in the string are the same characters and false otherwise.
        
        ```
         haveSameChar('aaaaaa') //true
         haveSameChar('cccb9') //false
        
        ```
        

### Extracting/ Removing

- e**xtracting a specific part of a string**
    - **exercises:**
        - Create a function that takes a string as an argument and return an array of words that exist in that strings and begins with letter `a`. For example:
            
            ```
            extractStr('abcd bcd aa'); //[abcd, aa]
            
            ```
            
        - Create a function that takes two strings as arguments a return an array of sub strings that are the same as the second argument. For example:
            
            ```
            extractStr('abcdefabcdefabcdef abcdefg', 'abc'); //['abc', 'abc', 'abc', 'abc'];
            
            ```
            
        - Create a function that takes a string as an argument and return an array of all the alphanumeric characters that the input string contained. For Example:
            
            ```
            etractStr('abcd123acc 227 0 , *&^a'); //['1', '2', '3', '2', '2', '7', '0'];
            
            ```
            
- **removing and extracting duplicates from a string or array:**
    - **remove duplicates code:**
        - **exercise:**
            
            Create a function that takes an array as argument and returns  a new array with all the elements that appears more than once removed. For example:
            
            ```
            removeDuplicate([1, 2, 3, 5, 2, 1, 5, 2 ]); //=> [1, 2, 3, 5];
            
            ```
            
    - **extract duplicates code:**
        - **exercise:**
            
            Create a function that takes an array as an argument and return an array containing all the elements of argument array that appears more than once. For example:
            
            ```
            extractDup([1,2,3,4,1,2]); //[1,2];
            
            ```
            
- **extracting** **characters/elements that appear a specific number of times in a string or array**
    - **exercises:**
        - Create a function that takes a string and a number as arguments and return an array containing all the characters that appears in the string as many times as the second argument. For Example:
            
            ```
            extractChar('abcabcdefra', 2); // ['b', 'b', 'c', 'c'];
            
            ```
            
        - Create a function that takes an array and a number as arguments and return an array containing all the elements that appears in the array as many times as the second argument. For Example:
            
            ```
            extractEl(['a', 1, 'A', 'a', 'a', '111', 1, 1], 3); ['a', 'a', 'a', 1, 1, 1];
            
            ```
            
- **remove certain element from a an array**
    - **exercise:**
        
        Create a function that takes two arguments: an array with elements and another element, which can be any primitive data type, and return the same array with the second argument of the function, removed from that array. For example:
        
        ```
        let arr = [1,2,3];
        let arr3 = removeEl(arr, 2); //[1, 3]
        arr === arr3 //true
        
        ```
        

### Transformation

- t**ransform lowercase to uppercase (whole string, only first letter, every second letter)**
    - **Exercises:**
        
        Create a function that takes a string as an argument and return a new string with all the letters upper-cased. For example:
        
        ```
        allUpper('abcd'); //'ABCD'
        
        ```
        
        Create a function that takes a string as an argument and return a new string with every second letter changed to upper case. For example:
        
        ```
        toUpper('abcdef'); //'aBcDeF'
        
        ```
        
- **reversing strings**
    
    Create a function that takes a string as an argument and return a new, reversed string. For example:
    
    ```
    reverseIt('abcdef'); //'fedcba'
    
    ```
    
- **remove characters and elements**
    - Create a function that takes two strings as arguments. The second string represents a character that is supposed to be removed from the string. For example:
        
        ```
        removeIt('abcdefghd', 'd'); //'abcefgh'
        
        ```
        
    - Create a function that takes an array and a string as arguments and return an array with the second string removed as elements of the first array argument. For example:
        
        ```
        removeIt(['a', 0, undefined, 'aa', 'a', 'A', []], 'a');//[ 0, undefined, 'aa', 'A', []]
        
        ```
        
- **replacing characters**
    - Create a function that takes three strings as arguments and return a string with all the characters that are the same as the second argument replaced with the thirds argument character. For example:
        
        ```
        replaceIt('abcdefgaa', 'a', '00'); '00bcdefg0000'
        
        ```
        
    - Create a function that takes three arguments: an array, a string, and a string and returns an array with all the elements that are the same as the second argument replaced with the third argument. For example:
        
        ```
        replaceIt(['a', 'b', NaN, [], 'A', 'aa', 'a'], 'a', '00'); //['00', 'b', NaN, [], 'A', 'aa', '00']
        
        ```
        
- **rotating**
    
    Create a function that takes a string as an argument and a number and console log the string rotated by one to the right as many times as the second argument. For example:
    
    ```
    rotate('abcdefg', 3);
    //'bcdefga'
    //'cdefgab'
    //'defgabc'
    
    ```
    
- **swapping**
    - Create a function that takes a string as an argument and returns a string with the first and the last character swapped. For example:
        
        ```
        swappIt('abcdef'); //'fbcdea'
        
        ```
        
    - Create a function that takes an array as an argument and returns an array with all the pair elements swapped. So the elements with index `0` will swap the place with element with index `1`, the elements with index `2` will swap place with element number `3`, and so on. For example:
        
        ```
        swappIt(['a', 0, undefined, [], NaN, {1:2}]);//[0, 'a', [], undefined, {1:2}, NaN]
        
        ```
        
- **transform 2D arr into 1D array**
    
    Create a function that takes a two-dimensional array and transforms it into a one-dimensional array. For example:
    
    ```
    transformIt([[1], [2], [3]]); // [1,2,3]
    
    ```
    

### Finding

- **specific character, number, array element in a string or object/array**
    - Create a function that takes two strings as arguments and returns a boolean value `true` if a second argument (a character) exists in the first argument (longer string) and `false` otherwise. For example:
        
        ```
        findMe('abcdefghijk', 'a'); //true
        findMe('abcdefgh', 'z'); //false
        
        ```
        
    - Create a function that takes two arguments: an array of different elements and a number. The function should return an index's number of that number in the array and `false` if the number doesn't exist in the array. For example:
        
        ```
        findMe([5, null, undefined, 0, '11', 11, {'11':11}, [11, '11']], 11);// 5
        findMe([5, null, undefined, 0, '11', {'11':11}, [11, '11']], 11) //false
        
        ```
        
    - Create a function that takes two arguments: an object containing several properties and an array and returns `true` if any of the object's values looks like the array passed as an argument. Note that it doesn't have to be the same array in terms of the place in the memory. They just have to have the same primitive values as arguments. Return `false` otherwise. For example:
        
        ```
        findMe({'prop1': [1, '2'], 'prop2': 1, 'prop3': [1,2]}, [1, 2]); //true
        findMe({'prop1': [1, '2'], 'prop2': 1, 'prop3': [2, 1]}); //false
        
        ```
        
- **indexes**
    
    Create a function that takes two strings as an argument and returns a number representing an index number of the the character passed as a second argument in the first string argument. If the character doesn't exist in the string the function should return `false`. For example:
    
    ```
    findIndex('Aabcdefgh ab A', 'a'); //1
    findIndex('bcdefgBA', 'a'); //false
    
    ```
    
- **missing characters in a sequence**
    
    Create a function that takes an array of numbers as an argument and returns a number that is missing in the specific sequence. Return `false` if there is no missing elements.
    
    - Specific range:
    
    ```
    findMissisng([0,1,2,3,5,6,7]); //4
    findMissing([100, 101, 102, 103, 104, 106, 107]); //105
    findMissing([34, 35, 36, 37, 38, 39]); //false
    
    ```
    
    - prime numbers sequence:
    
    ```
    findMissingPrime([2, 3, 5, 11, 13, 17, 19, 23]);  //7
    findMissingPrime([23, 29, 31, 41, 43, 47, 53, 59, 61]); //37
    findMissingPrime([53, 59, 61, 67, 71, 73, 79, 83]); //false
    
    ```
    
    - fibonacci sequence: * extra excercise
    
    ```
    findMissingFibo(1, 1, 2, 3, 8, 13, 21, 34, 55) //5
    findMissingFibo([ 8, 13, 21, 34, 55]); //false
    
    ```
    
- **duplicates**
    - Create a function that takes a string as an argument and returns an array containing all characters that appear in the strings more than once. For example:
        
        ```
        findDuplicates('kabcdeffghhijk'); //['k', 'f', 'h']
        
        ```
        
    - Create a function that takes an array as an argument and returns another array containing all elements of the argument array that appears more than once, Note that the elements have to be the same elements (represented by the same place in the memory), for Example:
        
        ```
        findDuplicates([1, 1, [], [], {1:1}, {1:1}, 'hello', undefined); //[1]
        findDuplicates([1, 2, 3, [], [], null]) //false
        
        ```
        
    - Create a function that takes an object as an argument and return an array containing elements that exist in the argument object more than once as values. Note that the elements have to be the same elements (represented by the same place in the memory). For example:
        
        ```
        findDuplicates({1:1, 2:2, 'a':1, 'b':2, 'c': '1', 'd':11}); //[1,2];
        findDuplicates({1:1, 2:'abcd', 3:undefined, 4:'1'}); //[];
        
        ```
        
- **find if there is a pair in a str. '(' , ')', '[', ']' etc.**
    
    Create a function that takes a string as an argument and returns `true` if the string contains a pair of parenthesis, where '(' and ')' is a pair but ')' and ')' is not. Return `false` otherwise. For example:
    
    ```
    findPairs('abcd(abcd ) dbb ) ddss ('); //true
    findPairs('ab))) ccc ((('); //true
    findPair('(fff))))(('); //false
    findPairs('(((((('); //false
    findPairs('()()())()()('); //true
    
    ```
    
- **find the lowest number in arr**
    - Create a function that takes an array with numbers and returns a number that is the lowest number in that array. For example:
        
        ```
        lowest([1,3,4,6,11,9,0,1]); //0
        lowest([5,6,3,4,8,1]); //1
        
        ```
        
    - Create a function that takes an array with numbers and returns a number that is the highest number in that array. For example:
        
        ```
        highest([1,2,4,66,2224, 189, 0]); //2224
        highest([3,222,156,109, 999, 1]); //999
        
        ```
        
    - code:
        
        ```
        let arr = [2,3,1];
        console.log(Math.min(...arr))
        
        // => 1
        
        ```
        

### Comparing

- **comparing two strings**
    - Create a function that takes two strings as arguments and return a boolean value `true` if those two strings are the same and `false` otherwise. For example:
        
        ```
        theSame('abcdf', 'Abcdf')//false
        
        ```
        
    - Create a function that takes two strings as arguments and return a boolean value `true` if those two strings have the same characters (ignoring the case), and `false` otherwise. For example:
        
        ```
        theSame('abcdef', 'ABCDef') //true
        theSame('abcdef', 'a bcdef') //false
        
        ```
        
- **comparing arrays**
    - Create a function that takes two arrays as arguments and return a boolean value `true` if two arrays pointing to the same space in the memory and `false` otherwise. For example:
        
        ```
        let a = [1,2,3];
        let b = a;
        let c = [1,2,3];
        
        theSame(a,b); //true
        theSame(a,c); //false
        theSame(c,b); //false
        
        ```
        
    - Create a function that takes two arrays as arguments and return a boolean value `true` if two arrays have the same values (primitives) and `false` otherwise. For example:
        
        ```
        let a = [1,2,3];
        let b = a;
        let c = [1,2,3];
        
        theSame(a,b); //true
        theSame(a,c); //true
        theSame(c,b); //true
        
        ```
        
    - Create a function that takes two arrays as arguments and return a boolean value `true` if those two arrays have the same values (primitives and objects). The same objects are objects that are pointing to the same place in the memory. For example:
        
        ```
        let a = [1,2,3];
        let b = [1,2,3];
        
        let c = [a, b]
        let d = [a, b]
        let e = [[1,2,3], [1,2,3]]
        
        theSame(c,d); //true
        theSame(c, e); //false
        theSame(d,e); //false
        
        ```
        
- **comparing objects**
    - Create a function that takes two objects as arguments and return a boolean value `true` if two objects pointing to the same space in the memory and `false` otherwise. For example:
        
        ```
        let a = {1:2};
        let b = a;
        let c = {1:2};
        
        theSame(a,b); //true
        tehSame(a,c); //false
        
        ```
        
    - Create a function that takes two objects as arguments and return a boolean value `true` if two objects have the same values (primitives) and `false` otherwise. For example:
        
        ```
        let a = {1:2, 2:3};
        let b = {1:2, 2:3};
        let c = {2:3, 1:2};
        let d = {1:2, 2:3, 3:4};
        let e = {'a': 1}
        
        theSame(a,b); //true
        thesame(a,c); //true
        theSame(a,d); //false
        theSame(a,e); //false
        
        ```
        
    - Create a function that takes two objects as arguments and return a boolean value `true` if those two objects have the same values (primitives and objects). The same objects are objects that are pointing to the same place in the memory. For example:
        
        ```
        let a = {1:2};
        let b = {2:2};
        let c = {1:a, 2:b};
        let d = {1:a, 2:b};
        let e = {1:{1:2}, 2:{1:2}};
        
        theSame(c,d); //true
        theSame(c,e); //false
        theSame(d,e); //false
        
        ```
        
- **comparing if two strings has the same sub-strings**
    - Create a function that takes two strings as arguments and return a boolean value `true` if the second string has at least one leading substring that is the same as a leading substring in the first string. Substring is at least 2 char. For example:
        
        ```
        sameSubstr('abcde', 'abiuop');// true => 'ab', 'ab'
        sameSubstr('abcdefg', 'abcrfo')// true => 'abc', abc'
        sameSubstr('abcdefg', 'fabcdefg') //false (not a leading substr)
        
        ```
        

### Generating:

- generate an array of numbers from `startNum` to `endNum`

### Counting:

- **letters/characters in a string**
- **words in a string**
- **specific characters in a string**
- **specific sub-strings in a string or array of strings**
- **specific elements of an array**
- **duplicates**
- **pairs in an array**
- **Additional** **Exercises:**

### Sorting

- **sorting elements (numbers, strings) descendant / ascendant / alphabetical / length / numerical / lexicographical order**
- **sorting arrays of object by key or value**
- **sorting array elements by sum of the inner array elements**
- **Additional exercises:**
- code:

### Sub-strings

- **creating all leading sub-strings from a string**
- **creating all sub-string from a string**

### Playing with words

- **Anagram**
- **Pangram**
- **Isogram**
- **Palindrome**
- **Lipogram**
- **Tautonym**
- **Ambigram**

### Strings

- **checking if is in alphabetical order**
- **checking if a string** **has only vowels / consonants / numbers / upper or lowercase / any specific character**
- **segregating**
- **checking if a string** **includes only the same characters**

### Extracting/ Removing

- **extracting a specific part of a string**
- **removing and extracting duplicates from a string or array:**
- **extracting** **characters/elements that appear a specific number of times in a string or array**
- **remove certain element from a an array**

### Transformation

- t**ransform lowercase to uppercase (whole string, only first letter, every second letter)**
- **reversing strings**
- **remove characters and elements**
- **replacing characters**
- **rotating**
- **swapping**
- **transform 2D arr into 1D array**

### Finding

- **specific character, number, array element in a string or object/array**
- **indexes**
- **missing characters in a sequence**
- **duplicates**
- **find if there is a pair in a str. '(' , ')', '[', ']' etc.**
- **find the lowest number in arr**

### Deciphering according to key

### Comparing

- **comparing two strings**
- **comparing arrays**
- **comparing objects**
- **comparing if two strings has the same sub-strings**