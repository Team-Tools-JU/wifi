import serial
from time import sleep
import threading
ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
bufferReady = True
buffer = []

def sendLoop():
    global buffer
    while True:
        if buffer.count > 0 and bufferReady:
            bufferReady = False
            data = buffer.pop(0)
            #send to db
            print(data)
            bufferReady = True


def readLoop():
    while True:
        if bufferReady:
            bufferReady = False
            receivedData = ser.read()              #read serial port
            sleep(0.03)
            dataLeft = ser.inWaiting()             #check for remaining byte
            receivedData += ser.read(dataLeft)
            decodedData = receivedData.decode("utf-8")
            buffer.append(decodedData)
            bufferReady = True


def setup():
    threading.Thread(target=readLoop,args=())
    threading.Thread(target=sendLoop,args=())


setup()