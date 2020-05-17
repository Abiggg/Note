import os
import sys
absdir = os.path.abspath(os.path.dirname(sys.argv[0]))

def load_data():
    import numpy as np
    path=absdir + '/mnist.npz'
    f = np.load(path)
    x, y = f['x_train'], f['y_train']
    x_val, y_val = f['x_test'], f['y_test']
    f.close()
    return (x, y), (x_val, y_val)