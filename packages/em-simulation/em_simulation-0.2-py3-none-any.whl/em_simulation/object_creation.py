"""
module to create the objects of the model
"""

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#libraries:
import numpy as np
from math import  sqrt

#modules:
from global_constants import RED, RESET
from global_constants import EPSZ, DT




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class ObjectCreation:

    def __init__(self,dicc_model):

        #1) load data: 
        self.size_x = dicc_model['model_size_x']
        self.size_y = dicc_model['model_size_y']

        #2) initialization: 
        self.gaz = np.ones((self.size_y, self.size_x ))
        self.gbz = np.zeros((self.size_y, self.size_x ))

    
    def subsurface(self,dicc_characteristics):

        
        #load values:
        if 'permittivity_r' in dicc_characteristics:
            epsr = dicc_characteristics['permittivity_r']
        else:
            raise KeyError(f'{RED}The key "permittivity_r" does not exist in the dictionary...{RESET}')
        
        if 'conductivity' in dicc_characteristics:
            cond  = dicc_characteristics['conductivity']
        else:
            raise KeyError(f'{RED}The key "conductivity" does not exist in the dictionary...{RESET}')
        
        if 'subsurface_height' in dicc_characteristics:
            subsurface_height  = dicc_characteristics['subsurface_height']
            subsurface_height = self.size_y-subsurface_height
        else:
            raise KeyError(f'{RED}The key "subsurface_height" does not exist in the dictionary...{RESET}')


        # Creation of the dielectric profile    

        self.gaz[subsurface_height:,:] = 1 / (epsr + (cond * DT / EPSZ))
        self.gbz[subsurface_height:,:] = cond * DT / EPSZ

        return (self.gaz, self.gbz)

    def cylinder(self,dicc_characteristics):
        #initialization:
        ia = 7 
        ja  = 7
        ib = self.size_y - 8
        jb = self.size_x  - 8

        #load data:
        
        if 'permittivity_r' in dicc_characteristics:
            epsr = dicc_characteristics['permittivity_r']
        else:
            raise KeyError(f'{RED}The key "permittivity_r" does not exist in the dictionary...{RESET}')
        
        if 'conductivity' in dicc_characteristics:
            cond  = dicc_characteristics['conductivity']
        else:
            raise KeyError(f'{RED}The key "conductivity" does not exist in the dictionary...{RESET}')
        
        if 'radius' in dicc_characteristics:
            radius = dicc_characteristics['radius']
            
        else:
            raise KeyError(f'{RED}The key "subsurface_height" does not exist in the dictionary...{RESET}')

        
        if 'x_position' in dicc_characteristics:
            x_position = dicc_characteristics['x_position']
            
        else:
            raise KeyError(f'{RED}The key "x_position" does not exist in the dictionary...{RESET}')
        
        if 'y_position' in dicc_characteristics:
            y_position = dicc_characteristics['y_position']
            y_position = self.size_y - y_position 
            
        else:
            raise KeyError(f'{RED}The key "y_position" does not exist in the dictionary...{RESET}')


        # creation of the dielectric profile    
        for j in range(ja, jb):
            for i in range(ia, ib):
                xdist = (y_position - i)
                ydist = (x_position - j)
                dist = sqrt(xdist ** 2 + ydist ** 2)
                if dist <= radius:
                    self.gaz[i, j] = 1 / (epsr + (cond * DT / EPSZ))
                    self.gbz[i, j] = cond * DT / EPSZ
                    
        return (self.gaz, self.gbz)

