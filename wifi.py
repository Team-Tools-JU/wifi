import serial
import pyrebase
import datetime
from time import sleep
import threading
ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
bufferReady = True
buffer = []
dt = datetime.datetime.now()

session_id = dt.strftime("%Y-%m-%d-%H:%M:%s")


firebaseConfig = {
    "apiKey" : "AIzaSyCXSY5xD4wyy0H8Ubtl7DfBb_e493Esg90",
    "authDomain" : "teamtools-c9f38.firebaseapp.com",
    "databaseURL" : "https://teamtools-c9f38-default-rtdb.firebaseio.com",
    "projectId" : "teamtools-c9f38",
    "storageBucket" : "teamtools-c9f38.appspot.com",
    "messagingSenderId" : "572582303921",
    "appId" : "1:572582303921:web:a4f7994bfcaaea159aea90",
    "measurementId" : "G-X9ZWKFGELQ"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

def sendDataToDb(angle , length, collision):
    messageToSend = {'angle': angle, 'length': length, 'collision': collision}
    db.child(session_id).push(messageToSend)
    



def sendLoop():
    global buffer
    global bufferReady
    while True:
        if bufferReady:
            if len(buffer):
                bufferReady = False
                data = buffer.pop(0)
                dataArr = data.split(" ")
                if len(dataArr) == 3:
                    angle = dataArr[0]
                    length_mm = dataArr[1]
                    collision = dataArr[2]
                    sendDataToDb(angle,length_mm,collision) #send data to db.
                    print(dataArr)
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
    #setupfucntions for the threads.
    t =threading.Thread(target=readLoop,args=())
    t2 = threading.Thread(target=sendLoop,args=())
    t.start()
    t2.start()
    

setup()
