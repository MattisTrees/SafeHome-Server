# SafeHome-Server
Safe Home (Previously Secure Smart Home) Section 2

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
