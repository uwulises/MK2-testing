import pandas as pd
import numpy as np
from serial_control.serial_control import SerialControl
import sys
import os
from pynput.keyboard import Key, Listener, KeyCode
import time
sys.path.insert(0, os.path.abspath('..'))


robot = SerialControl(port="COM4")
robot.open_serial()
L0ang = 90
L1ang = 90
L2ang = 90
L0_list = np.array([], dtype='i')
L1_list = np.array([], dtype='i')
L2_list = np.array([], dtype='i')


def L0(val0):
    global L0ang
    global L1ang
    global L2ang
    global L0_list
    global L1_list
    global L2_list
    if val0 > 0:
        L0ang += 2
    else:
        L0ang -= 2
    print(f"base = {L0ang}")
    robot.write_servo(1, L0ang*0.5)
    L0_list = np.append(L0_list, L0ang*0.5)
    L1_list = np.append(L1_list, L1ang)
    L2_list = np.append(L2_list, L2ang)


def L1(val1):
    global L0ang
    global L1ang
    global L2ang
    global L0_list
    global L1_list
    global L2_list
    if val1 > 0:
        L1ang += 1
    else:
        L1ang -= 1

    print(f"L1 = {L1ang}")
    robot.write_servo(2, L1ang)
    L1_list = np.append(L1_list, L1ang)
    L0_list = np.append(L0_list, L0ang*0.5)
    L2_list = np.append(L2_list, L2ang)


def L2(val2):
    global L0ang
    global L1ang
    global L2ang
    global L0_list
    global L1_list
    global L2_list
    if val2 > 0:
        L2ang += 1
    else:
        L2ang -= 1
    print(f"L2 = {L2ang}")
    robot.write_servo(3, L2ang)
    L2_list = np.append(L2_list, L2ang)
    L1_list = np.append(L1_list, L1ang)
    L0_list = np.append(L0_list, L0ang*0.5)


def on_press(key):

    if key == KeyCode.from_char('w'):
        L1(1)
    if key == KeyCode.from_char('s'):
        L1(-1)
    if key == KeyCode.from_char('a'):
        L0(1)
    if key == KeyCode.from_char('d'):
        L0(-1)
    if key == KeyCode.from_char('q'):
        L2(1)
    if key == KeyCode.from_char('e'):
        L2(-1)


def on_release(key):
    global L0_list
    global L1_list
    global L2_list

    #print('{0} release'.format(key))
    if key == Key.esc:
        values = np.asarray([L0_list, L1_list, L2_list])
        np.savetxt('sample.csv', values, delimiter=",")
        # Stop listener
        print('{0} release'.format(key))
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
