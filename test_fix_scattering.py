# -*- coding: utf-8 -*-
"""
Test of fix_Scattering

"""

import numpy as np
import plot_data
import fix_scattering
import read_data
import mock


# To initiate the object so that I can test the functions in the class
def get_object():
    directory_path = "Data/"
    sample_name = "sample_1"
    file_name = directory_path + sample_name + '.h5'
    data = read_data.read_data(file_name)
    
    return fix_scattering.FixScattering(data.copy(), file_name)

# Test of resize data, that it becomes the size I want
def test_resize_data():
   fs = get_object()
   assert isinstance(fs.data, np.ndarray)
   assert len(fs.data) == 900
   
# Test that I run all the functions once, when I intend to do so
def test_run():
    fs = get_object()
    with mock.patch.object(fs, "no_gaps") as no_gaps_mock:
        with mock.patch.object(fs, "beamstop") as beamstop_mock :
            with mock.patch.object(fs, "outliers") as outliers_mock:
                with mock.patch.object(fs, "pointsymmetry") as pointsymmetry_mock:
                    fs.run(True, True, True, True, False)
                    no_gaps_mock.assert_called_once()
                    beamstop_mock.assert_called_once()
                    outliers_mock.assert_called_once()
                    pointsymmetry_mock.assert_called_once()
   
# Test that the size doesn't change when I run the function
def test_no_gaps():
    fs = get_object()
    size_before = len(fs.data)
    fs.no_gaps()
    size_after = len(fs.data)
    assert size_before == size_after
  
# Test that the size doesn't change when I run the function and that the data actually changes
# Test that the data in the middle of the matrix is a mirror of the other
def test_beamstop():
    fs = get_object()
    size_before = len(fs.data)
    predata = fs.data.copy()
    fs.beamstop()
    assert np.array_equal(predata, fs.data) == False
    size_after = len(fs.data)
    assert size_before == size_after
    
    mid = len(fs.data) //2
    for i in range(0,mid):
        assert fs.data[mid-1, i] == fs.data[mid, -(i+1)]
        
# Test that the size doesn't change when I run the function and that the data actually changes
def test_outliers():
    fs = get_object()
    size_before = len(fs.data)
    predata = fs.data.copy()
    fs.outliers()
    assert np.array_equal(predata, fs.data) == False
    size_after = len(fs.data)
    assert size_before == size_after
    
    