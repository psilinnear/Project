# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:58:07 2023

@author: rensmo_l
"""

def read_data(file_name):
    
    """
    A function that reads data from hdf5-files
    
    Parameters
    ----------
    file_name : the file_name of the hdf5-file

    """
    
    import h5py
    import numpy as np
    sample = h5py.File(file_name,'r')
    # In the hdf5-file I get data from a line of experiments, I just want to explore one point in the middle
    # From how I conducted my experiments I know this point is the 30:th
    point_scan = 30

    # There is a lot of information within the file, I only want the scattering pattern 
    data_slice = sample["entry/data/data"][point_scan,:,:]
    # The data is rotated compared to how I saw it during the experiments. I want it rotated, so I recognize it
    data = np.rot90(np.array(data_slice))
    return data