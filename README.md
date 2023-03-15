# Project

Before the course this was my plan:
I need to do analysis on small angle scattering data. I have yet not written a code to do so, but will do it in this project. The scattering data that is uploaded is not good enough to use for my future algorithm. I want make the size symmetric around the middle point, fill in the streaks of the detector and investigate whether it is point symmetry or not. 


Which turned into the following project:
The current goal of my PhD project is to write a reverse Monte Carlo algorithm to extract structural information from small angle x-ray scattering data. I will simulate scattering patterns and compare it to the actual measured scattering data and then evaluate the similarities of the patterns. 

- Using the program main.py (using the functions read_data, plot_data and the class FixScattering) you can do the following steps:
The scattering data I get from the experiments cannot directly be used for my algorithm, I have to adapt it a little. The goals of the upcoming project is to take my scattering data and do the following:

1. Load the data and display it, to see what we are working with
2. Make the scattering pattern symmetric around a chosen middle point and fill out the empty pixels from the detector edges (by assuming point symmetry)
3. Take away the beamstop
4. Take away outliers by comparing the very intense pixels with surrounding data
5. Check for point symmetry by rotating the figure 180 degrees and subtracting from the other half. 

- I an analyzing a lot of scattering patterns and wanted to see if MPI can help me speed up the process. See with_MPI and without_MPI for this part of the projekt.

- Out of curiosity I profiled the main.py code using Spyders built-in profiler which yielded the following result
Function/Module   Total time    Local time
run                 2.51 s       1.26 ms
read_data           208.37 ms    85.10 us
plot_data           4.93 s       48.17 ms
_find_and_load      12.40 us     4.5 us

It is obvious that the plotting of the data takes the absolute longest time. If I wanted to speed up the code I would start there. I don't need to see the results continuously as I run it, I just want to save the results. I think that could save me a lot of time

- I also wanted to run a few tests of the code. I will not test the whole code, but a few important steps.

