#!/bin/bash

# Function to add all arguments
addition() {
  local sum=$(( $* ))
  echo "The sum of the numbers is: $sum"
}

# Function to subtract all arguments
subtraction() {
  local initial=$1
  shift
  # Build the subtraction expression using all remaining arguments
  local expr="$initial"
  while [ $# -gt 0 ]; do
    expr="$expr - $1"
    shift
  done
  local result=$(( expr ))
  echo "The result of subtraction is: $result"
}

# Function to multiply all arguments
multiplication() {
  local product=1
  product=$(( product * $* ))
  echo "The product of the numbers is: $product"
}

# Display the menu
echo "Welcome to the Simple Bash Calculator!"
echo "You can perform the following operations:"
echo "1) Addition"
echo "2) Subtraction"
echo "3) Multiplication"
echo

# Prompt the user to choose an operation
read -p "Please choose an operation (1/2/3): " operation

# Prompt for numbers
if [ "$operation" -eq 1 ]; then
  read -p "Enter the numbers separated by space: " -a numbers
  addition "${numbers[@]}"
elif [ "$operation" -eq 2 ]; then
  read -p "Enter the numbers separated by space: " -a numbers
  subtraction "${numbers[@]}"
elif [ "$operation" -eq 3 ]; then
  read -p "Enter the numbers separated by space: " -a numbers
  multiplication "${numbers[@]}"
else
  echo "Invalid choice, please run the script again and choose a valid option."
fi
