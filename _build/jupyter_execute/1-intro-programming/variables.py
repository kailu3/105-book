# Python Variables

Using variables is essential to all programming languages. I like to think of a variable as a nametag attached to an object. Variables are essentially reserved memory locations to store values. In Python, variables do not need to be declared or defined in advance like other programming languages such as Java. To create a variable, we just assign it a value and then can start using it. Assignment is done with a single equals sign `=`

colour_of_car = "red"

> This is read as `colour_of_car` is assigned the string "red". Once this is done, `colour_of_car` can be used in any statement or expression, and its value will be substituted.

print(colour_of_car)

Python also supports multiple assignment, which allows you to assign values to multiple variables in one line.

x, y, z = 1, 2, 3
print(x + y + z)

You can also assign the same value to multiple variables in one line. I don't use this one often though!

x = y = z = "cat"
print(x)
print(y)
print(z)

## Variable Names

Here are some rules for naming your variables:
- A variable name must start with a letter or the _ character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
- Variable names are case-sensitive (cat, Cat, and caT are three different variables)

cat = "meow"
# mistyping variable names is a very common error!

```{warning}
Here, `print(Cat)` would not work since our variable name is `cat`.

```

```{tip}
When typing your variable you can press `TAB` to bring up a drop down of variable names to select from or to autocomplete your variable name.
```

## Passing Variables to Strings

You may want to print a message with a variable at times to help with debugging. Some ways to do this are

apple = 12
print('Apples are ' + str(apple) + ' dollars a dozen')

```{note}
When you concatenate Strings using `+`, all components must be of String Type. Here, I used the `str()` function to cast the integer 12 into the String `12`. More on types and casting later.
```

Here is another way of doing String concatenation that does not require 12 to be a String.

print('Apples are', apple, 'dollars a dozen')

Using `.format` to pass variables to Strings

print('apples are {} dollars a dozen'.format(apple))

In Python 3.6, we can also use `f-strings`. This is another way of formatting
strings that I am trying to use more frequently. So far it's the cleanest way in my opinion to embed variables into Strings. Here's a simple example:

print(f'apples are {apple} dollars a dozen')

You can also do inline arithmetic with this formatting approach! Pretty cool!

a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')

```{tip}
As you see, there are multiple ways to pass variables to a String in Python. Similarly, there are many different ways
to do most things in Python. These snippets in this book are just how I use Python for tasks I want to complete. You should not be limited by them!
```