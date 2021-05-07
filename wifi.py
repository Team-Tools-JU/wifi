import serial
from time import sleep
import threading
ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
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
                sleep(0.5)
                print(data)
                bufferReady = True
        else:
            sleep(0.5)


def readLoop():
    global buffer
    global bufferReady
    while True:
        if bufferReady:
            bufferReady = False
            #receivedData = ser.read()              #read serial port
            sleep(0.03)
            #dataLeft = ser.inWaiting()             #check for remaining byte
            #receivedData += ser.read(dataLeft)
            #decodedData = receivedData.decode("utf-8")
            
            sleep(1)
            bufferReady = True


def setup():
    threading.Thread(target=readLoop,args=())
    sendLoop()
    

setup()
