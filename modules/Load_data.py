import numpy
import math
import scipy
import sys
import os
from os import path

def import_data_from_file(self,file_frequency,file_S21):
    """import data from file.
    
    Data files should be in the "data" folder.
    
    PARAMETERS
    ----------
    file_frequency : file containing the frequencies used during the experiment
    file_S21 : file containing the S21 parameters recorded for the given frequencies
    
    OUTPUT
    ------
    Numpy array
    First row = frequencies
    Second row = S21
    """
    
    file_path = "data"
    complete_file_path_frequency = os.path.join(file_path, file_frequency)
    complete_file_path_S21 = os.path.join(file_path, file_S21)
    assert os.path.isfile(complete_file_path_frequency), "File does not seem to exist."
    assert os.path.isfile(complete_file_path_S21), "File does not seem to exist."
    frequency = open(complete_file_path_frequency, 'r')
    S21 = open(complete_file_path_S21, 'r')
    
    freq_list=[]
    S21_list=[]
    
    for line in frequency:
            elements_freq=line.split(', ')
            for i in range(len(elements_freq)):
                if elements_freq[i]!= '\n':
                    freq_list.append(float(elements_freq[i]))

    for line in S21:
            elements_S21=line.split(', ')
            for i in range(len(elements_S21)):
                if elements_S21[i]!= '\n':
                    S21_list.append(float(elements_S21[i]))
    
    assert len(freq_list)==len(S21_list), "Number of data points different for x and y, likely data not from same measurement."    
    
    Output_array=np.zeros((2,len(freq_list)))
              
    for j in range(len(freq_list)):
        Output_array[0,j]=freq_list[j]
        Output_array[1,j]=S21_list[j]
    
    frequency.close()
    S21.close()
    
    return Output_array