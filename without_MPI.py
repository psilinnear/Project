# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:28:11 2023

@author: rensmo_l
"""

#%% The code I used to run it without MPI
import fix_scattering
import read_data

# Set the file names 
directory_path = "Data/" # Same for all samples
sample_names = ["sample_1", "sample_2", "sample_3", "sample_4", "sample_5"]

for sample_name in sample_names:
    # Set file name
    file_name = directory_path + sample_name + '.h5'
    # Read the data
    data = read_data.read_data(file_name)
    # Initialize the object
    fixscattering = fix_scattering.FixScattering(data.copy(), file_name) # I just want to read the data, not change it. That is why I make a copy
    # Run the analysis
    fixscattering.run(True, True, True, True, True)
    