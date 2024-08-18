#!/usr/bin/env python3
"""
This module provides a function for calculating the index range for pagination.
"""

from typing import Tuple, List, Dict, Any  # Import Dict here


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data.

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        assert type(page) == int and page > 0, "page must be an integer greater than 0"
        assert type(page_size) == int and page_size > 0, "page_size must be an integer greater than 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if end_index > len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieves a page of data with hypermedia metadata.

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary containing the paginated data and hypermedia links.
        """
        assert type(page) == int and page > 0, "page must be an integer greater than 0"
        assert type(page_size) == int and page_size > 0, "page_size must be an integer greater than 0"

        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)

        hypermedia = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return hypermedia
