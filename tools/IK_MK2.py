import numpy as np

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from serial_control.serial_control import SerialControl
import time


def inverse_kinematics(X=150,Y=0,Z=60):

    zb = Z - 94
    l1=135
    l2=147
    l3 = 56
    
    q0 = np.arctan2(Y,X)

    if np.abs(Y)<1e-6:
        xo = X-l3
    else:
        xo = np.sqrt((X-l3*np.cos(q0))**2 + (Y-l3*np.sin(q0))**2)

    q1 = np.pi - np.arctan2(zb,xo) - np.arccos((xo**2 + zb**2 + l1**2-l2**2)/(2*l1*np.sqrt(xo**2 + zb**2)))
    q2 = np.pi/2 - q1 + np.arccos((l1**2+l2**2-xo**2-zb**2)/(2*l1*l2))

    #to deg
    q0 = -2*np.round(np.rad2deg(q0),0)+90
    q1 = np.round(np.rad2deg(q1),0)
    q2 = np.round(np.rad2deg(q2),0)

    return q0,q1,q2






robot = SerialControl(port="COM8")

robot.open_serial()

q0 , q1, q2 = inverse_kinematics(200,0,40)
time.sleep(1)
robot.send_command([q0,q1,q2])

q0 , q1, q2 = inverse_kinematics(240,0,40)
time.sleep(1)
robot.send_command([q0,q1,q2])

q0 , q1, q2 = inverse_kinematics(290,0,40)
time.sleep(1)
robot.send_command([q0,q1,q2])

time.sleep(1)
robot.home()
robot.close_serial()