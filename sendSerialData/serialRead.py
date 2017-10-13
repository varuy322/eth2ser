# coding:utf-8
import serial
import struct


# from sendTcpData.tcpClient import MySocket


class MySerial():
    def __init__(self, ser=None):
        if ser is None:
            print("=============== port_serial==============")
            self.ser = serial.Serial("com4")
            print("check which port was really used >>", self.ser.name)
        else:
            self.ser = ser
            print("******")
        self.ser.baudrate = 2400

    def com_open(self):
        self.ser.open()

    def com_read(self, length):
        buf = self.ser.read(length)
        print(">>>len:", len(buf), " ", buf)
        return buf

    def com_send(self, data):
        num = self.ser.write(data)
        return num

    def com_close(self):
        self.ser.close()


if __name__ == "__main__":
    myser = MySerial()
    cnt = 0
    length = 11
    while cnt < 10:
        readBytes = myser.com_read(length)
        data = bytes([17, 34])
        if readBytes == length:
            print("===OK===")
            num = myser.com_send(data)
            print("send num = ", num, ' data=', data)
        cnt += 1
    myser.com_close()
