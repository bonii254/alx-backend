#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple

"""Module for Server class."""


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        data = self.dataset()
        indicies = index_range(page, page_size)
        return data[indicies[0]:indicies[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page of data.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return start_index, end_index
