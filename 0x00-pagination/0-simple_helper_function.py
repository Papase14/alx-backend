#!/usr/bin/env python3
"""
Pagination helper function.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Retrieves the index range from a given page and page size.

    Parameters:
    - page (int): The current page number.
    - page_size (int): The number of items per page.

    Returns:
    - Tuple[int, int]: A tuple containing the start and end index of the page.
    """
    start = (page - 1) * page_size
    end = start + page_size

    return start, end
