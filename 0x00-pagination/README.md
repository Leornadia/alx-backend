# 0x00. Pagination

This project focuses on implementing pagination in Python using a dataset of popular baby names. The goal is to understand how to paginate datasets with simple page and page_size parameters, add hypermedia metadata to paginated data, and create pagination that is resilient to deletions.

## Learning Objectives

By the end of this project, you should be able to:
- Paginate a dataset with simple page and page_size parameters.
- Paginate a dataset with hypermedia metadata.
- Implement deletion-resilient pagination.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- The code should use the `pycodestyle` style (version 2.5.*).
- All modules should have documentation.
- All functions should have documentation.
- All functions and coroutines must be type-annotated.

## Dataset

The dataset used for this project is `Popular_Baby_Names.csv`, which contains popular baby names along with other related data.

## Project Structure

The project consists of the following Python scripts:

- `pagination.py`: Contains functions for loading the dataset, paginating it with simple page and page_size parameters, paginating with hypermedia metadata, and creating deletion-resilient pagination.
- `Popular_Baby_Names.csv`: The dataset used for pagination.
- `README.md`: This file, which explains the project.

## Functions

### `load_dataset() -> List[List[str]]`
Loads the dataset from the CSV file and returns it as a list of lists, skipping the header row.

### `get_page(dataset: List[List[str]], page: int = 1, page_size: int = 10) -> List[List[str]]`
Returns a specific page of data from the dataset. The function takes the dataset, a page number, and a page size as parameters.

### `get_hyper(dataset: List[List[str]], page: int = 1, page_size: int = 10) -> dict`
Returns a page of data along with hypermedia metadata, including the current page, next page, previous page, and total pages.

### `get_deletion_resilient_page(dataset: List[List[str]], page: int = 1, page_size: int = 10) -> List[List[str]]`
Returns a deletion-resilient page of data, filtering out any deleted rows before paginating.

## Usage

To run the scripts, use the following commands:

```bash
# Ensure the script is executable
chmod +x pagination.py

# Run the script
./pagination.py

