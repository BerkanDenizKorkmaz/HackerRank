#lang racket
(define n (read))
(define (f n)
  (for ([i n])
    (displayln "Hello World")))
(f n)
