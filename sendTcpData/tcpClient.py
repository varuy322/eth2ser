# coding:utf-8
import socket
import struct

hostIP = socket.gethostbyname(socket.gethostname())
sentBytes = 0
recvBytes = 0


class MySocket():
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        print(hostIP)

    def myconnect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        global sentBytes
        sent = self.sock.send(msg)
        if sent == 0:
            raise RuntimeError("socket connection broken!!!")
        sentBytes = sentBytes + sent
        print(hostIP, " send >> ", sentBytes, " bytes!: ",msg)

    def myrecv(self, bytes2read):
        global recvBytes
        recv = self.sock.recv(bytes2read)
        recvBytes = recvBytes + len(recv)
        print(hostIP, " recv >> ", recvBytes, " bytes! :",recv)

    def myclose(self):
        self.sock.close()


if __name__ == "__main__":
    host = "192.168.2.2"
    port = 8001

    mysock = MySocket()
    mysock.myconnect(host, port)
    msg = struct.pack('!3B', 0x55, 0xAA, 0x7E)  # Frame header
    msg += struct.pack('!3B', 0x01, 0x23, 0x45)  # device ID
    msg += struct.pack('!2B', 0x44, 0x05)  # event option
    msg += struct.pack('!2B', 0x44, 0x05)  # CRC checksum
    msg += struct.pack('!B', 0x0D)
    mysock.mysend(msg)
    mysock.myclose()
