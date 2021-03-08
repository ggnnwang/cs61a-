# EXPRESSION

[TOC]

specifications
<https://inst.eecs.berkeley.edu/~cs61a/fa20/articles/scheme-spec.html>

Scheme programs consist of only expressions

1. atomic primitive expressions `1 2 3 + #t` 
1. call expressions  e.g,  `(define pi 3.14)`
    1. special forms     e.g, `(define (<name> <formal parameters>) <body>)`

没括号的，直接返回变量值
有括号的，要么是个函数，要么是宏，要么是特殊操作符。然后就执行这个函数/宏/特殊操作符就行了。宏跟特殊操作符虽然不是函数，但跟函数还挺像的。

**homoiconic**:
source code is data

(define xx )
Definitions are not expressions, and cannot appear in all places where an expression can occur. Moreover, a definition has no value.
<https://stackoverflow.com/questions/66463405/what-does-scheme-define-expression-return/66463846?noredirect=1#comment117514650_66463846>

Define binds a symbol to a value in the first frame of the current environment.

```scheme

scm> (define (a x) (+ 1 x))
a
scm> (symbol? a)
#f
scm> (procedure? a)
#t
scm> (symbol? (define (a x) (+ 1 x)))
#t
scm> ((eval (define (a x) (+ 1 x))) 2)
3
```

cannot call on a symbol, should evaluate it to its real value(which is a procedure)

---
why special?

special form follows its own special rules for execution, such as short-circuiting before evaluating all the operands. not the traditional 3 steps way(operators, operands left to right, return)
`scm> ((if (< 4 3) + -) 4 100) ;operator expression also evaluates`

define procedure expression is special because its operands are not evaluated at all! For example, `<body>` is not evaluated when a procedure is defined, but rather when it is called. `<name>`and the parameter names are all names that should not be evaluated when executing this define expression.`

---

```scheme
(and <e1> ... <en>) ; 
;Evaluate the tests in order, returning the first false value. If no test is false, return the last test. If no arguments are provided, return #t.


(or <e1> ... <en>) ;Evaluate the tests in order, returning the first true value. If no test is true and there are no more tests left, return #f.
(or (= 0 2) (= 1 1))
#t
(or (= 0 2) (= 1 2))
#f

scm> (and 25 32)
32
scm> (or 1 (/ 1 0)) ; Short-circuits
1

(not <e>)
;it shortcuts
```

---

## Pairs

 For historical reasons, pairs are created with the cons built-in function, and the elements of a pair are accessed with car and cdr:

 a list as being either
• the empty list, nil
• a pair whose second element is a list

```scheme
(define x (cons 1 2))
x
(car x)
1
(cdr x)
(2)

;return length
(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

;return which item
(define (getitem items n)
  (if (= n 0)
      (car items)
      (getitem (cdr items) (- n 1))))

scm> (cons 1 (cons 2 (cons 3 nil)))
(1 2 3)
scm> (list 1 (list 2 3) 4)
(1 (2 3) 4)

scm> (null? nil)                ; Checks if a value is the empty list
True
scm> (append '(1 2 3) '(4 5 6)) ; Concatenates two lists
(1 2 3 4 5 6)
scm> (length '(1 2 3 4 5))      ; Returns the number of elements in a list
5

```

The rule for displaying lists is very similar to that for the Link class from earlier
in the class’s str method. It prints out the elements in the linked list as if the
list has no nested structure

```

scm> (cons 1 (cons 2 (cons 3 nil)))
(1 2 3)

```

---

## Symbolic data

scheme can work with arbitrary symbols as data.

any expression that is not evaluated is said to be quoted.

a dog, which runs around and barks, and the word "dog" that is a linguistic construct for designating such things

symbol in Scheme is also a type of value. 
On the other hand, in Python, names only serve as expressions; a Python expression can never evaluate to a name. a scheme expression can evaluate to a symbol(a value)

---

## built-in functions

<https://inst.eecs.berkeley.edu/~cs61a/fa20/articles/scheme-builtins.html>

``` scheme

(eq? <a> <b>)
;If a and b are both numbers, booleans, symbols, or strings, return true if they are equivalent; false otherwise. (no pairs)

;;Otherwise, return true if a and b both refer to the same object in memory; false otherwise.

scm> (eq? '(1 2 3) '(1 2 3)) ;compare them if refer to the same object
False
scm> (define x '(1 2 3))
scm> (eq? x x)
True


(equal? <a> <b>)
;Returns true if a and b are equivalent. For two pairs, they are equivalent if their cars are equivalent and their cdrs are equivalent.

scm> (equal? '(1 2 3) '(1 2 3))
True

;
```

* = can only be used for comparing numbers.
* eq? behaves like == in Python for comparing two non-pairs (numbers, booleans,
etc.). Otherwise, eq? behaves like is in Python.
* equal? compares pairs by determining if their cars are equal? and their cdrs
are equal?(that is, they have the same contents). Otherwise, equal? behaves
like eq?.

examples:

```scheme

(define (no-repeats lst)
  (cond
    ((null? lst) nil)
    (else (append
            (list (car lst)) 
            (no-repeats (filter (lambda (x) (not (= x (car lst)))) (cdr lst)))
          )
    )
  )
)
;(no-repeats (list 5 4 5 4 2 2)) evaluates to (5 4 2).

;5 + non(4422) ；  5 4 non(22) ; 5 4 2 
;(filter <pred> <lst>)
; (filter (lambda (x) (not (= x (car lst)))) (cdr lst))

; (list 5 4 5 4 2 2)

```

`(filter <pred> <lst>)`
Returns a list consisting of only the elements of lst that return true when called on pred (a one-argument procedure).

`(reduce <combiner> <lst>)`
Returns the result of sequentially combining each element in lst using combiner (a two-argument procedure). reduce works from left-to-right, with the existing combined value passed as the first argument and the new value as the second argument. lst must contain at least one item

`(map <proc> <lst>)`
Returns a list constructed by calling proc (a one-argument procedure) on each item in lst.

### Mutation

`(set-car! <pair> <value>)`
Sets the car of pair to value. pair must be a pair.

`(set-cdr! <pair> <value>)`
Sets the cdr of pair to value. pair must be a pair.

