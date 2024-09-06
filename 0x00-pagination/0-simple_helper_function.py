#!/usr/bin/env python3
"""Module for index_range function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page of data.

    Args:
        page (int): The current page number (1-indexed).
            The first page is page 1.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
            for the range of items to return. The start index is inclusive,
            and the end index is exclusive, meaning
            the range is [start_index, end_index).
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return start_index, end_index
