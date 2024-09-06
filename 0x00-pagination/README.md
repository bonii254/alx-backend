# ALX Backend - Pagination Project

## Project Overview
This project introduces pagination concepts using Python. The goal is to handle large datasets by dividing them into smaller, manageable pages. The project involves implementing various pagination strategies such as basic slicing, hypermedia pagination, and handling deletion-resilient pagination.

## Key Concepts
- **Pagination**: Splitting a large dataset into smaller sections (pages).
- **Hypermedia Pagination**: Returning extra metadata (e.g., next/previous page info).
- **Deletion-resilient Pagination**: Ensuring consistency when items are deleted from the dataset.

## Tasks

### 0. Simple Helper Function
- **Task**: Write a function `index_range(page: int, page_size: int)` that returns a tuple `(start, end)` for pagination.
- **Key Points**: The function computes the start and end indices for any given page and page size. Page numbers are 1-indexed.
  
### 1. Simple Pagination
- **Task**: Create a class `Server` that reads a CSV dataset and implements a method `get_page` to return paginated data.
- **Key Points**: Use assertions to verify input and reuse `index_range` for correct pagination. Returns an empty list if inputs are out of range.

### 2. Hypermedia Pagination
- **Task**: Extend the `Server` class with a `get_hyper` method, returning additional metadata like next/previous page and total pages.
- **Key Points**: Implement hypermedia pagination to help clients navigate through large datasets.

### 3. Deletion-resilient Pagination
- **Task**: Implement a `get_hyper_index` method to handle pagination even when items are deleted from the dataset.
- **Key Points**: Ensure consistency in pagination by maintaining item order even if some rows are deleted between requests.

## Files
- `0-simple_helper_function.py`: Contains the `index_range` function.
- `1-simple_pagination.py`: Implements the `Server` class with basic pagination.
- `2-hypermedia_pagination.py`: Adds hypermedia pagination capabilities.
- `3-hypermedia_del_pagination.py`: Handles deletion-resilient pagination.

## Usage
1. Clone the repository.
2. Execute the main files provided for each task to test the functionality.
3. Use assertions to validate the input and ensure the correct handling of edge cases.
