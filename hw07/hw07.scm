(define (filter-lst fn lst)
  (cond 
    ((null? lst) nil)
    ((eq? (fn (car lst)) #t) (append (list (car lst)) (filter-lst fn (cdr lst))))
    ((eq? (fn (car lst)) #f) (filter-lst fn (cdr lst)))
  )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)




(define (interleave first second)
  (cond
    ((null? first) second)
    ((null? second) first)
    (else 
      (append (list (car first) (car second)) (interleave (cdr first) (cdr second)))   
    )
  )
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)

(interleave (list 2 4) (list 1 3 5))
; expect (2 1 4 3 5)

; (1 3 5) (2 4 6)
; (1 2) + (3 5)(4 6)
; (1 2) + (3 4) + (5)(6)

; (1 2 3 ^ 5) (4 6)
; (1 2 3 4 5 ^) (6)

; (2 1 4 ^) (3 5)

; (1 2 3 ^ 5) (4)



(define (accumulate combiner start n term)
  (define 
    (acc comb a fn)
    (cond
      ((= 1 a) (fn 1))
      (else (comb (fn a) (acc comb (- a 1) fn)))
    )
  )
  (combiner 
    start
    (acc combiner n term)
  )
)




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