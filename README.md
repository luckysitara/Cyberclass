# Cyberclass


```markdown
# Python Functions and Arguments

This document provides a comprehensive guide to functions and their arguments in Python, including various types of arguments with detailed examples.

## Table of Contents
1. [What is a Function?](#what-is-a-function)
2. [Defining a Function](#defining-a-function)
3. [Function with Default Parameters](#function-with-default-parameters)
4. [Keyword Arguments](#keyword-arguments)
5. [Arbitrary Arguments](#arbitrary-arguments)
    - [*args](#args)
    - [**kwargs](#kwargs)
6. [Lambda Functions](#lambda-functions)
7. [Nested Functions](#nested-functions)
8. [First-Class Functions](#first-class-functions)
9. [Additional Examples](#additional-examples)
10. [Summary](#summary)

## What is a Function?

A function is a block of organized, reusable code that performs a single, related action. Functions provide better modularity for your application and a high degree of code reusability.

## Defining a Function

In Python, you define a function using the `def` keyword followed by the function name and parentheses. Here’s the syntax:

```python
def function_name(parameters):
    """
    Docstring: Describe your function here.
    """
    # function body
    # perform some tasks
    return result
```

### Example: A Simple Function

```python
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    """
    result = a + b
    return result

sum = add_numbers(3, 5)
print(sum)  # Output: 8
```

### Explanation

- `def`: Keyword used to define a function.
- `add_numbers`: Function name.
- `(a, b)`: Parameters passed to the function.
- `result = a + b`: The body of the function where the addition is performed.
- `return result`: The function returns the result.

## Function with Default Parameters

You can provide default values for parameters. If an argument for that parameter is not provided, the default value is used.

### Example: Function with Default Parameters

```python
def greet(name, message="Hello"):
    """
    Greets a person with a given message. Default message is "Hello".
    """
    return f"{message}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
```

### Explanation

- `message="Hello"`: Default parameter value for `message`.
- If `message` is not provided when calling the function, it defaults to "Hello".

## Keyword Arguments

Python allows you to call functions using keyword arguments, which makes the function call more readable and order-independent.

### Example: Keyword Arguments

```python
def describe_pet(animal_type, pet_name):
    """
    Describes a pet with its type and name.
    """
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Buddy")
describe_pet(pet_name="Whiskers", animal_type="cat")
```

### Explanation

- `animal_type="dog"` and `pet_name="Buddy"`: Keyword arguments.
- The order of keyword arguments does not matter.

## Arbitrary Arguments

### *args

`*args` allows you to pass a variable number of non-keyword arguments to a function.

### Example: *args

```python
def make_pizza(size, *toppings):
    """
    Makes a pizza of a given size with a list of toppings.
    """
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, "pepperoni", "mushrooms", "green peppers")
```

### Explanation

- `*toppings`: Collects additional arguments into a tuple.

### **kwargs

`**kwargs` allows you to pass a variable number of keyword arguments to a function.

### Example: **kwargs

```python
def build_profile(first, last, **user_info):
    """
    Builds a user profile with first name, last name, and additional user information.
    """
    profile = {"first_name": first, "last_name": last}
    profile.update(user_info)
    return profile

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)
```

### Explanation

- `**user_info`: Collects additional keyword arguments into a dictionary.

## Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword. They are useful for short, throwaway functions.

### Example: Lambda Functions

```python
square = lambda x: x ** 2
print(square(5))  # Output: 25

add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
```

### Explanation

- `lambda x: x ** 2`: A lambda function that squares its input.

## Nested Functions

You can define functions within other functions. These are known as nested functions or inner functions.

### Example: Nested Functions

```python
def outer_function(text):
    """
    Outer function that defines an inner function.
    """
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from inner function!")
```

### Explanation

- `inner_function` is defined inside `outer_function` and can access its local variables.

## First-Class Functions

In Python, functions are first-class citizens. This means you can pass functions as arguments to other functions, return them from other functions, and assign them to variables.

### Example: First-Class Functions

```python
def shout(text):
    """
    Returns the text in uppercase.
    """
    return text.upper()

def whisper(text):
    """
    Returns the text in lowercase.
    """
    return text.lower()

def greet(func):
    """
    Greets using the passed function.
    """
    message = func("Hello, World!")
    print(message)

greet(shout)  # Output: HELLO, WORLD!
greet(whisper)  # Output: hello, world!
```

### Explanation

- `greet` takes another function as an argument and calls it with the message "Hello, World!".

## Additional Examples

### Function with Multiple Return Values

A function can return multiple values as a tuple.

```python
def get_coordinates():
    """
    Returns a pair of coordinates.
    """
    x = 10
    y = 20
    return x, y

x, y = get_coordinates()
print(f"x: {x}, y: {y}")  # Output: x: 10, y: 20
```

### Recursive Function

A function can call itself. This is known as recursion.

```python
def factorial(n):
    """
    Returns the factorial of a number.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Function with Type Hints

Type hints help specify the expected types of function arguments and return values.

```python
def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    """
    return a + b

print(add_numbers(3, 5))  # Output: 8
```

## Summary

- **Defining functions:** Use the `def` keyword.
- **Arguments and parameters:** Specify inputs.
- **Default parameters:** Provide default values.
- **Keyword arguments:** Improve readability.
- **Arbitrary arguments:** Use `*args` and `**kwargs` for flexible inputs.
- **Lambda functions:** Define short, anonymous functions.
- **Nested functions:** Define functions within functions.
- **First-class functions:** Treat functions as variables.
- **Multiple return values:** Return multiple values as a tuple.
- **Recursive functions:** Functions that call themselves.
- **Type hints:** Specify expected types of arguments and return values.

Understanding functions and arguments will greatly enhance your ability to write efficient and reusable code in Python.
```

This README.md file includes detailed explanations, comprehensive examples for each type of argument, and additional examples to provide a deeper understanding of Python functions and their various features.
