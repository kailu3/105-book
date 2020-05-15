# Computation on Arrays

import numpy as np

The beauty of doing computation on NumPy arrays is that we can do calculations very quickly when we use built-in vectorized operations. Instead of iterating over the array and doing an operation at each iteration (e.g. using a for loop), it is much much faster to use a vectorized operation. This can be done by performing an operation on the array, which can be applied to each element. Essentially, this vectorized approach is designed to push the loop into the compiled layer that underlies NumPy, leading to much faster computation.

## For Loop vs. Vectorized Operation

Suppose we wanted to add 1 to each element in an array. The straightforward way to do it is to use a for loop.. 

some_array = np.arange(1, 1000)

def add_one(some_array):
    for i in np.arange(0, len(some_array)):
        some_array[i] = some_array[i] + 1
    return some_array

# For Loop
%timeit add_one(some_array)

If we used the vectorization inherent to NumPy arrays, we would get a much faster compute time.

some_array = np.arange(1, 1000)

# Vectorized Operation
%timeit some_array + 1

```{note}
$1.29 \mu s$  is a lot smaller than  $688 \mu s$! Since we get the same result from either method, it is preferable to avoid using for loops when we can use vectorized operations on NumPy arrays
```

## Array Arithmetic

Hopefully now I've convinced you to use vectorized operations in NumPy. They are, fortunately, very easy to use and feel very natural to use with the standard addition, subtraction, multiplication, and division operatiors in Python. Essentially, any operator on a NumPy array is applied on each element.

some_array = np.arange(9)
some_array

print("x + 3 ->", some_array + 3)
print("x - 3 ->", some_array - 3)
print("x * 2 ->", some_array * 2)
print("x / 2 ->", some_array / 2)
print("x // 2 ->", some_array // 2)
print("x ** 2 ->", some_array ** 2)
print("x % 2 ->", some_array % 2)

We can combine these operations together as well to do more complex operations to all elements of an array. For instance, suppose we wanted to approximate $\pi$ which is $$\frac{\pi^2}{6} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \space ...$$

# We first calculate the RHS elements
rhs = 1 / (np.arange(1, 1000)**2)

# Then we take the sum, multiply by 6, and take the sqrt
(sum(rhs)*6) ** (1/2)

## Wrappers in NumPy

Each of the standard operators (e.g. `+`, `-`, `*`) were simply convenient wrappers for specific functions built into NumPy. For example, the `+` operator is a wrapper for the `add` function in NumPy. Equivalently, we can use the syntax:

print("x + 3 ->", np.add(some_array, 3))
print("x - 3 ->", np.subtract(some_array, 3))
print("x * 2 ->", np.multiply(some_array, 2))
print("x / 2 ->", np.divide(some_array, 2))
print("x // 2 ->", np.floor_divide(some_array, 2))
print("x ** 2 ->", np.power(some_array, 2))
print("x % 2 ->", np.mod(some_array, 2))

## Aggregation Functions

Apart from doing arithmetic with NumPy arrays, we can also get summary statistics easily using built-in NumPy operations. When we're analyzing data, it is always useful to compute these to get a good sense of what our data looks like. Here are some of the most common NumPy operations:

| Aggregation | Description        |
|-------------|--------------------|
| `np.mean`     | mean               |
| `np.max`      | maximum            |
| `np.min`      | minimum            |
| `np.median`   | median             |
| `np.var`      | variance           |
| `np.std`     | standard deviation |

```{tip}
You can always type `np.` andd press `TAB` to see all the operations available!

```

### Example

To illustrate how we can use these operations, it's best to learn through an example. Suppose we collected some data on textbook prices and wanted to do some initial data exploration on this data.

tb = np.array([95,19.95,51.5,128.5,96,48.5,146.75,92,19.5,85.5,16.95,9.95,5.95,58.75,6.5,70.75,
               4.25,115.25,158,6.5,130.5,7,41.25,169.75,71.25,82.25,12.95,127,41.5,31])

print("Minimum price:", np.min(tb))
print("Maximum price:", np.max(tb))
print("Mean price:", np.mean(tb))
print("Median price:", np.mean(tb))
print("Variance:", np.var(tb))
print("Standard deviation:", np.std(tb))

```{note}
Pretty straightforward isn't it? :)
```