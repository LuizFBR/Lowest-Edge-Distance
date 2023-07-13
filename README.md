# Lowest-Edge-Distance
An algorithm that calculates the lowest edge distance between pairs of edges.

Implemented functions are in led.py file.

## Dependencies

Python packages `sympy` is used, to install just do `pip install sympy`

## Running

To run the tests, just run python3 ./led  on the same folder where ./led and the tests (files t1,t2,... ) are located.

Test t3 has a t3.png image file illustrating the problem.

## Tests

The first tests `t1` and `t2` are just here to test edge cases (low number of edges). The test `t3` simulates walls in a real housing complex. The tests `t4`, `t5`, and `t6` are just more numerically complex versions of `t3`.

`t5` and `t6` are currently returning very small distances as solutions (lower than $10^{-12}$) which suggests the code must be tweaked further in order to decrease tolerance (error) or that SymPy cannot handle too many decimal places.
