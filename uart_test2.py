import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate


while True:
    
    i = input()
    ba = bytes(i,"utf-8")
    ser.write(ba)
    sleep(0.05)                      
  
