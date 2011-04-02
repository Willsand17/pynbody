import pynbody
import numpy as np

def setup() :
    global f, h
    f = pynbody.load("MW1.512/MW1.512g1bwdcK.00512")
    h = f.halos()
    assert type(h) is pynbody.halo.AmigaGrpCatalogue

def teardown() :
    global f
    del f


def test_get() :
    current =  f['pos'][0:100:10]
    correct = np.array([[ 0.05419805, -0.0646539,  -0.15700017],
                        [ 0.04330373, -0.05328381, -0.13771422],
                        [ 0.05118063, -0.05374216, -0.13027677],
                        [ 0.0578489,  -0.05937488, -0.1415794 ],
                        [ 0.0898305,  -0.08368044, -0.19480452],
                        [ 0.06412952, -0.0712738,  -0.15869184],
                        [ 0.08050784, -0.0779544,  -0.18164405],
                        [ 0.06102384, -0.06157777, -0.14551604],
                        [ 0.06705956, -0.07371401, -0.1634458 ],
                        [ 0.05734131, -0.06026748, -0.1280915 ]])
    
    print "Position error of ",np.abs(current-correct).sum()
    assert (np.abs(current-correct).sum()<1.e-7)

def test_standard_arrays() :
    # just check all standard arrays are there
    with f.lazy_off :
        f['x']
        f['y']
        f['z']
        f['pos']
        f['vel']
        f['vx']
        f['vy']
        f['vz']
        f['eps']
        f['phi']
        f['mass']
        f.gas['rho']
        f.gas['temp']
        f.gas['metals']
        f.star['tform']
        f.star['metals']
    
    
def test_halo() :
    assert len(h[1])==444703

    

def test_loadable_array() :
    assert 'HI' in f.loadable_keys()
    f['HI']
    assert 'HI' in f.keys()

    