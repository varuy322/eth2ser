# coding:utf-8
import struct

from sendTcpData.tcpClient import MySocket
# from sendSerialData.serialRead import MySerial
from sendSerialData.serialCRC16 import crc16

host = "192.168.2.2"
port = 8001

mysock = MySocket()
mycrc16 = crc16()
# myser = MySerial()

mysock.myconnect(host, port)

msg = struct.pack('!3B', 0x55, 0xAA, 0x7E)  # Frame header
msg += struct.pack('!3B', 0x01, 0x23, 0x45)  # device ID
msg += struct.pack('!2B', 0x44, 0x05)  # event option
crc_result = mycrc16.createCRC(msg)
print(crc_result)
crchi = crc_result & 0xff
crclo = crc_result >> 8
print(crchi,crclo)
msg += struct.pack('!2B', crchi, crclo)  # CRC checksum
msg += struct.pack('!B', 0x0D)

#print(msg)

cnt = 0
length = 11
while cnt < 10:
    mysock.mysend(msg)
    cnt += 1
    mysock.myrecv(2)

mysock.myclose()
