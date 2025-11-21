# DSA Arrays

This repository contains Python implementations of basic array operations and sorting algorithms, focusing on data structures and algorithms (DSA) concepts. It includes both basic implementations and optimized versions to demonstrate algorithm improvements.

## Files

- `arrays.py`: Demonstrates basic array operations including finding minimum and maximum values, array length, and element access.
- `binarySearch.py`: Implements the binary search algorithm for efficiently finding elements in a sorted array.
- `linearSearch.py`: Implements the linear search algorithm for finding elements in an unsorted array.
- `pythonQueueClass.py`: Implements a queue data structure as a Python class with methods for enqueue, dequeue, peek, and size operations.
- `pythonQueue.py`: Demonstrates basic queue operations using Python lists, showing enqueue, dequeue, and queue management.
- `queueUsingLinkedLists.py`: Implements a queue data structure using linked lists with Node class, providing efficient O(1) enqueue and dequeue operations.
- `stacks.py`: Demonstrates basic stack operations using Python lists, showing push, pop, peek, and stack management.
- `classStack.py`: Implements a stack data structure as a Python class with push, pop, and isEmpty methods.
- `bubbleSort.py`: Implements the basic bubble sort algorithm with detailed comments explaining each step of the sorting process.
- `bubbleSortImprovement.py`: An optimized version of bubble sort that includes early termination when the array becomes sorted, improving performance on nearly sorted arrays.
- `countingSort.py`: Implements the counting sort algorithm, a non-comparison based sorting method that uses frequency counting.
- `insertionSort.py`: Implements the basic insertion sort algorithm using pop/insert operations to build a sorted array.
- `improvedInsertionSort.py`: An optimized insertion sort implementation using in-place shifting and early termination for better performance.
- `mergeSort.py`: Implements the merge sort algorithm using divide-and-conquer with separate merge function.
- `mergeSortImplimentation.py`: Another implementation of merge sort demonstrating the algorithm with additional utility functions.
- `quickSort.py`: Implements the quick sort algorithm using divide-and-conquer approach with partitioning.
- `radixSort.py`: Implements the radix sort algorithm using digit-by-digit sorting with bucket distribution.
- `selectionSort.py`: Implements the selection sort algorithm, which finds the minimum element in each pass and places it at the beginning of the unsorted portion.
- `selectionSwapSort.py`: Another implementation of selection sort using direct element swapping instead of pop/insert operations.
- `simpleMergeSort.py`: A simplified implementation of merge sort with inlined merging logic and minimal variable names.
- `scatterplot.py`: Generates a scatterplot visualization using matplotlib and numpy, demonstrating data visualization concepts.
- `hashTable.py`: Implements a basic hash table data structure with add, contains, and hash functions.
- `HashSets.py`: Implements a hash set data structure with collision handling using bucket lists.

## Requirements

- Python 3.x

## Usage

Run the scripts directly with Python:

```bash
python arrays.py
python binarySearch.py
python linearSearch.py
python pythonQueueClass.py
python pythonQueue.py
python queueUsingLinkedLists.py
python stacks.py
python classStack.py
python bubbleSort.py
python bubbleSortImprovement.py
python countingSort.py
python insertionSort.py
python improvedInsertionSort.py
python mergeSort.py
python mergeSortImplimentation.py
python quickSort.py
python radixSort.py
python selectionSort.py
python selectionSwapSort.py
python simpleMergeSort.py
python scatterplot.py
python hashTable.py
python HashSets.py
```

### arrays.py
This script creates an array and performs basic operations:
- Prints the array
- Displays the length of the array
- Accesses the first element
- Finds and prints the minimum value
- Finds and prints the maximum value + 1

### binarySearch.py
This script demonstrates the binary search algorithm for efficient element lookup:
- Implements iterative binary search on a sorted array
- Uses divide-and-conquer approach to find target values quickly
- Returns the index of the target element if found, or -1 if not found
- Achieves O(log n) time complexity, much faster than linear search
- Requires the array to be sorted before performing the search
- Shows the importance of preconditions for algorithm correctness
- Demonstrates logarithmic time complexity concepts in search algorithms

