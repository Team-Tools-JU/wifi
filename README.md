# Software Design Description: WIFI
## Introduction
The mower is connected to a Raspberry Pi 0 with WiFi capabilities that allows continuous connection to the database. The communication between the mower and the WiFi card is a two way serial communcation.

-------------------
## Functionality

The program consists of a main program written in Python that establishes the connection with both the mower and the database. After the connection is done, two threads are created that read data from the mower and send data to the backend.

Between these threads, a buffer is implemented to ensure that there is no delay when reading the data.
The data from the mower is in the form a vector i.e., an angle, distance traveled and a collision boolean that is true in the case that a collision was detected in the movement. By this, it is possible to distinguish a collision from a boundry detection. To send the vector to the database, the function sendDataToDB() is used.

The mower will also notify the WiFi node if a new sessions is started. If that happends, the WiFi node will update the current date and time. This will then be used as a session id for the database so that vectors can be grouped by that session id. To update the id , the function updateSessionId() is used.


-------------------
## Requirements
### **M1.4 The mower shall establish a connection from the main node to the backend via the WiFi node.**

The connection to the mower is established trough serial communication. 
The backend communication is established in the beginning of the program trough the Pyrebase wrapping for Python.

### **B1.1 The Backend shall read positions from the mower via the WiFi connection and save these in a file**

This is achieved by acting as a node between the mower and the backend, where data is in the form of a vector.

### **B1.2 The Backend shall record each position where the collision avoidence is activated**

This is achieved by sending a collision boolean with every vector, so that it is possible to distinguish a boundry detection from a collision.

--------------------
