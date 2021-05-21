# Software Design Description: WIFI
## Introduction
The mower is connected to a Raspberry Pi 0 with Wifi capabilities that allows continuous connection to the database. The communication between the mower and the wifi card is a two way serial communcation.

-------------------
## Functionality

The program consist of a main program written in python that establishes the connection with both the mower and the database. After the connection is done, two threads are created to read data from the mower and send data to the backend.

Between these threads, a buffer is implemented to ensure that there is no delay when reading the data.
The data from the mower is in the form a vector i.e., an angle +and lengeth, + a collision boolean that is true in the case that a collision was detected in the movement. By this, it is possible to distinguish a collision from a boundry detection. To send the vector to the database, the function sendDataToDB() is used.

The mower will also notify the Wifi node if a new sessions is started. If that happends the wifi node will update the current date + time and that will be used as a session id for the database so vectors can be grouped by that session id. To update the id , the function updateSessionId() is used.


-------------------
## Requirments
### **M1.4 The mower shall establish a connection from the main node to the backend via the wifi node.**

The connection to the mower is established trought serial communication. 
The backend communication is established in the beginning of the program trought the pyrelance wrapping for python.

### **B1.1 The Backend shall read position from the mower via the wifi connection and save these in a file**

This is achieved by acting as a node between the mower and the backend, where data is in a form of a vector.

### **B1.2 The Backend shall record each position where the collision aboidence is activated**

This is achived by sending a collision boolean with every vector, so that it is possible to distinguish a boundry detection from a collision.

--------------------