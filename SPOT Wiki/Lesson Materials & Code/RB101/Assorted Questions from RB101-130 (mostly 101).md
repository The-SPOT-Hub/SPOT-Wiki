Course: RB101

1. What happens if you call `sort` on an array with multiple data types? What does this code return?

```ruby
[1, 'a'].sort
```

a.

```ruby
[1, 'a']
```

b. 

A type error will be thrown

c.

```ruby
['a', 1]
```

d. 

An argument error will be thrown

- Answer:
    
    ```ruby
    ['a', 1].sort # => ArgumentError: comparison of String with 1 failed
    ```
    
    D. `Sort` uses the `<=>` operator to compare items. The return value of the `<=>` method is used by `sort` to determine the order in which to place the items. If `<=>` returns `nil` to sort then it throws an argument error.
    

**2. What does the following code return?**

```ruby
[
  ['a', 'cat', 'b', 'c'],
  ['b', 2],
  ['A', 'car', 'd', 3],
  ['a', 'car', 'd']
].sort
```

a. 

It throws an ArgumentError because we can't compare integers and strings.

b. 

```ruby
[
  ["a", "car", "d"], 
  ["a", "car", "d", 3], 
  ["a", "cat", "b", "c"], 
  ["b", 2]
]
```

c.

```ruby
[
  ["a", "b", "c", "cat"],
  ["a", "car", "d"],
  ["a", "car", "d", 3],
  ["b", 2]
]
```

d.

```ruby
[
  ["b", 2],
  ["a", "car", "d"],
  ["a", "car", "d", 3],
  ["a", "cat", "b", "c"]
]
```

- Answer
    
    B: Array#sort compares each array one element at a time to determine which one comes first. When called with nested arrays, each sub array will be compared element by element and ordered based on which element comes first. An error is not thrown in this case, even though `sort` can't compare integers and strings because we can sort the subarrays without reaching the integers.
    

**3. What is output in this code?**

```ruby
def remove_evens!(arr)
  arr.each do |num|
    if num % 2 == 0
      arr.delete(num)
    end
  end
  arr
end

p remove_evens!([1,1,2,3,4,6,8,9])
```

a. 

```ruby
[1, 1, 2, 3, 4, 6, 8, 9]
```

b. 

```ruby
[1, 1, 3, 9]
```

c.

```ruby
[1, 1, 3, 6, 9]
```

d. 

```ruby
[2, 4, 6, 8]
```

- Answer
    
    B: The Array#delete method is destructive, and is changing the contents of `arr` during iteration. The return value here may or may not make some sense to you, but there's almost always a much clearer way of achieving the desired result without having to resort to mutating the collection while iterating through it.
    

**4.** Demonstrate how to create an instance of the Textbook class.

```ruby
class Book
  def initialize(args)
    @pages = args.fetch(:pages)
    @title = args.fetch(:title)
  end
end

class Textbook < Book
  def initialize(args)
    @chapters = args.fetch(:chapters)
  end
end
```

a.

```ruby
textbook = Textbook.new({ chapters: 20 })
```

b.

```ruby
textbook = Textbook.new(chapters = 20)
```

c. 

```ruby
textbok = Textbook.new({ chapters: 20, 
                         pages: 260,
                         title: "The Human Brain" })
```

d. 

```ruby
textbook = Textbook.new(20, 260, "The Human Brain")
```

The Textbook class is initialized with a hash that must contain the key :chapters. The Textbook#initialize method overwrites the Book#initialize method, so a Textbook object does not need to be initialized with a hash containing :pages or :title. initialize() is just like any other method that can be overwritten with inheritance

**5. Is it appropriate for the Board class to inherit from the Game class?**

```ruby
class Board

end

class Game

end
```

a. Yes, because a Game *has a* Board

b. No, because a board is not a game, so the "is a" test is not met. When the "is a" test is not met, inheritance should not be used.

c. No, we should use a module instead

d. Yes, because a Board will need access to the same attributes and behaviors as a Game

- Answer
    
    B
    

**6. What does the following code print?**

```ruby
puts :unicorn.reverse
```

a. 

```ruby
:nrocinu
```

b. 

```ruby
"nrocinu"
```

c.

```ruby
:unicorn
```

d.

An error message

- Answer:
    
    D. This raises an error because symbols don't have a method called reverse(). Since symbols don't have some of the capabilities of strings, they are more efficient to store in memory. It is appropriate to use symbols when the additional functionality that strings provide is not required.
    

**7. What does the following code return?**

```ruby
snowy_owl = {
  "type"=>"Bird",
  "diet"=>"Carnivore",
  "life_span"=>"10 years"
}
snowy_owl.select do |key, value|
  key == "type"
end
```

a.

```ruby
{"type"=>"Bird"}
```

