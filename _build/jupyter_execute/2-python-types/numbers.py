import sys

# Numbers

As we've seen in the `Basic Math` section, we can use numbers to perform calculations. In this section, I will explain in detail the differences between the different types of numbers: `int`, `float`, and `complex` as well as some common methods we can use with them.

## Integers

Integers refer to `int` values in Python. They represent whole numbers (negative, zero, positive) and do not have a decimal component

1

0

-1

# Python3 ints can be some pretty large values

123812093819012381290380129830192830912312312313123712983719823719237

## Floats

Real numbers are called `float` values in Python. They can represent whole and fractional numbers but have limitations that I will discuss as you scroll down.

3.0

3.76

When an operation (e.g. addition) is performed on a `float` and a `int` value, the result will always be a `float` value. For operations with only `int` values, you typically get an `int` value as a result but division of two `int` values will always return a `float`.

3.0 + 3

3 / 3

### Limitations for Floats

>These limitation most likely won't affect any work done in CIS105 but I think they are good to know :)

1. There is an upperbound and lowerbound to a `float`'s number. You will rarely encounter this problem however
2. A `float` has limited precision (up to around 15 or 16 significant digits)
3. Combining `float` values with arithmetic operations can lead to small rounding errors

#### Limitation 1

# the maximum a float's value is ..
sys.float_info.max

> `e+308` means e^308 in mathematical terms.

1.797e+308

1.797e+309

If we go past this value, we will run into the value `inf` which is positive infinity. 

On the other hand, we could also have a very small number that is extremely close to 0. At a certain point, the number is going to be represented as `0.0`.

5e-324

5e-325

#### Limitation 2

If we do operations on floats with a large number of decimal places, the resulting `float` can be a tiny bit inprecise.

0.111111111111111111111111111119 - 0.111111111111111111111111111118

#### Limitation 3

# square root of 5
5 ** 0.5

(5**0.5) * (5**0.5)

>The product of two square roots of 5 should be 5 as well but it's not!

## Complex Numbers

Complex numbers are not used as much (in my opinion) so I won't go over them in much detail. In Python, you can make a number imaginary by putting `j` or `J` after it.

1j

1J

2j * 3j

If you ever need to deal with complex numbers, the standard module `cmath` has many functions that handle them nicely.

# e.g.
import cmath

x = complex(1,2)
y = complex(3,4)

x, y

x.real, x.imag

y.real, y.imag

## Numerical Methods

There are some basic numerical methods/functions that are built into Python without any imports. Here are some examples:

# minimum value
min(3, 3.14, 3.1415, 3.141596)

# maximum value
max(3, 3.14, 3.1415, 3.141596)

# absolute value
abs(-2)

# round
round(3.5), round(3.49)

There are also many methods/functions the `math` library that help you do mathematical calculations. Here are some more examples:

import math

# ceil (smallest integer greater than x)
math.ceil(1.2)

# floor (biggest integer smaller than x)
math.ceil(1.2)

# natural log & e
math.log(math.e)

# log base 10
math.log10(10)

# exponential e^x
math.exp(2)

# square root
math.sqrt(4)

For more useful functions in the `math` library, you can check them out [here](https://www.programiz.com/python-programming/modules/math)!