### linearSearch.py
This script demonstrates the linear search algorithm for finding elements in arrays:
- Implements a simple sequential search that checks each element one by one
- Works on both sorted and unsorted arrays without any preprocessing
- Returns the index of the target element if found, or -1 if not found
- Has O(n) time complexity in the worst case, making it less efficient for large arrays
- Demonstrates the most straightforward search approach
- Shows the trade-off between simplicity and performance in search algorithms

### pythonQueueClass.py
This script demonstrates an object-oriented implementation of a queue data structure:
- Defines a Queue class with an internal list to store queue elements
- Implements enqueue method to add items to the end of the queue
- Provides dequeue method to remove and return the front item (FIFO)
- Includes peek method to view the front item without removing it
- Features isEmpty method to check if the queue contains no elements
- Offers size method to get the current number of items in the queue
- Demonstrates class-based design patterns for data structures

### pythonQueue.py
This script demonstrates basic queue operations using Python lists:
- Uses a simple list to implement FIFO (First In, First Out) queue behavior
- Shows enqueue operations by appending elements to the end of the list
- Demonstrates dequeue by removing elements from the front using pop(0)
- Illustrates peeking at the first element without removing it
- Shows how to check if the queue is empty using boolean conversion
- Demonstrates getting the queue size using the len() function
- Provides a procedural approach to queue operations without classes

### queueUsingLinkedLists.py
This script demonstrates a linked list implementation of a queue data structure:
- Defines a Node class to represent individual elements in the linked list
- Implements a Queue class using front and rear pointers for efficient operations
- Provides enqueue method to add elements to the back of the queue (O(1))
- Offers dequeue method to remove and return elements from the front (O(1))
- Includes peek method to view the front element without removing it
- Features isEmpty and size methods for queue status checking
- Demonstrates proper linked list pointer management and edge case handling
- Shows memory-efficient implementation without fixed-size limitations
- Illustrates fundamental data structure concepts with practical implementation

### stacks.py
This script demonstrates basic stack operations using Python lists:
- Uses a list to implement LIFO (Last In, First Out) stack behavior
- Shows push operations by appending elements to the end of the list
- Demonstrates pop operations by removing elements from the end of the list
- Illustrates peeking at the top element without removing it using negative indexing
- Shows how to check if the stack is empty using boolean conversion
- Demonstrates getting the stack size using the len() function
- Provides a procedural approach to stack operations using built-in list methods

### classStack.py
This script demonstrates an object-oriented implementation of a stack data structure:
- Defines a Stack class with an internal list to store stack elements
- Implements push method to add items to the top of the stack
- Provides pop method to remove and return the top item (LIFO)
- Includes isEmpty method to check if the stack contains no elements
- Demonstrates class-based design patterns for data structures
- Shows proper error handling for empty stack operations
- Illustrates encapsulation of stack operations within a class

### hashTable.py
This script demonstrates a basic hash table implementation:
- Defines a HashTable class with an array of buckets for storing key-value pairs
- Implements a simple hash function using character sum modulo array size
- Provides add method to insert key-value pairs into the hash table
- Includes contains method to check if a key exists in the hash table
- Demonstrates hash table creation, population, and display operations
- Shows basic collision handling through direct indexing (no chaining)
- Illustrates fundamental concepts of hash tables and hash functions
- Includes step-by-step comments explaining the program's execution flow

### HashSets.py
This script demonstrates a hash set implementation with collision handling:
- Defines a SimpleHashSet class with buckets implemented as lists
- Implements a hash function using character sum modulo bucket count
- Provides add method that prevents duplicate entries in buckets
- Includes contains method to check membership in the appropriate bucket
- Offers remove method to delete items from their buckets
- Features print_set method to display all buckets and their contents
- Demonstrates hash collisions where multiple items share the same bucket
- Shows set operations (add, contains, remove) with collision resolution
- Includes step-by-step comments explaining the program's execution flow

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

