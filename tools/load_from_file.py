import time
from numpy import genfromtxt
from serial_control.serial_control import SerialControl
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
robot = SerialControl(port="COM4")
robot.open_serial()


values = genfromtxt('sample.csv', delimiter=',')

L0_values = values[0]
L1_values = values[1]
L2_values = values[2]

for i in range(len(L0_values)):
    robot.write_servo(1, L0_values[i])
    time.sleep(0.01)
    robot.write_servo(2, L1_values[i])
    time.sleep(0.01)
    robot.write_servo(3, L2_values[i])
    time.sleep(0.03)
