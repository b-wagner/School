;Ben Wagner Homework 4

#lang racket

(display "1a.")
(newline)
(define (contains? list object)
  (if (equal? (car list) object)
      #t
      (if (equal? (cdr list) '())
          #f
          (contains? (cdr list) object))))
(contains? (list 1 2 3 4) 3)
(contains? (list 1 2 3 4) 5)

(define (contains1? list object)
  (accumulate (lambda (x y) (or x y))
              #f
              (map (lambda(x) (equal? object x)) list)))

(define (accumulate operator null list)
(if (null? list)
null
(operator (car list)
(accumulate operator null (cdr list)))))

(contains1? (list 1 2 3 4) 3)
(contains1? (list 1 2 3 4) 5)

(newline)

(display "1b.")
(newline)
(define (remove object list)
  (define (extract list1 list2 object)
    (if (null? list2)
        (reverse list1)
        (if (equal? (car list2) object)
            (extract list1 (cdr list2) object)
            (extract (cons (car list2) list1)(cdr list2) object))))
  (extract null list object))

(remove 3 (list 1 2 3 4))
(remove 3 (list 1 2 4 3 5 2 3))

(define (remove1 object list)
  (accumulate (lambda (item rest)
                (if (equal? object item)
                    rest
                (cons item rest)))
              null
              list))

(remove1 3 (list 1 2 3 4))
(remove1 7 (list 1 3 7 3 4 6 7 8 7))

(newline)

(display "2a.")
(newline)

(define (operator? object)
  (ormap (lambda (x) (equal? object x)) (list + - * /)))

(operator? +)
(operator? *)
(operator? 7)

(newline)

(display "2b.")
(newline)

(define (null-val operator)
  (car (cdr (assoc operator (list (list + 0)(list - 0)(list * 1)(list / 1))))))

(null-val +)
(null-val *)

(newline)

(display "2c.")
(newline)

(define (expression? object)
  (if (list? object)
      (if (operator? (car object))
          (andmap (lambda (x)
                    (if (expression? x)
                        #t
                        (number? x)))
                  (cdr object))
          #f)
      #f))

(expression? (list 1 + 2))
(expression? (list + 2 2))

(newline)

(display "2d.")
(newline)
(define (count-operators expr)
  (accumulate + 0 (map (lambda (x)
                         (if (expression? x)
                             (count-operators x)
                             (if (operator? x)
                                 1
                                 0)))
                       expr)))

(define (count-primitive-operands expr)
  (accumulate + 0 (map (lambda (x)
                         (if (expression? x)
                             (count-primitive-operands x)
                             (if (number? x)
                                 1
                                 0)))
                       expr)))

(define expr
   (list +
         1
         (list /
               2
               (list +
                     (list * 3 5)
                     1))
         (list - 0 4)))

(count-operators expr)
(count-primitive-operands expr)

(newline)

(display "2e.")
(newline)
(define (evaluate expr)
  (apply (car expr) (map (lambda (x)
                         (if (expression? x)
                             (evaluate x)
                             x))
                         (cdr expr))))

(evaluate expr)

(newline)
(display "Showing results as laid out at end of homework.")
(newline)

(operator? (car expr)) 
;Value: #t 
(number? (cadr expr)) 
;Value: #t
(expression? expr) 
;Value: #t 
(expression? (list 1 + 2)) 
;Value: #f
(expression? (list + 1)) 
;Value: #f 
(count-operators expr) 
;Value: 5
(count-primitive-operands expr) 
;Value: 7 
(evaluate expr) 
;Value: -23/8