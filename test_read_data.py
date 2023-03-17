# -*- coding: utf-8 -*-
"""
Test of the read_data function
"""

import read_data
import numpy as np
import pytest

# A test that makes sure that I get a matrix back when I run read_data 

@pytest.mark.parametrize("sample_name", ["sample_1", "sample_2", "sample_3", "sample_4", "sample_5"])
def test_read_data(sample_name):
    directory_path = "Data/"
    file_name = directory_path + sample_name + '.h5'
    read = read_data.read_data(file_name)
    assert isinstance(read, np.ndarray)
