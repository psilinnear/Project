# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:58:07 2023

@author: rensmo_l
"""

def plot_data(data, file_name):
    """
    A function that plots the data from the scattering experiments
    
    Parameters
    ----------
    data : The data is provided as a matrix

    """
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    # I want the data plotted with logarithmic scale and absolute values so I remake the data as:
    processed_data = np.double(np.abs(np.log10(data+1)))

    # Display the image using imshow()
    plt.imshow(processed_data) # To make the plot of the data
    plt.colorbar() # To add a colorbar
    plt.set_cmap('jet') # To get a nice colormap
    plt.clim(0, 4) # Make the caxis
    plt.title(file_name)
    
    figure_name = file_name + '.png'
    plt.savefig(figure_name)
    plt.show() # Show the plot
