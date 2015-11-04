"""function that tests the module SignalGenerator"""
import SignalGenerator
import numpy as np

def test_generate_array():
    assert (SignalGenerator.generate_array(10, noise = False) == np.array([ 0.21774626,  0.48880324,  0.15461862,  1.05722306,  1.22551658,0.79690716,  0.62644355,  0.36520195,  0.64680239,  0.72169636])).all