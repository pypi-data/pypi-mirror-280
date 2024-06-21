#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import matplotlib.pyplot as plt 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



def graph_ez(electric_field_Z):

    plt.contourf(electric_field_Z,levels=65)
    #plt.axis('off')

    plt.colorbar()
    plt.xlabel('# position traces')
    plt.ylabel('# time traces')
    ax = plt.gca() 
    ax.invert_yaxis() 
    plt.show()
