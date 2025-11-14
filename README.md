# DSA Arrays

This repository contains Python implementations of basic array operations and sorting algorithms, focusing on data structures and algorithms (DSA) concepts. It includes both basic implementations and optimized versions to demonstrate algorithm improvements.

## Files

- `arrays.py`: Demonstrates basic array operations including finding minimum and maximum values, array length, and element access.
- `bubbleSort.py`: Implements the basic bubble sort algorithm with detailed comments explaining each step of the sorting process.
- `bubbleSortImprovement.py`: An optimized version of bubble sort that includes early termination when the array becomes sorted, improving performance on nearly sorted arrays.
- `selectionSort.py`: Implements the selection sort algorithm, which finds the minimum element in each pass and places it at the beginning of the unsorted portion.

## Requirements

- Python 3.x

## Usage

Run the scripts directly with Python:

```bash
python arrays.py
python bubbleSort.py
python bubbleSortImprovement.py
python selectionSort.py
```

### arrays.py
This script creates an array and performs basic operations:
- Prints the array
- Displays the length of the array
- Accesses the first element
- Finds and prints the minimum value
- Finds and prints the maximum value + 1

### bubbleSort.py
This script demonstrates bubble sort:
- Starts with an unsorted array
- Applies bubble sort to sort the array in ascending order
- Prints the sorted array and its length
- Includes detailed comments explaining the algorithm's logic

### bubbleSortImprovement.py
This script shows an optimized bubble sort implementation:
- Uses the same basic bubble sort logic
- Adds a flag to track if any swaps occurred in a pass
- Terminates early if no swaps are made, indicating the array is already sorted
- Demonstrates performance optimization techniques for sorting algorithms

### selectionSort.py
This script demonstrates selection sort:
- Iterates through the array, finding the minimum element in each pass
- Swaps the minimum element with the first unsorted element
- Builds the sorted array from left to right
- Always performs O(n²) comparisons, making it predictable but less efficient than optimized bubble sort on nearly sorted data

## Learning Objectives

- Understanding basic array operations in Python
- Implementing and understanding multiple sorting algorithms (bubble sort and selection sort)
- Algorithm optimization techniques (early termination)
- Time complexity analysis (both algorithms are O(n²) in worst case, with bubble sort potentially O(n) in best case)
- Nested loop patterns in sorting algorithms
- Performance improvements through algorithmic enhancements
- Comparing different sorting approaches and their trade-offs