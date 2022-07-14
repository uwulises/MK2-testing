from serial import Serial
import time


class SerialControl:

    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        self.serial = None

    def open_serial(self):
        try:
            self.serial = Serial(self.port, 115200, timeout=1, write_timeout=0.1)
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

    def write_servo2(self, id, ang):
        angledata = ang
        if id == 1:
            angledata = 2 * angledata
            self.serial.write((str(angledata+1000)+ '\n').encode())
        elif id==2:
            self.serial.write((str(angledata+2000)+ '\n').encode())
        elif id==3:

            self.serial.write((str(angledata+3000)+ '\n').encode())
        