### countingSort.py
This script demonstrates the counting sort algorithm:
- A non-comparison based sorting algorithm that counts occurrences of each element
- Creates a frequency array to track how many times each value appears
- Rebuilds the array in sorted order using the frequency counts
- Performs in O(n + k) time where k is the range of input values
- Most efficient when the range of input values is small compared to the array size

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

### mergeSort.py
This script demonstrates the merge sort algorithm:
- Uses divide-and-conquer approach to recursively split the array into halves
- Employs a separate merge function to combine sorted subarrays
- Stable sort that maintains relative order of equal elements
- Consistently performs in O(n log n) time across all cases (worst, average, best)
- Requires O(n) additional space for the merging process
- Excellent for large datasets and external sorting scenarios

### simpleMergeSort.py
This script provides a simplified implementation of merge sort:
- Inlines the merging logic directly within the main function
- Uses concise variable names for a more compact implementation
- Maintains the same divide-and-conquer approach and performance characteristics
- Demonstrates how merge sort can be implemented with fewer lines of code
- Still achieves O(n log n) time complexity and O(n) space complexity
- Includes step-by-step comments explaining the algorithm's execution

### scatterplot.py
This script generates a scatterplot visualization:
- Uses matplotlib and numpy to create data visualizations
- Generates random data points for demonstration
- Creates a scatterplot showing the relationship between x and y values
- Saves the plot as a PNG image file for viewing
- Demonstrates basic data visualization concepts in Python

### quickSort.py
This script demonstrates the quick sort algorithm:
- Uses a divide-and-conquer approach for efficient sorting
- Selects a pivot element and partitions the array around it
- Recursively sorts the left and right subarrays
- Generally performs in O(n log n) time, much faster than O(n²) algorithms for large 
datasets
- In-place sorting with no additional memory requirements

### radixSort.py
This script demonstrates the radix sort algorithm:
- A non-comparison based sorting algorithm that processes numbers digit by digit
- Uses 10 buckets (0-9) to distribute elements based on each digit's value
- Processes digits from least significant (units place) to most significant
- Stable sort that maintains relative order of equal elements
- Performs in O(d × (n + b)) time where d is digits, n is elements, and b is buckets 
(10)
- Most efficient for sorting numbers with many digits but limited range

### selectionSort.py
This script demonstrates selection sort:
- Iterates through the array, finding the minimum element in each pass
- Swaps the minimum element with the first unsorted element
- Builds the sorted array from left to right
- Always performs O(n²) comparisons, making it predictable but less efficient than 
optimized bubble sort on nearly sorted data

### selectionSwapSort.py
This script shows an alternative selection sort implementation:
- Uses direct element swapping instead of pop/insert operations
- Finds the minimum element in each pass and swaps it directly with the current 
position
- Demonstrates different approaches to implementing the same sorting algorithm
- Maintains the same O(n²) time complexity as other selection sort variants

## Learning Objectives

- Understanding basic array operations in Python
- Implementing and understanding multiple sorting algorithms (bubble sort, insertion 
sort, selection sort, merge sort, quick sort, counting sort, and radix sort)
- Exploring different implementation approaches for the same algorithm
- Algorithm optimization techniques (early termination, in-place operations)
- Time complexity analysis (from O(n²) quadratic algorithms to O(n log n), O(n + k), 
and O(d × (n + b)) algorithms)
- Divide-and-conquer algorithmic patterns (merge sort, quick sort)
- Non-comparison based sorting algorithms (counting sort, radix sort)
- Stable vs unstable sorting algorithms
- Nested loop patterns in sorting algorithms
- Performance improvements through algorithmic enhancements
- Comparing different sorting approaches and their trade-offs
- Understanding hash table data structures and hash functions
- Basic collision handling concepts in hash tables
- Hash set implementations with bucket-based collision resolution