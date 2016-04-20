#lang racket
;Ben Wagner
;Homework 1
;Note - individual questions are commented and 
;can be un-commented and ran just fine.

;Question 1
;(define (kilometers kph)
;  (* kph 0.6215))
;(define (miles mph)
;  (* mph 1.6215))

;Question 2
;a
;(define (foo x y) 
;   (+ x y (- x)))
;(foo (- 2) 4)

;b
;(define (a b c d)
;   (e b c d))
;(define f +) 
;(define e f)
;(a (+ 3 2) (* 4 5) 3)

;c
;(define (a b c d)
;   ((e (f b)) c d))
;(define (e a) 
;   a)
;(define (f a)
;   (if (positive? a) 
;       +
;       -))
;(a 1 (+ 2 3) 4)

;Question 3
;(define (baz n)
;  (define (foo a)
;   (* a (+ a 2)))
;(define (bar a b)
;   (if (= a 14)
;       b
;       (bar (+ a 1) (+ (foo a) b))))
;   (bar 3 n))

;Question 4
(define (sum-range from to [sum 0])
  (if (= from to)
      sum
      (if (<= to from)
      (sum-range to from)
      (sum-range (+ from 1) to (+ sum from)))))
