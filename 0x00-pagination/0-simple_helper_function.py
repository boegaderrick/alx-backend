#!/usr/bin/env python3
"""This module contains a pagination helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        This function calculates start and end indices based on
        'page' and 'page_size'
    """
    return (page_size * (page - 1), page_size * page)
