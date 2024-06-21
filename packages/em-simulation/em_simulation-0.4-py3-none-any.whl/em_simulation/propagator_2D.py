"""
module contains two functions:
1) FDTD modeling
2) PML absorbent barrier
"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import numpy as np

from user_messages import UserMessages


#modules:
from global_constants import RED, RESET
from global_constants import EPSZ, DT,DDX,SPEED_C
from waveform import Waveform

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Propagator2D:

    def __init__(self,dicc_model,dicc_sim_parameters):
        
        #intialization: 
        self.name_file = dicc_model['name_simulation']
        self.size_x = dicc_model['model_size_x']
        self.size_y = dicc_model['model_size_y']
        
        self.position_TX_x = dicc_model['TX_antenna_position_x']
        self.position_TX_y = dicc_model['TX_antenna_position_y']
        self.position_TX_y = self.size_y- self.position_TX_y -1 

        self.position_RX_x = dicc_model['RX_antenna_position_x']
        self.position_RX_y = dicc_model['RX_antenna_position_y']
        self.position_RX_y = self.size_y- self.position_RX_y -1 

        self.number_steps_antenna = dicc_sim_parameters['steps_antenna']
        self.time_window = dicc_sim_parameters['time_window']
        self.frequency = dicc_sim_parameters['frecuency']

        self.caracteristicas_modelo = dicc_model
        
        self.C = SPEED_C
        self.DELTA_T = DT

    def spread(self,medios):
        
        #initialization: 
        gaz, gbz = medios    
        gi2, gi3, gj2, gj3, fi1,fi2,fi3,fj1,fj2,fj3 = self.PML_parameters()

        num_steps_antenna = self.number_steps_antenna
        t_window = self.time_window

        electric_field_Z = np.zeros(( t_window+1,num_steps_antenna ))

        x_modelo = self.size_x
        y_modelo = self.size_y

        #-----------------------------------------------------------------------
        # main : 

        for pasos in range(num_steps_antenna):  
        
            #variable initialization
            ez = np.zeros((y_modelo, x_modelo)) 
            ix = np.zeros((y_modelo, x_modelo))
            dz = np.zeros((y_modelo, x_modelo))
            hx = np.zeros((y_modelo, x_modelo))
            hy = np.zeros((y_modelo, x_modelo))
            ihx = np.zeros((y_modelo, x_modelo))
            ihy = np.zeros((y_modelo, x_modelo))            
      
        
            # Main FDTD Loop
            for time_step in range(1, t_window + 1):
                
                # Dz calculation:
                for j in range(1, x_modelo):
                    for i in range(1, y_modelo):
                        dz[i, j] = gi3[i] * gj3[j] * dz[i, j] + gi2[i] * gj2[j] * 0.5*(hy[i, j] - hy[i - 1, j] - hx[i, j] + hx[i, j - 1])
                        
                # source pulse:          
                pulse = Waveform(self.frequency).ricker(time_step,self.DELTA_T ) 
                dz[self.position_TX_y, self.position_TX_x+pasos] = pulse
                    
                
                #calculation of the Ez field
                for j in range(1, x_modelo):
                    for i in range(1, y_modelo):
                        ez[i,j] = gaz[i,j] * (dz[i,j]-ix[i,j]) 
                        ix[i,j] = ix[i,j] + gbz[i,j]*ez[i,j]
                        
                # calculation of the Hx field
                for j in range(x_modelo - 1):
                    for i in range(y_modelo - 1):
                        curl_e = ez[i, j] - ez[i, j + 1]
                        ihx[i, j] = ihx[i, j] + curl_e
                        hx[i, j] = fj3[j] * hx[i, j] + fj2[j] *(0.5 * curl_e + fi1[i] * ihx[i, j])
                            
                # field calculation Hy
                for j in range(0, x_modelo - 1):
                    for i in range(0, y_modelo - 1):
                        curl_e = ez[i, j] - ez[i + 1, j]
                        ihy[i, j] = ihy[i, j] + curl_e
                        hy[i, j] = fi3[i] * hy[i, j] - fi2[i] *(0.5 * curl_e + fj1[j] * ihy[i, j])
                        
                        
                #Save the field at the receiver location
                electric_field_Z[time_step-1,pasos] = ez[self.position_RX_y,self.position_RX_x+pasos]

            #message for user: 
            UserMessages(self.caracteristicas_modelo).progress_message(num_steps_antenna,pasos)


        return electric_field_Z
            
    def PML_parameters(self):

        #initialization:
        x_model =self.size_x
        y_model = self.size_y
        
        gi2 = np.ones(y_model)
        gi3 = np.ones(y_model)
        fi1 = np.zeros(y_model)
        fi2 = np.ones(y_model)
        fi3 = np.ones(y_model)

        gj2 = np.ones(x_model)
        gj3 = np.ones(x_model)
        fj1 = np.zeros(x_model)
        fj2 = np.ones(x_model)
        fj3 = np.ones(x_model)

        # creation of the PML
        
        npml = 8 #number of yee cells taken

        for n in range(npml):
            xnum = npml - n
            xd = npml
            xxn = xnum / xd
            xn = 0.33 * xxn ** 3
            gi2[n] = 1 / (1 + xn)
            gi2[y_model - 1 - n] = 1 / (1 + xn)
            gi3[n] = (1 - xn) / (1 + xn)
            gi3[y_model - 1 - n] = (1 - xn) / (1 + xn)
            gj2[n] = 1 / (1 + xn)
            gj2[x_model - 1 - n] = 1 / (1 + xn)
            gj3[n] = (1 - xn) / (1 + xn)
            gj3[x_model - 1 - n] = (1 - xn) / (1 + xn)
            
            xxn = (xnum - 0.5) / xd
            xn = 0.33 * xxn ** 3
            fi1[n] = xn
            fi1[y_model - 2 - n] = xn
            fi2[n] = 1 / (1 + xn)
            fi2[y_model - 2 - n] = 1 / (1 + xn)
            fi3[n] = (1 - xn) / (1 + xn)
            fi3[y_model - 2 - n] = (1 - xn) / (1 + xn)
            fj1[n] = xn
            fj1[x_model - 2 - n] = xn
            fj2[n] = 1 / (1 + xn)
            fj2[x_model - 2 - n] = 1 / (1 + xn)
            fj3[n] = (1 - xn) / (1 + xn)
            fj3[x_model - 2 - n] = (1 - xn) / (1 + xn)

        return (gi2,gi3,gj2,gj3,fi1,fi2,fi3,fj1,fj2,fj3)