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
### Bash Conditionals




##In Bash, conditionals allow you to execute different blocks of code depending on whether a condition is true or false. Here’s a breakdown of how conditionals work in Bash.

#### 1. **Basic `if-else` Syntax**

The basic syntax for an `if-else` statement in Bash is:

```bash
if [ condition ]; then
    # code to run if condition is true
else
    # code to run if condition is false
fi
```

- `[ condition ]` is the test command, which evaluates the condition.
- `then` indicates the start of the block of code that will be executed if the condition is true.
- `else` (optional) indicates the block of code to execute if the condition is false.
- `fi` marks the end of the conditional statement.

#### 2. **Using `elif` for Multiple Conditions**

You can check multiple conditions using `elif` (short for "else if"):

```bash
if [ condition1 ]; then
    # code to run if condition1 is true
elif [ condition2 ]; then
    # code to run if condition2 is true
else
    # code to run if neither condition1 nor condition2 is true
fi
```

#### 3. **Common Conditional Expressions**

Here are some common expressions used in conditionals:

- **String Comparison**
  - `=`: Equality (e.g., `[ "$a" = "$b" ]`)
  - `!=`: Inequality (e.g., `[ "$a" != "$b" ]`)
  - `-z`: String is empty (e.g., `[ -z "$a" ]`)
  - `-n`: String is not empty (e.g., `[ -n "$a" ]`)

- **Numeric Comparison**
  - `-eq`: Equal (e.g., `[ "$a" -eq "$b" ]`)
  - `-ne`: Not equal (e.g., `[ "$a" -ne "$b" ]`)
  - `-lt`: Less than (e.g., `[ "$a" -lt "$b" ]`)
  - `-le`: Less than or equal (e.g., `[ "$a" -le "$b" ]`)
  - `-gt`: Greater than (e.g., `[ "$a" -gt "$b" ]`)
  - `-ge`: Greater than or equal (e.g., `[ "$a" -ge "$b" ]`)

- **File Conditions**
  - `-e file`: True if the file exists
  - `-d file`: True if the file is a directory
  - `-f file`: True if the file is a regular file (not a directory)
  - `-r file`: True if the file is readable
  - `-w file`: True if the file is writable
  - `-x file`: True if the file is executable

#### 4. **Logical Operators**

You can combine conditions using logical operators:

- **AND (`&&`)**
  ```bash
  if [ condition1 ] && [ condition2 ]; then
      # code to run if both condition1 and condition2 are true
  fi
  ```

- **OR (`||`)**
  ```bash
  if [ condition1 ] || [ condition2 ]; then
      # code to run if either condition1 or condition2 is true
  fi
  ```

#### 5. **Example: Simple Conditional**

```bash
#!/bin/bash

echo "Enter a number:"
read num

if [ "$num" -gt 10 ]; then
    echo "The number is greater than 10."
elif [ "$num" -eq 10 ]; then
    echo "The number is equal to 10."
else
    echo "The number is less than 10."
fi
```

#### 6. **Example: File Check**

```bash
#!/bin/bash

file="example.txt"

if [ -e "$file" ]; then
    echo "The file '$file' exists."
else
    echo "The file '$file' does not exist."
fi
```


### Bash Loops and Functions

#### 1. **Loops in Bash**

Loops allow you to repeat a block of code multiple times. Bash supports several types of loops:

##### **`for` Loop**

The `for` loop iterates over a list of items, executing the loop's body for each item.

**Syntax:**
```bash
for item in list; do
    # code to run for each item
done
```

**Example:**
```bash
#!/bin/bash

for i in 1 2 3 4 5; do
    echo "Iteration number $i"
done
```

You can also use a `for` loop with a range:

```bash
for i in {1..5}; do
    echo "Number $i"
done
```

Or with C-style syntax:

```bash
for ((i=1; i<=5; i++)); do
    echo "Counter $i"
done
```

##### **`while` Loop**

The `while` loop repeatedly executes the body as long as the condition is true.

**Syntax:**
```bash
while [ condition ]; do
    # code to run while the condition is true
done
```

**Example:**
```bash
#!/bin/bash

counter=1

while [ $counter -le 5 ]; do
    echo "Counter is at $counter"
    ((counter++))
done
```

##### **`until` Loop**

The `until` loop is similar to the `while` loop, but it continues running until the condition becomes true.

**Syntax:**
```bash
until [ condition ]; do
    # code to run while the condition is false
done
```

**Example:**
```bash
#!/bin/bash

counter=1

until [ $counter -gt 5 ]; do
    echo "Counter is at $counter"
    ((counter++))
done
```

#### 2. **Functions in Bash**

Functions in Bash allow you to group a set of commands into a single unit, which can be called multiple times throughout the script.

##### **Defining a Function**

**Syntax:**
```bash
function_name() {
    # code to run
}
```

**Example:**
```bash
#!/bin/bash

greet() {
    echo "Hello, $1!"
}

greet "Alice"
greet "Bob"
```

- `$1` is the first argument passed to the function, `$2` is the second, and so on.

##### **Returning Values from Functions**

