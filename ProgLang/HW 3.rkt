#lang racket
;Question 1a
(display "1a. ")
(define (compare p1 p2 n)
  (if (= (p1 n) (p2 n))
      #t
      #f))
(define (square x)
  (* x x))
(define (cube x)
  (* x x x))

(display "Testing (compare square cube 1). Expect true: ")
(compare square cube 1)
(display "Testing (compare square cube 3). Expect false: ")
(compare square cube 3)

;Question 1b
(display "1b. ")
(define (make-comparator p1 p2)
  
