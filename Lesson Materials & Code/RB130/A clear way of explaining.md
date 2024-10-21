# A clear way of explaining &

Course: RB130
Concepts: &:sym shortcut, Procs, blocks, to_proc
Last Edited: June 6, 2022 3:56 PM

### Description

We can think of `&` as doing 3 (or maybe 2-1/2) different, but related things. What it does depends on where it is and what comes after it.

1. Can be in method definition, prepended on a parameter name
    1. Here, `&` will take a block, convert it into a `Proc` and assign it to the parameter name
2. Can be in method invocation, prepended on an argument
    1. Here it takes a `Proc` and converts it to a block to be passed as an argument
    2. But, if what comes after is NOT a `Proc` it will call `to_proc` on that object and then proceed with converting it to a block to be passed

```
# method implementation
def say(words)
  yield if block_given?
  puts "> " + words
end

# method invocation
say("hi there") do
  system 'clear'
end
```
