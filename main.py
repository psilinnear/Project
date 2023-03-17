# -*- coding: utf-8 -*-
"""
# Analysis of scattering data

The current goal of my PhD project is to write a reverse Monte Carlo algorithm 
to extract structural information from small angle x-ray scattering data. I will simulate scattering patterns and compare it to the actual measured scattering data and then evaluate the similarities of the patterns. 

The scattering data I get from the experiments cannot directly be used for my algorithm, I have to adapt it a little. The goals of the upcoming project is to take my scattering data and do the following:

1. Load the data and display it, to see what we are working with
2. Make the scattering pattern symmetric around a chosen middle point and fill out the empty pixels from the detector edges (by assuming point symmetry)
3. Take away the beamstop
4. Take away outliers by comparing the very intense pixels with surrounding data
5. Check for point symmetry by rotating the figure 180 degrees and subtracting from the other half. 
6. Use MPI to do the similar process for several scattering patterns

To practice what we learned in the course I will furthermore:
- Write some tests
- Do profiling of the code

"""

#1.  Load the data and display it 
# My files are stored in HDF5-files. I want to load them, investigate them and
# plot the data. I will do this for a lot of samples later, so I create a
# function that takes the sample name as input and produces the data in a matrix. 

# Start with importing my functions
import read_data
import plot_data

directory_path = "Data/"
sample_name = "sample_1"
file_name = directory_path + sample_name + '.h5'

# Read the data
data = read_data.read_data(file_name)

# Plot the raw data, to see what I am working with
plot_data.plot_data(data, file_name)

#%% 
"""
Here I do all of the data analysis
"""
# Import my class
import fix_scattering

fixscattering = fix_scattering.FixScattering(data.copy(), file_name) # I just want to read the data, not change it. That is why I make a copy
fixscattering.run(True, True, True, True, True)
