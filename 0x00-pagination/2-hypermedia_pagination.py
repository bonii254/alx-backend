#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple, Dict

"""Module for Server class."""


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Iniatialize dataset attribute to None."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from a dataset according to the pagination paras."""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return dataset[
            start_index:end_index] if start_index < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """method that takes the same arguments (and defaults) as get_page and
        returns a dictionary containing key-value pairs:
        """

        data = self.get_page(page, page_size)
        page_size = len(data)
        total_entries = len(self.dataset())
        total_pages = math.ceil(total_entries / page_size if page_size else 1)
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page of data.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return start_index, end_index
