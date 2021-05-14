import serial
import pyrebase
from time import sleep
import threading
ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
bufferReady = True
buffer = []

firebaseConfig = {
    "type": "service_account",
    "project_id": "teamtools-c9f38",
    "private_key_id": "7e3d216a31cd954c0083aae25deec7863ce18703",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDKUnTnCOvafElF\nAZIrmjEteXkAoWmIJWFJ6LBQo/lXMkymm9MxqSm6apXfeKvi1hF+tVqGKRhB33sC\nVMPEesbGxu0D1t+WteLUc8vGUZVg++6LYSkBZyCYeRC5av5HO8/x94vAqliGwBK3\ni9Yi4/0QeM9uPFP/kuW63UoVe7dcc8Rp+vPZPuFpFq/QBgCbvgw8xWsA3ea4YjyF\nGz806clsbUCx2UJeizIgGZ7WtfTM62011NBX6XFL+9cXcRm8EEzNexHSOT202ozk\np0In5YGiCD6rS7RBVS1NaQwFNZiqXOS2pvdJaZS8fac4IQxW85U+rHKP/V0a2B3K\nRMiugTlfAgMBAAECggEAFhHqmK07dSjroTBrrn/yb2B515zD80sIktRkL1fDwkRF\nYkNLRXaLi79GvArgzSzG2ciUqF/hOoZTV8zBUjSGbHaUsj+FQl5y8PP0vZx2rA6v\nVdryaynBv4AtV9yZAlI++8kiIJE0ePaI1CbX5BR0rZBQKFlCXHW8w6aSB0fol5gD\npKZ1jOpyFa09xbHyJkU0uEXmBdLn6+JPliPS85SjwSVe17SU18fx8HOZSR/OYMJq\nfTpI0bFRy4Aq8avmdh3VyB8JsbCPkVGw5mJHnoU7RBXMcRqk+fZA0KP1YU26Sm/c\n60rI09tBJTHLfCh3qPHJTILzjPBTyXFt1d0asleXOQKBgQDldrcTE3oBHS6ioPmg\nz28fcrEs5cV5xJkXIomwZWplzEpMrGFnoccYHgTEuQQ5376MAxaCk/CeEIdn9NFS\ny5Ak7JylqF/9qCbU63d9TM4OEQ0zyPFC47j7oLfUU5A6ZLEBEsrTgoEuwN/jCLTK\n7BDsDHQmCIDqB4KG6fCP2Fzx3QKBgQDhuDZMlKOS1jnJr4q28y8yx3qJ9a1mqEqm\nrQl6x1kGh37N4cBQCQwWjmYBTRo0FaWnvLlumnbR/EC+2jAMMaB+wMpN6hlgET2T\nhFWw2HueD34Dgs+t5bZzPrr0+NSvzcbXPpojnF0Qj9UstsiK2PJog5rzecaMb8k1\nEiRKC3OKawKBgArp24k3uuzEo4wuldDVLNbVEKIvB3ZkKFfWV7AhEq9myP3ekP9p\nzVtTSizFE/NgteJY30A0oxQRey8xkKcccW2gJ08ls/MPhVFJJbS6623116fn3bmt\ntQWavkOF+e0dDuIbL7Rhl51OpRdaOacRFTj02q1YaDE5TDb4d22P/9OtAoGBALg3\nruE7YnChtFIdmXmM6dVopmLYBmhFK3/ys0zoS4kfpmcDOwBXEe2K1Ed1lNAzZpqK\nVVCmchkY5gKdch9RlWo9kB6c047rIzU1CPanB+TNQgw9g5+qXgiaht0OBA9jQ0hC\niGxN3kp5CQNQPkXLn7OazSivF1NgnHda0hE4XVj3AoGAHvAIBSnRPn0tNbtq2wwg\nBPiNhbRnFSAQHPu4HcSk1pQcq/wf06CGJKYJioI4Q2ygqXJRSZKHdeJzH82Bu0Z7\npauYJsvw8R63VhbJ5f798YTmFffkhmBa+bpoSAhCpZsCFH1pVcBcbgBXnW05AhtH\nSM5XRknVYbYRuwveQv2UokA=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-5xxi4@teamtools-c9f38.iam.gserviceaccount.com",
    "client_id": "113646353887816733314",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-5xxi4%40teamtools-c9f38.iam.gserviceaccount.com"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def sendDataToDb(angle , length, collision):
    #pass
    messageToSend = {'angle': angle, 'length': length, 'collision': collision}
    db.child('messages').push(messageToSend)



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
