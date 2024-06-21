"""
This model has different waveforms implemented
for use in the propagator

*Gaussian
*first derivative of the Gaussian pulse
*ricker
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from math import exp, pi,sqrt 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Waveform:

    def __init__(self, freq):
        self.frequency = freq
            

    def gaussiana(self, time_step,delta_t):

        sita = 2*(pi**2)*(self.frequency)**2
        equis = 1/self.frequency
        time = time_step*delta_t
        
        pulse = exp(-1*sita*(time-equis)**2)
        
        return pulse

    
    def first_der_gaussiana(self,time_step,delta_t):

        sita = 2*(pi**2)*(self.frequency)**2
        equis = 1/self.frequency
        time = time_step*delta_t

        pulse = -2 *sqrt(exp(1)/(2*sita))*sita*(time-equis)*exp(-1*sita*(time-equis)**2)

        return pulse

    def ricker(self,time_step,delta_t):

        sita = (pi**2)*(self.frequency)**2
        equis = sqrt(2) /self.frequency
        time = time_step*delta_t

        pulse = -1*((2*sita*((time-equis)**2))-1)*exp(-1*sita*(time-equis)**2)

        return pulse



        