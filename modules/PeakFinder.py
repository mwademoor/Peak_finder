"""Peak Finder module, for the Casimir course. authors: Suzanne van Dam and Michiel de Moor"""
import numpy as np
import SignalGenerator as sg

class PeakFinder(object):
    """the peakfinder class"""
    
    def __init__(self, array):
        """Initialize the object."""
        self.data = array
        #self.f = file
   
    def find_peak_position(self,minimal_peak_width = 2):
        """function finds a guess of the position of the peak in self.data
        PARAMETERS
        ===================
        minimal_peak_width - peaks are only detected if they are wider than this. default = 2
        -------------------
        OUTPUT
        ===================
        a numpy array containing the detected peak positions 
        -------------------
        """
        self.average = np.average(self.data)
        self.std = np.std(self.data)
        threshold = self.average+self.std
        data_above_threshold = [i for i,j in enumerate(self.data) if j>threshold]
        peak_locations = np.array([])
        record_first = True
        for i in data_above_threshold:
            if record_first: ##record the first point of the prak
                first = i
                record_first = False
            if i+1 in data_above_threshold:
                pass
            else:
                last = i ##the last point of the peak
                if last >= (first+minimal_peak_width-1): #only include wide enough peaks
                    peak_locations = np.append(peak_locations, (first+last)/2.)
                record_first = True ##reinitialize the new 'first' data
        return peak_locations 
    
