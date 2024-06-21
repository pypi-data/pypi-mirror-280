"""
Main file for the electromagnetic propagator

* all previously created modules are called:

1) propagator_2D_GPR, is the program that has FDTD modeling
2) wave_form, is the program in which the electromagnetic pulses are loaded
3) creation_object, is the program that creates the objects in the GPR model
4) user_message, is the program that generates the information through the simulation console

"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#libraries:

import time
import numpy as np

#classes
from propagator_2D import Propagator2D
from object_creation import ObjectCreation
from user_messages import UserMessages

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def run_image(dicc_model,dicc_sim_parameters,dicc_sub,dicc_cil):
    
    # 1) initialization:
    console_message = UserMessages(dicc_model)
    inst_propagator = Propagator2D(dicc_model,dicc_sim_parameters)

    #2) creation objects:
    
    inst_objects = ObjectCreation(dicc_model)
    medium = inst_objects.subsurface(dicc_sub)
    medium = inst_objects.cylinder(dicc_cil)

    # 3) run model:

    console_message.initial_message()       
    
    start_time = time.time()      
    electric_field_in_z = inst_propagator.spread(medium )
    final_time = time.time()
    simulation_time = final_time-start_time
    
    # 4)  Save Ez
    np.save(dicc_model['name_simulation'],  electric_field_in_z)

    console_message.final_message(simulation_time )
    
    return electric_field_in_z
   
 