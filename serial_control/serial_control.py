from serial import Serial
import time


class SerialControl:

    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        self.serial = None

    def open_serial(self):
        try:
            self.serial = Serial(
                self.port, 115200, timeout=1, write_timeout=0.1)
            print("The port is available")
            serial_port = "Open"
            time.sleep(2)
        except serial.serialutil.SerialException:
            print("The port is at use")
            self.serial.close()
            self.serial.open()

    def close_serial(self):
        time.sleep(0.2)
        self.serial.close()

    def write_servo(self, id, ang):
        angledata = ang
        if id == 1:
            angledata = 2 * angledata
            self.serial.write((str(angledata+1000) + '\n').encode())
        elif id == 2:
            self.serial.write((str(angledata+2000) + '\n').encode())
        elif id == 3:

            self.serial.write((str(angledata+3000) + '\n').encode())
        elif id == 4:

            self.serial.write((str(angledata+4000) + '\n').encode())
        elif id == 5:

            self.serial.write((str(angledata+5000) + '\n').encode())
        elif id == 6:

            self.serial.write((str(angledata+6000) + '\n').encode())
        elif id == 7:

            self.serial.write((str(angledata+7000) + '\n').encode())

    def gripper_iman(self, val):
        if val == 1:
            # close gripper
            self.write_servo(self, 5, 1)
        else:
            # release gripper
            self.write_servo(self, 5, 0)

    def eff_gripper(self, val):
        # write gripper-servo value
        self.write_servo(4, val)
