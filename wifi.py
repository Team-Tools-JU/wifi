import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
bufferReady = True

buffer = []

def runServer():
    global buffer
    while True:
        if buffer.count > 0 and bufferReady:
            bufferReady = False
            data = buffer.pop(0)
            #send to db
            bufferReady = True


while True:
    if bufferReady:
        bufferReady = False
        received_data = ser.read()              #read serial port
        sleep(0.03)
        data_left = ser.inWaiting()             #check for remaining byte
        received_data += ser.read(data_left)
        decoded_data = received_data.decode("utf-8")
        buffer.append(decoded_data)
        bufferReady = True






