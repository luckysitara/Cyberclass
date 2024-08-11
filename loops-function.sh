### Bash Conditionals

In Bash, conditionals allow you to execute different blocks of code depending on whether a condition is true or false. Here’s a breakdown of how conditionals work in Bash.

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
