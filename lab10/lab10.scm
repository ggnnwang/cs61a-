(define (over-or-under num1 num2)
  (if (> num1 num2) 
    1
    (if (< num1 num2) -1 0)
  )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0



; (define 
;   (make-adder num)
;   (begin
;     (define (foo inc) (+ inc num))
;     foo
;   )
; )

; (define 
;   (make-adder num)
;   (lambda (inc) (+ inc num))
; )

(define 
  (make-adder num)
    (eval(define (foo inc) (+ inc num)))
)











;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13



(define (composed f g)
  (lambda (x)
  (f (g x)))
)


; (define lst
;   (cons (cons 1 nil) (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil) )))
; )
(define lst
 '((1) 2 (3 4) 5)
)




(define (remove item lst)

  (cond
    ((null? lst) nil)
    (else (if 
            (= (car lst) item) 
            (remove item (cdr lst))
            (append (list (car lst)) (remove item (cdr lst))  )
          )
    )
  )
)
    


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)



;   (if 
;     (= (cdr lst) nil) 

;     (if (= (car lst) item) (nil) (lst) )

;     (if 
;       (= (car lst) item) 
;       (remove (cdr lst))
;       (append (car lst) (remove (cdr lst)))
;     )
;   )

; )


; scm> (cond
;         ((> x 0) 'positive)
;         ((< x 0) 'negative)
;         (else 'zero))

; (if 
;   (= (car lst) item) 
;   (remove (cdr lst))
;   (append (car lst) (remove (cdr lst)))
; )
  ; (append '(1 2 3) '(4 5 6))



; (if 
;   (= (cdr lst) nil) 
;   (if (= (car lst) item) (nil) (lst) )
;   (
;   if 
;     (= (car lst) item) 
;     (remove (cdr lst))
;     (append (car lst) (remove (cdr lst)))
;   )
; )