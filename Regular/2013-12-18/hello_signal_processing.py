import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
 

tau = 5.0*60   # 5 minutes
h_times = np.arange(0.0, 10*tau, 0.1)
impulse_function = len(h_times)*[0]
impulse_function[1] = 10
#Simple first order system model. Example =  X = Xo * e^(-t/T)  
#Physical examples: Voltage in a capacitor in an RC circuit, temperature of a cooling off pot of water
sys = signal.lti(1,[1, 1/tau]) #Signal with a 1/t decay, like a swinging door
#2 ways to simulate the same basic dynamic
#1. we can  simulate an input and plot the output (more general cases)
system_output_t, system_output, system_output_state_vector = signal.lsim(sys, impulse_function, h_times)
#2. Or, we can use the LTI class to just ask for an impulse response
impulse_response = sys.impulse(T=h_times)[1]


plt.subplot(2, 1, 1)
plt.plot(h_times, impulse_function, 'b-')
plt.plot(system_output_t, system_output, 'r-')
plt.xlabel('time (s)')
plt.ylabel('Original Signal (Blue) and Decayed signal (Red)')

plt.subplot(2, 1, 2)
plt.plot(h_times, impulse_response/impulse_response.max(), 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Impulse Response')
#
plt.show()
