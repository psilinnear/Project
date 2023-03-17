# -*- coding: utf-8 -*-
"""
I have many samples that I want to analyse. I will therefore do this using MPI
and see if the code is faster when using it. 

When running with time 'time mpiexec -n 5 python with_MPI.py' I got the output

Ran process  3
Ran process  4
Ran process  2
Ran process  0
Ran process  1

real    0m10.385s
user    0m0.000s
sys     0m0.015s

When I run 'time python without_MPI.py' I get the following output:
    
    

"""
import fix_scattering
import read_data
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank=comm.Get_rank()


# Set the file names 
directory_path = "Data/" # Same for all samples
sample_names = ["sample_1", "sample_2", "sample_3", "sample_4", "sample_5"]
sample_name = sample_names[rank]

# Set file name
file_name = directory_path + sample_name + '.h5'
# Read the data
data = read_data.read_data(file_name)
# Initialize the object
fixscattering = fix_scattering.FixScattering(data.copy(), file_name) # I just want to read the data, not change it. That is why I make a copy
# Run the analysis
fixscattering.run(True, True, True, True, True)

print("Ran process ", rank)

# Managed to execute this using mpiexec -n 5 python MPI_main.py

    
    