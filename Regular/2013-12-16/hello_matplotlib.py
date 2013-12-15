import numpy
import matplotlib.pyplot as plt


#Straight from MatPlotLib tutorial documentation: 
#http://matplotlib.org/users/pyplot_tutorial.html

#First, use MatPlotLib the way you use Matlab- as an interactive console

t = numpy.arange(0., 5., 0.2) # evenly sampled time at 200ms intervals
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') # red dashes, blue squares and green triangles
plt.ylabel('This y axis label will be used.')
plt.show()

plt.ylabel('This label will NOT appear') #isn't called until AFTER we "show" the plot, so it's ignored
