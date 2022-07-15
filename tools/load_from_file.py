import time
import sys
import os
from numpy import genfromtxt
sys.path.insert(0, os.path.abspath('..'))
from serial_control.serial_control import SerialControl

robot = SerialControl(port="COM4")
robot.open_serial()


values = genfromtxt('sample.csv', delimiter=',')

L0_values = values[0]
L1_values = values[1]
L2_values = values[2]
Mgrip_values = values[3]
Ser_grip_values = values[4]

for i in range(len(L0_values)):
    robot.eff_gripper(Ser_grip_values[i])
    robot.gripper_iman(Mgrip_values[i])
    time.sleep(0.01)
    robot.write_servo(1, L0_values[i])
    time.sleep(0.01)
    robot.write_servo(2, L1_values[i])
    time.sleep(0.01)
    robot.write_servo(3, L2_values[i])
    time.sleep(0.02)

time.sleep(0.1)
robot.home()
