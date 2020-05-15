# NumPy Arrays

import numpy as np

This section will go over examples of numpy arrays to manipulate numerical data. We'll go over some operations to create, modify, and access NumPy arrays. Note that these are in no way holistic and only represent the things that are mostly useful to CIS 105.

## Creating NumPy Arrays from Lists

We start with one-dimensional NumPy arrays. We can create these from lists and simply wrap `np.array` around the list.

some_list = [1, 2, 3]
some_array = np.array(some_list)
some_array

Or more succinctly:

some_array = np.array([1, 2, 3])
some_array


We can also create two-dimensional or three-dimensional NumPy arrays (though not needed for 105)

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
two_d_array

three_d_array = np.random.randint(10, size=(2, 3, 4))
three_d_array

## NumPy Array Attributes

We can access useful attributes of NumPy arrays through the `.` notation. Some useful attributes are `ndim`, `shape`, and `size`.

# ndim -> number of dimensions
three_d_array.ndim

# shape -> array dimensions
three_d_array.shape

# size -> total number of elements
three_d_array.size

```{tip}
For more attributes, you can explore for yourself by pressing `TAB` after typing in `{name of array}.` Use `?` to find out what each attribute does/is.
```

# for example
three_d_array.cumsum?

## Creating NumPy Arrays using `np.arange`

What if we wanted to create a large numeric array, say 1-2000? It wouldn't be very feasible for us to create this manually by typing out each element inside a list. We could, alternatively use `np.arange` to do this very easily!

some_large_array = np.arange(1, 2001, 1)
some_large_array

The syntax of `np.arange` is `np.arange(start, end, stepsize)`. Note that `start` is inclusive while `end` is exclusive. You may also omit the third argument `stepsize` for this situation as it defaults to `1`.

# 2 stepsize
np.arange(1, 10, 2)

# negative stepsize
np.arange(10, 1, -1)

## Array Indexing for One-Dimensional Arrays

If you are familiar with doing indexing with Python lists, then indexing in NumPy will feel very familiar.

some_array = np.array(["a", "b", "c", "d", "e"])
some_array

# first element
some_array[0]

# last element
some_array[-1]

# third element
some_array[2]

# second to fourth elements
some_array[1:4]

# first four elements
some_array[:4]

# excluding first four elements
some_array[4:]

We can also slice arrays in steps.. The syntax is

```
x[start:end:step]
```

# every second element
some_array[::2]

## Array Indexing for Multi-Dimensional Arrays

For multi-dimensional array, we can access elements using a comma-separated tuple of indices (not required for 105)

two_d_array

two_d_array[0, 0]

two_d_array[2, 0]

two_d_array[0, 2]

three_d_array

three_d_array[0, 0, 0]

## Array Concatenation

We sometimes might also want concatenate together two Numpy arrays. For this task, we can use `np.concatenate` to get the job done. Note that we can also concatenate multi-dimensional arrays but I won't be covering this here.

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.concatenate([x, y])
z