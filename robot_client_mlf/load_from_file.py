import time
from numpy import genfromtxt
from client import RobotClient

robot = RobotClient(address="localhost")  # Recuerda usar una dirección válida
robot.connect()

values = genfromtxt('sample.csv', delimiter=',')

L0_values = values[0]
L1_values = values[1]
L2_values = values[2]

for i in range(len(L0_values)):
    robot.set_joints(L0_values[i], L1_values[i], L2_values[i])
   
time.sleep(0.1)
robot.set_joints(q0=0, q1=0, q2=90)

