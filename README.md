# SafeHome-Server
Safe Home (Previously Secure Smart Home) Section 2

## Basics

  This main directory represents the Django Apps set-up on top of a LAMP server (Linux, Apache, MySQL, Python).
None of the Server code is hosted here. The SafeHome directory contains the main configuration files for the Django 
installation. The main purpose of the Server lies in the SafeHomeDatabase directory and has the model files for both
the "Users" and "Devices" tables. 

  To run the server, SSH in and navigate to SafeHome Directory from the root folder and run the following command:
  
  >python manage.py runserver [::]:[DESIRED PORT NUMBER]
  
  Despite Django naturally running on port 8000 recently I've had to explicitly define port 8000 for Django to listen on. 
The '[::]' which binds the socket to all of the network interfaces, this is a security risk and should be changed. 

  To make changes to the database cd into /SafeHome/SafeHomeDatabase/ and edit the models.py file. More information on
creating and making changes to SQLite databases here: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

  To make changes to the function that modify the database cd into /SafeHome/SafeHomeDatabase/ and edit the functions in 
the views.py file. If you add any functions in that file you need to edit the urls.py file in the same directory.

## Functions
 
  The Django Server has several functions to interact with the Database:
  
* <b>index</b> - This function remains solely for testing connections and returns a default string. It does not interact with the database.
  * URL: http://[IP ADDRESS]:[PORT NUMBER]/SafeHomeDatabase/

* <b>signUp</b> - takes in parameters from the URL and adds a new entry into the 'Users' table in the database
  * URL: http://[IP ADDRESS]:[PORT NUMBER]/SafeHomeDatabase/signUp?email=[USER EMAIL]&password=[PASSWORD]

* <b>signIn</b> - takes in the same parameters as signUp from the URL and searches the database for a matching User Email and checks the password for correctness
  * URL: http://[IP ADDRESS]:[PORT NUMBER]/SafeHomeDatabase/signIn?email=[USER EMAIL]&password=[PASSWORD]

* <b>addDevice</b> - takes in the User's Email and the Device Name from the URL and adds a new entry into the 'Owns' table in the database, associating a device in the Devices table to a user in the Users table
  * URL: http://[IP ADDRESS]:[PORT NUMBER]/SafeHomeDatabase/addDevice/?email=[USER EMAIL]&device=[DEVICE NAME]

* <b>getDevices</b> - takes in the User's Email from the URL and returns a list of the Device Id's, Device Names, and Ip Addresses for the stream in a list seperated by commas.
  * URL: http://[IP ADDRESS]:[PORT NUMBER]/SafeHomeDatabase/getDevices/?email=[USER EMAIL]

* <b>deleteDevice</b> - takes in the User's Email and the Device Name from the URL and returns a confirmation if the entry in the Owns table was successfully deleted.
  * URL: http://[IP ADDRESS]:[PORT NUMBER]/SafeHomeDatabase/deleteDevice/?email=[USER EMAIL]&device=[DEVICE NAME]

* <b>changeDeviceName</b> - takes in the Device's Unique Id and a New Name for the device from the URL and returns a confirmation if the entry in the Device table was successfully modified.
  * URL: http://[IP ADDRESS]:[PORT NUMBER]/SafeHomeDatabase/changeDeviceName?device_id=[DEVICE ID]&device_name=[NEW DEVICE NAME]
