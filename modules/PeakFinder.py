"""Peak Finder module, for the Casimir course. authors: Suzanne van Dam and Michiel de Moor"""
import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
import modules.SignalGenerator as sg
import modules.Fitting as fitting

class PeakFinder(object):
    """the peakfinder class"""
    
    def __init__(self, xarray, yarray):
        """Initialize the object."""
        self.xdata = xarray
        self.ydata = yarray
   
    def find_peak_position(self, minimal_peak_width = 5):
        """function finds a guess of the position of the peak in self.data
        PARAMETERS
        ===================
        minimal_peak_width - peaks are only detected if they are wider than this. default = 2
        -------------------
        OUTPUT
        ===================
        a numpy array containing the detected peak positions (indices of self.data)
        -------------------
        """
        self.average = np.average(self.ydata)
        self.std = np.std(self.ydata)
        threshold = self.average+self.std
        data_above_threshold = [i for i,j in enumerate(self.ydata) if np.abs(j)>threshold]
        self.peak_locations = np.array([])
        self.peak_sigma = np.array([])
        self.peak_height = np.array([])
        
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
                    #get the best estimates for the parameters
                    self.peak_locations = np.append(self.peak_locations, self.xdata[int((first+last)/2.)])
                    print(self.xdata[last])
                    print(self.xdata[first])
                    self.peak_sigma = np.append(self.peak_sigma,(self.xdata[last]-self.xdata[first]))
                    self.peak_height = np.append(self.peak_height,(self.ydata[int((first+last)/2.)]))
                record_first = True ##reinitialize the new 'first' data
        return self.peak_locations, self.peak_sigma

    def fit_Gaussian(self):
        """fit peaks.
        PARAMETERS
        plot - if True plot original data and fit.
        OUTPUT
        fitparamters
        """
        # giving initial parameters
        mu = fitting.Parameter(self.peak_locations[0])
        sigma = fitting.Parameter(self.peak_sigma[0])
        height = fitting.Parameter(10)
        
        print(mu(),sigma(),height())
        
        def f_Gauss(x): 
            return height() * np.exp(-((x-mu())/sigma())**2)

        fitparams,fitdata = fitting.fit(f_Gauss, [mu, sigma, height], self.ydata, x = self.xdata)
        
        self.xdata_fit = np.linspace(self.xdata[0],self.xdata[-1],len(self.xdata)*10)
        self.ydata_fit = fitparams[2] * np.exp(-((self.xdata_fit-fitparams[0])/fitparams[1])**2)

        print(fitparams)
        return fitparams,fitdata
     
    
    def plot_fitdata(self):
        fig = plt.figure(figsize = (20,4))
        ax1 = fig.add_subplot(111)
        ax1.plot(self.xdata,self.ydata,label='data')
        ax1.plot(self.xdata_fit,self.ydata_fit,label='fit')
        ax1.legend()
        
        
      