b. 

An error because `select` is an Array method and won't work for a Hash

c. 

```ruby
"Bird"
```

d.

```ruby
["type", "Bird"]
```

- Answer
    
    A: The `select()` method is used to find the key/value pair with the key equal to `"type"`.
    

**8. Given the following code:**

```ruby
personality_types = ["bad", "good", "great"]
# omitted code

puts personality_types
# ["bad person", "good person", "great person"]
```

Which of these lines of code will mutate the `personality_types` array to this:

```ruby
["bad person", "good person", "great person"]
```

a. 

```ruby
personality_types.each { |type| type << " person" }
```

b. 

```ruby
personality_types.each {|type| type += ' person'}
```

c. 

```ruby
personality_types.map {|type| type + ' person'}
```

d. 

```ruby
personality_types.map {|type| type += ' person'}
```

Notes: C, D return a new array. A will mutate the caller.

**9. What does the following code return when we call the `speak()` method on `Dog`?**

```ruby
class Mammal
  def speak()
    return "hello!"
  end
end

class Dog < Mammal
  include Friendable

  def speak()
    return "woof woof"
  end
end

module Friendable
  def speak()
    return "Nice to meet you!"
  end
end

Dog.speak()
```

a.

```ruby
"woof woof"
```

b. 

An error

c. 

```ruby
"hello!"
```

d. 

```ruby
"Nice to meet you!"
```

- Answer:
    
    B. This raises an error as speak() is an instance method. To call the speak() method, we must first create an instance of the Dog class:
    
    `d = Dog.new()
    d.speak()`
    

**10. Which of the following method calls will mutate the string "hello"?**

a. 

```ruby
greeting = "hello"
greeting.delete "lo"
```

b.

```ruby
greeting = "hello"
greeting.gsub(/[aeiou]/, '*')
```

c. 

```ruby
greeting = "hello"
greeting.replace("world")
```

d.

```ruby
greeting = "hello"
greeting.slice(3)
```

- Answer
    
    C: The other three return new strings. 
    

**11. What does the following code output and return?**

```ruby
{ a: "ant", b: "bear", c: "cat" }.each_with_index do |element, index|
  puts "The index of #{element} is #{index}."
end
```

a. 

```ruby
# The index of [:a, "ant"] is 0.
# The index of [:b, "bear"] is 1.
# The index of [:c, "cat"] is 2.
# => nil
```

b.

```ruby
# The index of "ant" is 0.
# The index of "bear" is 1.
# The index of "cat" is 2.
# => { :a => "ant", :b => "bear", :c => "cat" }
```

c.

```ruby
# The index of :a is "ant".
# The index of :b is "bear".
# The index of :c is "cat".
# => { :a => "ant", :b => "bear", :c => "cat" }
```

d.

```ruby
# The index of [:a, "ant"] is 0.
# The index of [:b, "bear"] is 1.
# The index of [:c, "cat"] is 2.
# => { :a => "ant", :b => "bear", :c => "cat" }
```

**12. What does the following code return?**

```ruby
{ flour: '1c', sugar: '.5c', eggs: 2 }.first(2)
```

a. 

```ruby
[[:flour, '1c'], [:sugar, '.5c']]
```

b.

An error because hashes are unordered, so we can't use the `first` method here.

c. 

```ruby
{ flour: '1c', sugar: '.5c' }
```

d. 

```ruby
[:flour, '1c']
```

- Answer
    
    A: There are a couple interesting things to note here:
    
    1. First, hashes are typically thought of as unordered and values are retrieved by keys. In some programming languages, the order is not preserved at all. This used to be true for Ruby too, but since Ruby 1.9, order is preserved according to the order of insertion. Calling `first` on a hash doesn't quite make sense, but Ruby lets you do it.
    2. Second, notice that the return value of calling `first` on a hash with a numeric argument is a nested array. This is unexpected. Fortunately, turning this nested array back to a hash is easy enough: `[[:a, "ant"], [:b, "bear"]].to_h`.
    
    In practice, `first` is rarely called on a hash, and most often used with arrays.
    

**13. What will this code return?** 

```ruby
{ a: "ant", b: "bear", c: "cat" }.include?("ant")
```

- Answer:
    
    False. When called on a hash, include? only checks the keys, not the values. Hash#include? is essentially an alias for Hash#key? or Hash#has_key?.
    

**14. What's the return value of `reject` in the following code?**

```ruby
[1, 2, 3].reject do |num|
  puts num > 2
end
```

a. 

```ruby
[3]
```

b. 

```ruby
[]
```

c.

```ruby
[1, 2, 3]
```

d. 

```ruby
[1, 2]
```

- Answer
    
    C: `reject` returns a new array containing items where the block's return value is "falsey". In other words, if the return value was false or nil the element would be selected.
    

