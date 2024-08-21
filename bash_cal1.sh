#!/bin/bash

# Function to display options
display_menu() {
  echo "Welcome to the Simple Bash Calculator!"
  echo "You can perform the following operations:"
  echo "1) Addition"
  echo "2) Subtraction"
  echo "3) Multiplication"
  echo
}

# Function to add all arguments
addition() {
  local sum=0
  for num in "$@"; do
    sum=$((sum + num))
  done
  echo "The sum of the numbers is: $sum"
}

# Function to subtract all arguments
subtraction() {
  local result=$1
  shift
  for num in "$@"; do
    result=$((result - num))
  done
  echo "The result of subtraction is: $result"
}

# Function to multiply all arguments
multiplication() {
  local result=1
  for num in "$@"; do
    result=$((result * num))
  done
  echo "The result of multiplication is: $result"
}

# Display the menu
display_menu

# Prompt the user to choose an operation
read -p "Please choose an operation (1/2/3): " operation

# Ask for numbers for the operation
read -p "Enter the numbers separated by space: " -a numbers

# Perform the chosen operation using if conditionals
if [ "$operation" -eq 1 ]; then
  addition "${numbers[@]}"
elif [ "$operation" -eq 2 ]; then
  subtraction "${numbers[@]}"
elif [ "$operation" -eq 3 ]; then
  multiplication "${numbers[@]}"
else
  echo "Invalid choice, please run the script again and choose a valid option."
fi
