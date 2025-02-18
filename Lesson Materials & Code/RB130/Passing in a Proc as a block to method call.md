# Passing in a Proc as a block to method call

Course: RB130
Concepts: &:sym shortcut, Procs, to_proc
Last Edited: June 6, 2022 3:56 PM

### Description

Tricky problem to test understanding of `&:to_s` shorthand notation and Procs.

### Code

```ruby
# Problem
def call_this
	yield(2)
end

# How to get the following return values with modifying the method invocation nor the method definition
call_this(&to_s) # => returns 2
call_this(&to_i) # => returns "2"

# Solution
to_s = Proc.new { |num| num.to_i } # Define these before the method invocations
to_i = Proc.new { |num| num.to_s }
```