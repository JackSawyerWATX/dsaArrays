# DSA Arrays

This repository contains Python implementations of basic array operations and sorting algorithms, focusing on data structures and algorithms (DSA) concepts. It includes both basic implementations and optimized versions to demonstrate algorithm improvements.

## Files

- `arrays.py`: Demonstrates basic array operations including finding minimum and maximum values, array length, and element access.
- `bubbleSort.py`: Implements the basic bubble sort algorithm with detailed comments explaining each step of the sorting process.
- `bubbleSortImprovement.py`: An optimized version of bubble sort that includes early termination when the array becomes sorted, improving performance on nearly sorted arrays.
- `insertionSort.py`: Implements the basic insertion sort algorithm using pop/insert operations to build a sorted array.
- `improvedInsertionSort.py`: An optimized insertion sort implementation using in-place shifting and early termination for better performance.
- `quickSort.py`: Implements the quick sort algorithm using divide-and-conquer approach with partitioning.
- `selectionSort.py`: Implements the selection sort algorithm, which finds the minimum element in each pass and places it at the beginning of the unsorted portion.
- `selectionSwapSort.py`: Another implementation of selection sort using direct element swapping instead of pop/insert operations.

## Requirements

- Python 3.x

## Usage

Run the scripts directly with Python:

```bash
python arrays.py
python bubbleSort.py
python bubbleSortImprovement.py
python insertionSort.py
python improvedInsertionSort.py
python quickSort.py
python selectionSort.py
python selectionSwapSort.py
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

### insertionSort.py
This script demonstrates basic insertion sort:
- Builds the sorted array one element at a time
- For each element, finds its correct position in the already-sorted portion
- Uses pop and insert operations to move elements into place
- Efficient for small datasets and nearly sorted arrays (O(n) in best case)

### improvedInsertionSort.py
This script shows an optimized insertion sort implementation:
- Uses in-place shifting instead of pop/insert operations for better efficiency
- Implements early termination when the correct position is found
- Shifts larger elements to the right during the search phase
- Provides better performance than basic insertion sort, especially on partially sorted data

### quickSort.py
This script demonstrates the quick sort algorithm:
- Uses a divide-and-conquer approach for efficient sorting
- Selects a pivot element and partitions the array around it
- Recursively sorts the left and right subarrays
- Generally performs in O(n log n) time, much faster than O(n²) algorithms for large datasets
- In-place sorting with no additional memory requirements
- Note: Alternative implementations can choose the pivot as the middle element (halfway point) of the array for potentially better performance on certain data distributions

### selectionSort.py
This script demonstrates selection sort:
- Iterates through the array, finding the minimum element in each pass
- Swaps the minimum element with the first unsorted element
- Builds the sorted array from left to right
- Always performs O(n²) comparisons, making it predictable but less efficient than optimized bubble sort on nearly sorted data

### selectionSwapSort.py
This script shows an alternative selection sort implementation:
- Uses direct element swapping instead of pop/insert operations
- Finds the minimum element in each pass and swaps it directly with the current position
- Demonstrates different approaches to implementing the same sorting algorithm
- Maintains the same O(n²) time complexity as other selection sort variants

## Learning Objectives

- Understanding basic array operations in Python
- Implementing and understanding multiple sorting algorithms (bubble sort, insertion sort, selection sort, and quick sort)
- Exploring different implementation approaches for the same algorithm
- Algorithm optimization techniques (early termination, in-place operations)
- Time complexity analysis (from O(n²) quadratic algorithms to O(n log n) efficient algorithms)
- Divide-and-conquer algorithmic patterns
- Nested loop patterns in sorting algorithms
- Performance improvements through algorithmic enhancements
- Comparing different sorting approaches and their trade-offs