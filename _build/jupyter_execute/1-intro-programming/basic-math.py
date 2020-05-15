# Basic Math Operations

Let's first try some simple commands. In this section, we learn to use Python as a calculator to perform mathematical operations like addition, subtraction, multiplication, and division. The examples so far are basic and I would recommend playing around with some examples on your own.

# Addition
2 + 2

# Subtraction
4 - 1

# Multiplication
2 * 3

# Division
5 / 2

# Integer Division
5 // 2

# Exponents
4 ** 3

# Modulo -> remainder computation
123 % 2

*Here is a quick summary of common operations used:*


| Operator	    |          Description                   | Syntax  | Example | Result
|---------------|----------------------------------------|---------|---------|-------
| +             | Addition                               | x + y   | 2 + 2   | 4
| -             | Subtraction                            | x - y   | 5 - 3   | 2
| *             | Multiplication                         | x * y   | 3 * 4   | 12
| /             | Division (float)                       | x / y   | 3 / 4   | 0.75
| //            | Division (floor)                       | x // y  | 3 // 4  | 0
| %             | Modulus (remainder)                    | x % y   | 5 % 3   | 2
| **            | Exponential                            | x ** y  | 2 ** 3  | 8

>Another thing to note is that Python expressions obey the rules of precedence as we are familar with. We can use parentheses to group together expressions that we want to be evaluated in higher priority:

2 + 2 * (2 - 2) ** 2 / 4