**15. What will the following code output?**

```ruby
a = 7
array = [1, 2, 3]

def my_value(ary)
  ary.each do |b|
    a += b
  end
end

my_value(array)
puts a
```

a. 

An error will be raised

b.

```ruby
13
```

c.

```ruby
7
```

d.

```ruby
10
```

- Answer
    
    ```ruby
    undefined method `+' for nil:NilClass (NoMethodError)
    ```
    
    `a` at the top level is not visible inside the invocation of the `each` method with a block because the invocation of `each` is inside `my_value`, and method definitions are self-contained with respect to local variables. Since the outer `a` is not visible inside the `my_value` method definition, it isn't visible inside the method invocation with a block.
    

**16. The following code doesn't work as expected.** 

```ruby
def someMethod(array, &block)
  array.map(block)
end

p someMethod([1, 3, 5]) { |n| n**2 }
```

**Which of the following changes will produce the array `[1, 9, 25]`?**

a.

```ruby
def someMethod(array, &block)
  array.map(block.call)
end

p someMethod([1, 3, 5]) { |n| n**2 }
```

b. 

```ruby
def someMethod(array, &block)
  array.map(&block)
end

p someMethod([1, 3, 5]) { |n| n**2 }
```

c.

```ruby
def someMethod(array, &block)
  array.map{ yield }
end
```

d.

```ruby
def someMethod(array, &block)
  block.call(array)
end

p someMethod([1, 3, 5]) { |n| n**2 }
```

- Answer
    - B
    
    ```ruby
    def someMethod(array, &block)
      array.map{ |num| yield(num) }
    end
    ```
    
    This also works ^
    
    ```ruby
    def someMethod(array, &block)
      array.map(&block)
    end
    
    someProc = Proc.new { |n| n**2 }
    
    p someMethod([1, 3, 5], &someProc)
    ```
    
    **17. What does `self` refer to in this code?**
    
    **18. What is a block's arity?**
    
    a. Blocks don't enforce argument count so passing more or less arguments to a block 
    
    b. Like methods, blocks have strict arity and will raise an exception if arguments are omitted
    
    c. 1, because blocks can only accept one value at a time
    
    d. Only methods have arity
    
    **19. What will this calling `Potato.new.potato` return?**
    
    ```ruby
    module Ayto
      def potato
        'Pohtayto'
      end
    end
    
    module Ahto
      def potato
        'Pohtahto'
      end
    end
    
    class Potato
      include Ayto
      include Ahto
    end
    
    Potato.new.potato
    ```
    
    a. 
    
    ```ruby
    a. #<Potato:0x00000000029a73b8>
    ```
    
    b. 
    
    ```ruby
    "Pohtayto"
    ```
    
    c.
    
    ```ruby
    "Pohtahto"
    ```
    
    d. It will raise an exception
    
    - Answer
        - C. The method look-up chain is as follows: `[Potato, Ahto, Ayto, Object, Kernel, BasicObject]`. Since `Ahto` was mixed in last, it's the first place the `Potato` class looks for the `potato` method
    
    **20. Which of these is NOT a way to make a Proc?**
    
    a. Calling `to_proc` on a block:
    
    ```ruby
    my_proc = { |x| x**2 }.to_proc
    ```
    
    b. Calling the `new` method:
    
    ```ruby
    proc1 = Proc.new {|x| x**2 }
    ```
    
    c. Receiving a block of code as an argument using (&block):
    
    ```ruby
    def make_proc(&block)
      block
    end
    proc3 = make_proc {|x| x**2 }
    ```
    
    d. Using `Kernel#proc`:
    
    ```ruby
    proc2 = proc {|x| x**2 }
    ```
    
    - Answer
        
        A: a block isn't an object and doesn't have a `to_proc` method
        
    
    **21. Which of these is not an object?**
    
    a. An instance of a custom class
    
    b. Methods
    
    c. Blocks
    
    d. Classes
    
    **22. How do you access the letter 'g' in this array?**
    
    ```ruby
    array = [1, 2, [3, 4], [], { :alphabet => ['abcde', 'fg'] }, 'h']
    ```
    
    a.
    
    ```ruby
    array[:alphabet][1][1]
    ```
    
    b. 
    
    ```ruby
    array[4].values[1][1]
    ```
    
    c.
    
    ```ruby
    array[4][:alphabet][1][1]
    ```
    
    d.
    
    ```ruby
    array[4][:alphabet][1]
    ```
    
    - Answer
        
        C
        
    
    ```ruby
    arr = [["Mike",99], ["Zoolander",99],["Todd",230],["Max",99], ["Abby",13],["Mildred",99] ]
    p arr.sort_by { |name, score| [-score, name] }
    ```