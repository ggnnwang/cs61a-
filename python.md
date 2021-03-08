# Python

## decoration

@trace

memorization

count_times

## frame and environments

frame represent environment by having a parent frame

frame have method lookup define

frame do not hold return values only bound names

### Dynamic Scope

Lexical scope: The parent of a frame is the environment in which a procedure was defined
Dynamic scope: The parent of a frame is the environment in which a procedure was called

## interpreter mechanism

```ditaa

         +-------------------------------- Loop -----------+
         |                                                 |
         |  +-------+   +--------+   +-------+   +-------+ |
Input ---+->| Lexer |-->| Parser |-->| Eval  |-->| Print |-+--> Output
         |  +-------+   +--------+   +-------+   +-------+ |
         |                              ^  |               |
         |                              |  v               |
         ^                           +-------+             v
         |                           | Apply |             |
         |    REPL                   +-------+             |
         +-------------------------------------------------+
```

## functional programming

All functions are pure functions
No re-assignment and no mutable data types
Name-value bindings are permanent
Advantages of functional programming:
• The value of an expression is independent of the order in which sub-expressions are
evaluated
• Sub-expressions can safely be evaluated in parallel or only on demand (lazily)
• Referential transparency: The value of an expression does not change when we substitute
one of its subexpression with the value of that subexpression 

## tail call

Tail Calls
A procedure call that has not yet returned is active. Some procedure calls are tail calls.
A Scheme interpreter should support an unbounded number of active tail calls using only a
constant amount of space.

A tail call is a call expression in a tail context:
• The **last** body sub-expression in a lambda expression
• Sub-expressions 2 & 3 in a (tail context if expression)
<https://www.youtube.com/watch?v=RJux-9helvA&list=PL6BsET-8jgYXdYh7kYQ-4HkO_EF_BItoz&index=5>
• All non-predicate sub-expressions in a tail context cond
• The last sub-expression in a tail context and, or, begin, or let