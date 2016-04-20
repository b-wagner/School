#lang racket
;Ben Wagner CSIT 408 Homework 2
;Finally done!

;Question 1a
;(define (reverse-digits x)
;  (define (reverse y z)
;    (if (= y 0)
;        z
;        (reverse(floor(quotient y 10)) (+(* z 10)(modulo y 10)))))
;    (reverse x 0))

;Question 1b
;(define (same-digits? a b)
;  (define (adjust y z)
;    (if (= y 0)
;         z
;     (adjust (floor (quotient y 10))(+ z (* 1(expt 10(modulo y 10)))))))
;    (if (= (adjust a 0)(adjust b 0))
;        #t
;        #f))

;Question 2
;(define (gen x y)
;  (take(drop(digits(* x x)) y) y))

;  (define (digits n . args)
;  (let ((b (if (null? args) 10 (car args))))
;    (let loop ((n n) (d '()))
;      (if (zero? n) d
;          (loop (quotient n b)
;                (cons (modulo n b) d))))))

;Question 3
(define (mersenne? n predicate)
  (if (predicate n)
      (if (predicate (-(expt 2 n) 1))
         (display n)
         (mersenne? (+ n 1) predicate))
      (mersenne? (+ n 1) predicate)))

(define (smallest-divisor n)
  (find-divisor n 2))
(define (find-divisor n test-divisor)
  (cond ((> (* test-divisor) n) n)
        (( divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))))
(define (divides? a b)
  (= (remainder b a) 0))
(define (prime? n)
  (= n (smallest-divisor n)))