# Software Design Description: WIFI
## Introdcution
The mower is connected to a raspberry pi 0 with wifi capabilities to allow continoius connection to the database. The communication between the mower and the wifi card is a two way serial communcation.

-------------------
## functionality

The program consist of a main program that establishes the connection with both the mower and the database. After the connection is done, two threads are created to read data from the mower and send data to the backend.
Between these threads, a buffer is implemented to ensure that there is no delay when reading the data.
The data from the mower comes in the form a vector i.e., an angele +and lengeth, + a collision boolean that is true in the case that a collision was detected in the movement. By this, it is possible to distinguish a collision from a boundry detection.


-------------------
## Linked requirment
### **M1.4 The mower shall establish a connection from the main node to the backend via the wifi node.**

This is established in the beginning of the program trought the pyrelance wrapping for python.


### **B1.1 The Backend shall read position from the mower via the wifi connection and save these in a file**

This is achieved by acting as a node between the mower and the backend, where data in a the form a of a vector.

### **B1.2 The Backend shall record each position where the collision aboidence is activated**

This is achived by sending a collision boolean with every vector, so that it is possible to destinguish a boundtry detection from a collision.

--------------------