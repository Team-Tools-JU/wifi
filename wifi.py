#import serial
from time import sleep
import threading
#ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
bufferReady = True
buffer = ["hej","hej","hej","hej","hej","hej","hej","hej","hej","hej","hej"]

def sendLoop():
    global buffer
    global bufferReady
    while True:
        if bufferReady:
            if len(buffer):
                bufferReady = False
                data = buffer.pop(0)
                #send to db
                print(data)
                bufferReady = True


def readLoop():
    global buffer
    global bufferReady
    i = 0
    y = 5
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
    t =threading.Thread(target=readLoop,args=())
    t2 = threading.Thread(target=sendLoop,args=())
    t.start()
    t2.start()
    

setup()
