# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:07:36 2023

@author: rensmo_l
"""
import numpy as np
import plot_data

# Start by creating the class
class FixScattering:
    
    # Initializes all the features
    def __init__(self,data, file_name):
        self.data = self.resize_data(data)
        self.difference = []
        self.file_name = file_name

    def resize_data(self, data):
        """
        I want to work with symmetric data, with the beamstop in the middle. I know the beamstop is in the pixels (983,767) and
        I want it to extend with 450 pixels out from the beamstop. I will work with the resized data for the rest of the analysis
        Parameter: data (from the read_data function)
        """
        middle_x, middle_y, size =  983,708, 450
        return data[middle_y-size:middle_y+size,middle_x-size:middle_x+size]

    def run(self, no_gaps, beamstop, outliers, pointsymmetry, plot):
        
        """
        I want to be able to easily choose what features I want to change with the
        data, that is why I have this run-function  
        Parameter: either True or false for the options of using the functions:
            no_gaps, beamstop, outliers, pointsymmetry, plot
        """
        
        if no_gaps:
            self.no_gaps()
            #print("No gaps")
        if beamstop:
            self.beamstop()
            #print("No beamstop")
        if outliers:
            self.outliers()
            #print("Taken away outliers")
        if pointsymmetry:
            self.pointsymmetry()
            #print("Checked for point symmetry")
        if plot:
            #print("Plotted")
            plot_data.plot_data(self.data, self.file_name)
            
            if len(self.difference ) != 0:                        # Only want to plot this one if I actually checked for point symmetry
                file_name = self.file_name +'_pointsymmetry'
                plot_data.plot_data(self.difference, file_name)
  
    def no_gaps(self):
        """
        2. I want to replace the empty streaks that are due to detector gaps. The plot is point symmetric, so I can fill out the 
           blanks with data from the other side of the beamstop
          
        """
        
        length = self.data.shape[0]                               #Find the length of the data
        col_indices = np.all(self.data == 0, axis=0).nonzero()[0] # Find the indices of the detector gap columns
        row_indices = np.all(self.data == 0, axis=1).nonzero()[0] # Find the indices of the detector gap rows

        for i in col_indices:                                     # For every empty column I replace the data with a mirrored version of data from the other point of the beamstop
            other_side = self.data[:, length-i-1]
            flipped = other_side[::-1]                            # I want to flip the vector upside down, due to the point symmetry of the data
            self.data[:,i] = flipped                              # I replace the column data with the flipped vector 

        for i in row_indices:                                     # For every empty row I replace the data with a mirrored version of data from the other point of the beamstop
            new_vector = self.data[length-i-1, :]
            flipped = new_vector[::-1]                            # I want to flip the vector from left to righ, due to the point symmetry of the data
            self.data[i, :] = flipped                             # I replace the column data with the flipped vector

    def beamstop(self):
        """
        3. Take away the beamstop. I see a streak from the beamstop, which I
            can replace with data from the other side of the beamstop
        """
        
        beamstop_width = 5                                        # I want to find the middle of the beamstop streak and replace it with a width of 5 pixels up and down
        middle = round(self.data.shape[0]/2)                      # I find the middle point of the data
        
        not_beamstop = self.data[middle-beamstop_width:middle+beamstop_width,0:middle] # I find the matrix on the other side of the beamstop, that doesn't contain a streak
        flipped = np.flip(not_beamstop, axis=None)                                     # I flip that matrix both up and down, and left to right, due to the point symmetry of the data
        self.data[middle-beamstop_width:middle+beamstop_width,middle:]  = flipped      # Replace the beamstop with data from the other side
        
    def outliers(self):
        
        """
            4. Take away outliers by comparing the very intense pixels with surrounding data
        """
        limit = 10                                                # The difference between two adjacent points should not be bigger than a factor of ten
        length = self.data.shape[0]                               # Find the length of the data, should be 900

        for i in range(1, length-1):                              # Cycle over all pixels by using two for-loops
            for j in range(1, length-1):
                z = self.data[i,j]                                # Check the value z in one point
                z_close = self.data[i-1,j-1]                      # Check the value z_close of a point close to z
                diff = abs(z-z_close)                             # Find the differences between these two points
                if z <= z_close:                                  # If z is smaller than z_close I want the threshold value to be dependent on z
                    if z == 0:                                    # To define the threshold I need z to be at least 1
                        z = 1
                    threshold = z*limit                           # If the difference between z and z_close is bigger than a factor of 10 it is an outlier and should be taken away
                if z > z_close:                                   # If z is bigger than z_close I want the threshold to be defined by z_close
                    if z_close == 0:                              # Cannot define a threshold value if z_close is zero, has to be at least one
                        z_close = 1
                    threshold = z_close*limit
                if diff > threshold:                              # If the difference between two adjacent points are bigger than the threshold value, it is an outlier and should be taken away
                    self.data[i,j] = self.data[901-i,901-j]       # The outlier is replaced by the value on the other side of the beamstop, since there is point symmetry
        
    #5. I have assumed point symmetry throughout the whole analysis. I also want to check that this statement is actually true.
    # I will therefore check for point symmetry by rotating the figure 180 degrees and subtracting from the other half.
    def pointsymmetry(self):
        
        rotated_data = np.flip(self.data, axis = None)            # Rotate the data 180 degrees
        difference = abs(self.data-rotated_data)                  # Calculate the difference between my data and the difference
        self.difference = difference 
    
