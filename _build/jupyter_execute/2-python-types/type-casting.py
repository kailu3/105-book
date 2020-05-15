# Type Casting


Users of Python are often drawn-in by its ease of use, one piece of which is dynamic typing. While a statically-typed language like Java or C requires each variable to be explicitly declared, a dynamically-typed language like Python skips this specification. As a simple demonstration:

```java
// java code
String a = "Hello!"
int b = 2
boolean c = true
```

As you can see, each variable needs to explicitly declared a type. In contrast, the equivilant in Python is as follows:

```python
# python code
a = 'Hello'
b = 2
c = True
```

In short, data tyes in Java or C are explicitly declared, while in Python the types are dynamically inferred. This means that in Python we can assign any kind of data to any variable:

```python
x = 4
x = 'four'
x = True
```

## Datatype Conversion

Sometimes, we may need to convert a variable from one datatype to another in Python. For instance, say we want to again print out a message with a variable. Normally, the `print` statement expects only `str` inputs, but what if your variable was an `int`?

x = 123
print('My password is ' + x)

> As you see, we get a `TypeError` informing that the datatype we need to pass in `must be str, not int`. Through further working with Python for data analysis, you will find that some of these error messages will be helpful in finding out what went wrong.

To convert `x` to a string, you can simply use the `str()` conversion function.

print('My password is ' + str(x))

I won't be going over all of the conversion operations since I feel that there are better resources out there to reference. However, some common type conversion operations are:

- `int()` converts type to integer
- `float()` converts type to float
- `str()` converts type to string
- `list()` converts  type to list
- `dict()` converts a tuple of order (key, value) into a dictionary

There are many more datatype conversion functions and you may reference them [here](https://www.geeksforgeeks.org/type-conversion-python/).