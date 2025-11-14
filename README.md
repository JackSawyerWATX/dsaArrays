# DSA Arrays

This repository contains Python implementations of basic array operations and sorting algorithms, focusing on data structures and algorithms (DSA) concepts. It includes both basic implementations and optimized versions to demonstrate algorithm improvements.

## Files

- `arrays.py`: Demonstrates basic array operations including finding minimum and maximum values, array length, and element access.
- `bubbleSort.py`: Implements the basic bubble sort algorithm with detailed comments explaining each step of the sorting process.
- `bubbleSortImprovement.py`: An optimized version of bubble sort that includes early termination when the array becomes sorted, improving performance on nearly sorted arrays.

## Requirements

- Python 3.x

## Usage

Run the scripts directly with Python:

```bash
python arrays.py
python bubbleSort.py
python bubbleSortImprovement.py
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

## Learning Objectives

- Understanding basic array operations in Python
- Implementing and understanding the bubble sort algorithm
- Algorithm optimization techniques (early termination)
- Time complexity analysis (bubble sort is O(n²) in worst case, O(n) in best case with optimization)
- Nested loop patterns in sorting algorithms
- Performance improvements through algorithmic enhancements