Bash functions can return a value using the `return` keyword, but this return value is limited to an integer between 0 and 255, which is typically used as an exit status.

**Example:**
```bash
#!/bin/bash

calculate_sum() {
    local sum=$(( $1 + $2 ))
    echo $sum  # Output the result to use it later
}

result=$(calculate_sum 3 5)
echo "The sum is $result"
```

- `local` is used to define variables within the function's scope to avoid conflicts with variables outside the function.
- `$(...)` captures the output of the function to a variable.

##### **Function Example: Factorial**

```bash
#!/bin/bash

factorial() {
    if [ $1 -le 1 ]; then
        echo 1
    else
        local temp=$(( $1 - 1 ))
        local result=$(factorial $temp)
        echo $(( $1 * result ))
    fi
}

result=$(factorial 5)
echo "Factorial of 5 is $result"
```

This script defines a recursive function to calculate the factorial of a number.

### Summary

- **Loops** in Bash (`for`, `while`, and `until`) allow you to repeat code multiple times.
- **Functions** in Bash let you encapsulate reusable code, making your scripts more organized and modular.

These concepts are fundamental for writing efficient and maintainable Bash scripts.



### file that explains file conditions in Bash:


# File Conditions in Bash

This document provides an overview of various file conditions used in Bash scripting to test attributes of files and directories. These conditions are crucial for creating scripts that interact with the file system, allowing you to check if files exist, their permissions, types, and more.

## Table of Contents
- [Introduction](#introduction)
- [File Conditions Overview](#file-conditions-overview)
- [Common File Tests](#common-file-tests)
  - [Existence of a File or Directory](#existence-of-a-file-or-directory)
  - [Regular File](#regular-file)
  - [Directory](#directory)
  - [Readable File](#readable-file)
  - [Writable File](#writable-file)
  - [Executable File](#executable-file)
  - [Empty File](#empty-file)
  - [Symbolic Link](#symbolic-link)
  - [File Descriptor](#file-descriptor)
- [Combining Conditions](#combining-conditions)
- [Example Script](#example-script)
- [Resources](#resources)

## Introduction
Bash scripting allows you to perform a variety of file-related checks to determine the state or attributes of files and directories. These checks are often used in `if` statements to control the flow of a script based on the presence, type, or permissions of a file.

## File Conditions Overview
Bash provides several operators to test different file conditions. These operators are used within `[` (also known as `test`) brackets or within `[[ ]]` in an `if` statement.

## Common File Tests

### Existence of a File or Directory
- **`-e <file>`**: Checks if the file or directory exists.
  ```bash
  if [ -e myfile.txt ]; then
      echo "File exists."
  fi
  ```

### Regular File
- **`-f <file>`**: Checks if the file exists and is a regular file (not a directory or special file).
  ```bash
  if [ -f myfile.txt ]; then
      echo "It's a regular file."
  fi
  ```

### Directory
- **`-d <file>`**: Checks if the file exists and is a directory.
  ```bash
  if [ -d mydir ]; then
      echo "It's a directory."
  fi
  ```

### Readable File
- **`-r <file>`**: Checks if the file exists and is readable.
  ```bash
  if [ -r myfile.txt ]; then
      echo "File is readable."
  fi
  ```

### Writable File
- **`-w <file>`**: Checks if the file exists and is writable.
  ```bash
  if [ -w myfile.txt ]; then
      echo "File is writable."
  fi
  ```

### Executable File
- **`-x <file>`**: Checks if the file exists and is executable.
  ```bash
  if [ -x myscript.sh ]; then
      echo "File is executable."
  fi
  ```

### Empty File
- **`-s <file>`**: Checks if the file exists and is not empty.
  ```bash
  if [ -s myfile.txt ]; then
      echo "File is not empty."
  fi
  ```

### Symbolic Link
- **`-L <file>`**: Checks if the file exists and is a symbolic link.
  ```bash
  if [ -L mylink ]; then
      echo "It's a symbolic link."
  fi
  ```

### File Descriptor
- **`-t <fd>`**: Checks if the file descriptor is open and refers to a terminal.
  ```bash
  if [ -t 1 ]; then
      echo "File descriptor 1 is open."
  fi
  ```

## Combining Conditions
You can combine multiple file conditions using logical operators:
- **`-a`**: Logical AND (both conditions must be true).
- **`-o`**: Logical OR (at least one condition must be true).

Example:
```bash
if [ -f myfile.txt -a -r myfile.txt ]; then
    echo "File exists and is readable."
fi
```

## Example Script
```bash
#!/bin/bash

file="myfile.txt"
dir="mydir"

if [ -e $file ]; then
    if [ -f $file ]; then
        echo "$file exists and is a regular file."
    fi

    if [ -r $file ]; then
        echo "$file is readable."
    fi

    if [ -w $file ]; then
        echo "$file is writable."
    fi

    if [ -x $file ]; then
        echo "$file is executable."
    fi
else
    echo "$file does not exist."
fi

if [ -d $dir ]; then
    echo "$dir exists."
else
    echo "$dir does not exist."
fi
```

## Resources
- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs)
- [Bash Scripting Tutorial](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html)
