# Call Expressions

>A call expression is an expression that involves a function call. A call expression invokes a function and evaluates to the function's return value. 

From [https://www.ocf.berkeley.edu/~shidi/cs61a/wiki/Expression](https://www.ocf.berkeley.edu/~shidi/cs61a/wiki/Expression)

There are many built-in call expressions in Python in which we can use. A good example of such function is the `print` function which we introduced earlier. There are also other useful functions. We usually use these functions with the name of the function first and wrap our argument inside parentheses.

len('String')

abs(-123)

str(456)

You can find other built-in functions here: [https://docs.python.org/3.6/library/functions.html](https://docs.python.org/3.6/library/functions.html)

However, most functions in Python are not built into the Python language and are instead stored in modules. You can think of modules as a code library or collection containing functions you want to use in your program. We typically access Python libraries/modules by using the `import` statement. For example:

import math

Now if we type `math.` and press `TAB`, we can see a collection of functions we have access to now. 

From experience, using libraries in Python can you save a lot of time. Nowadays, there is a Python library for pretty much anything you can think of. In terms of practicality, it's usually better to use the library function instead of trying to reinvent the wheel by writing your own version of it. However, writing your own functions from scratch is good way to practice and learn the Python concepts starting out.

Now say we want to take the natural log of `420` and we find that `math.log` might be the function we are looking for. To learn more about this function, we can place a `?` after its name which will bring up a description of the function in the output.

math.log?

> Perfect! We see that `math.log` defaults to the natural logarithm.

math.log(420)

What if we wanted a `base 10` logarithm of `420`? We could simply add the second argument to the call that specifies the `base`.

math.log(420, 10)

## Aliases

In further chapters you will see that we are able to import libraries under aliases. For instance, the most common libraries we will be using in this book are `numpy` and `pandas`. By convention, they are imported under `np` and `pd`.

import numpy as np
import pandas as pd

You can pretty much import any library under any name though I would not recommend it. There are some standards in place and you should follow them.

# Bad example
import pandas as pandas_are_cool