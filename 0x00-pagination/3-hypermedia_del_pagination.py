#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieves a page of data with hypermedia metadata.

        Args:
            index (int, optional): The index of the first item in the page. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary containing the paginated data and hypermedia links.
        """
        assert type(index) == int and index >= 0, "index must be an integer greater than or equal to 0"
        assert type(page_size) == int and page_size > 0, "page_size must be an integer greater than 0"
        
        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index + page_size
        for i in range(index, next_index):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])
                
        hypermedia = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
        return hypermedia
