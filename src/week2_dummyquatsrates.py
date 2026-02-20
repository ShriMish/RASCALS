import numpy as np
import matplotlib.pyplot as plt
import os
output_dir = "plots/week2"
os.makedirs(output_dir, exist_ok=True)


def quaternion_propagation(omega, prev_q, dt):
    '''This function propagates the quaternion prev_q (scalar-last) forward
    using the angular rate omega and the time step dt to output q_out'''
    propagation_matrix = np.array([[0, omega[2], -omega[1], omega[0]],
                                   [-omega[2], 0, omega[0], omega[1]],
                                   [omega[1], -omega[0], 0, omega[2]],
                                   [-omega[0], -omega[1], -omega[2], 0]])
    q_out = np.dot((np.identity(4) + 0.5*dt*propagation_matrix),prev_q)
    q_out = q_out/np.linalg.norm(q_out)
    if q_out[3]<0:
        q_out = -q_out
    return q_out

q0 = np.array([0,0,0,1])
q = q0
dt = 0.01
q_array = q
t = np.linspace(0,100,int(100//dt))
omegas = np.array([3*np.sin(0.002*t), 0*np.cos(0.02*t), 1*np.sin(0.002*t)])


for i in range(1,len(t)):
    q = quaternion_propagation(omegas[:,i],q,dt)
    q_array = np.column_stack((q_array,q))


plt.plot(t,q_array[0],label = "q1")
plt.plot(t,q_array[1],label = "q2")
plt.plot(t,q_array[2],label = "q3")
plt.plot(t,q_array[3],label = "q4")
plt.xlabel("Time (s)")
plt.ylabel("Quaternion Components")
plt.title("Quaternion Propagation")
plt.legend()
plt.savefig(os.path.join(output_dir, "dummyquatprop.png"))
plt.show()
plt.close()

plt.plot(t,omegas[0], t, omegas[1], t, omegas[2])
plt.xlabel("Time (s)")
plt.ylabel("Dummy Rates")
plt.title("Dummy Rates")
plt.savefig(os.path.join(output_dir, "dummyrates.png"))
plt.show()
plt.close()

