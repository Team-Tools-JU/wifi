import serial
from time import sleep
import threading
ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
bufferReady = True
buffer = []

def sendDataToDb(angle , length, collision):
    pass




def sendLoop():
    global buffer
    global bufferReady
    while True:
        if bufferReady:
            if len(buffer):
                bufferReady = False
                data = buffer.pop(0)
                dataArr = data.split(" ")
                angle = dataArr[0]
                length_mm = dataArr[1]
                collision = dataArr[2]
                #send to db
                sendDataToDb(angle,length_mm,collision)
                bufferReady = True


def readLoop():
    global buffer
    global bufferReady
    while True:
        if bufferReady:
            bufferReady = False
            receivedData = ser.read()              #read serial port
            sleep(0.03)
            dataLeft = ser.inWaiting()             #check for remaining byte
            receivedData += ser.read(dataLeft)
            decodedData = str(receivedData.decode("utf-8"))
            decodedData = decodedData.strip()
            buffer.append(decodedData)
            bufferReady = True
            sleep(0.03)


def setup():

    #SET UP DB connection

    t =threading.Thread(target=readLoop,args=())
    t2 = threading.Thread(target=sendLoop,args=())
    t.start()
    t2.start()
    

setup()
