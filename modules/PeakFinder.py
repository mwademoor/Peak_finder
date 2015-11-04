"""Peak Finder module, for the Casimir course. authors: Suzanne van Dam and Michiel de Moor"""
import numpy as np
import SignalGenerator as sg

class PeakFinder(object):
    """the peakfinder class"""
    
    def __init__(self, array):
        """Initialize the object."""
        self.data = array
        #self.f = file
        
   
    def find_peak_position(array):
        pass
    
def import_data_from_file(self,file):
    """import data from file.
    PARAMETERS 
    file 
    OUTPUT 
    numpy array
    """
    f = open(file, 'r')
    
    ###not working yet. 
    for line in f:
        while i<10:
            print i
            #data_array=np.array([])
            #i=0
            #for line in f:
            #    while i<10:
            #        #print(line)
            #        print i
            #    i+=1
            #    data_array = np.append(data_array, line)
    f.close()  

def generate_data(self, length=100, position=0.5, width = 0.1, maximum = 10., noise = True):
    return sg.generate_array
    """Generate data"""
