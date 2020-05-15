# Python Types

Every value in Python has a type. In this section I will introduce the most common, basic types that are built into Python. To check the type of a value, we can use the Python built-in `type()` function.

## Numbers

The first category of types I will go through in detail is Numbers. Integers, floating point numbers, and complex numbers fall under Python's number category. They are defined as `int`,
`float`, and `complex`. I personally have not used `complex` yet but have used `int` and `float` almost every day.

type(9642)

type(9642.0)

type(1+2j)

## Strings

Next we have strings. As you've seen in the previous section, a sequence of one or more characters enclosed within single quotes ‘, double quotes ", or even triple quotes ''' is considered as a String in Python. Any letter, number or symbol could be a part of the sting.

type('I like cats')

type("meow")

type('''meoooooow''')

type('9642')

## Booleans

Last but not least, we introduce booleans. A boolean is a data type that almost every programming language has. A Boolean in Python can have two values: `True` or `False`. These values are constants and can be used to assign or compare boolean values.

type(True)

type(False)

> Note that there are many other Python data types that you will encounter in our Pythonic journey! Don't be intimidated as there are many data types that even I haven't heard of. Besides `Numbers`, `Strings`, and `Booleans`, I will also going over container data types like `Lists`, `Tuples`, and `Dictionaries` that can contain `Booleans`, `Numbers`, and `Strings` soon.




```{toctree}
:hidden:
:titlesonly:


numbers
strings
booleans
type-casting
tuples-lists-dicts
```
