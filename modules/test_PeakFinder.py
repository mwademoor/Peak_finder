"""test file for PeakFinder.py"""
import modules.PeakFinder as pf
import modules.SignalGenerator as sg
import numpy as np

def test_find_peak_position(noise=False):
    array = sg.generate_array(100)
    pf_test = pf.PeakFinder(array)
    assert pf_test.find_peak_position()[0] == 50.0
    

