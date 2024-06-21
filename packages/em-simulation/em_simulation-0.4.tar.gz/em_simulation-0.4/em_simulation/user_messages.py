#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#modules:
from global_constants import DT, DDX
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class UserMessages:

    def __init__(self, dicc_model):

        self.size_x = dicc_model['model_size_x']
        self.size_y = dicc_model['model_size_y']
        
        self.position_TX_x = dicc_model['TX_antenna_position_x']
        self.position_TX_y = dicc_model['TX_antenna_position_y']
        self.position_TX_y = self.size_y- self.position_TX_y -1 

        self.position_RX_x = dicc_model['RX_antenna_position_x']
        self.position_RX_y = dicc_model['RX_antenna_position_y']
        self.position_RX_y = self.size_y- self.position_RX_y -1 


    def initial_message(self):

        print('-----------------------------------------------------------------------------------------------')     
        print('-----------------------------------------------------------------------------------------------')   
        print('           *****         ******         *****                *******     ***********           ')
        print('         ***   ***      *********      *********            **     ***   ***     ****          ')
        print('        ***             ***    ***     ***    ***                  ***   ***      ****         ')
        print('        **              ***    ***     ***    **                  ***    ***        ****       ')
        print('        ***********     ***   ***      ***   **                 ***      ***         ****      ')
        print('        ***      ***    *******        ******      ******     ***        ***         ****      ')
        print('        ***      ***    ***            ***  ***             ***          ***        ****       ')
        print('        ****    ***     ***            ***   ***           ***           ***      ****         ')
        print('         *********      ***            ***    ***         ***      **    ***    ****           ')
        print('           *****        ***            ***      **        ***********    **********            ')
        print('-----------------------------------------------------------------------------------------------')     
        print('-----------------------------------------------------------------------------------------------')   
        print('_______________________________________________________________________________________________')
        print('MODEL FEATURES:        ')
        print(f'size {int(self.size_x)*DDX} [m] x {int(self.size_y)*DDX} [m]')
        print(f'spatial discretization: {DDX} [m]') 
        print(f'temporal discretization: {DT*1e12} [ps]')
        print('_______________________________________________________________________________________________')
        print('INITIAL ANTENNA LOCATION: ')
        print(f'transmission antenna in x: {int(self.position_TX_x)*DDX} [m] and in y: {int(self.position_TX_y)*DDX} [m] ')
        print(f'reception antenna in x: {int(self.position_RX_x)*DDX} [m] and in y: {int(self.position_RX_y)*DDX} [m] ')
        print('_______________________________________________________________________________________________')
        

    def progress_message(self,maximum_quantity,what_it_takes):
        percentage = round((int(what_it_takes+1)/int(maximum_quantity))*100,1)
        print(f'{what_it_takes+1} A-scan of {maximum_quantity} has been made, process = {percentage}% ')

    def final_message(self,time):
        print('_______________________________________________________________________________________________')
        print('SIMULATION FINISHED')
        print(f'total simulation time is {round(time/60,2)} [min]')