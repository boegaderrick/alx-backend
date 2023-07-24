#!/usr/bin/env python3
"""This module contains a page Server class"""
import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


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
            This method returns a page with a range specified by the
            'page' and 'page_size' parameters
        """
        assert all(type(i) is int and i > 0 for i in [page, page_size])
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
