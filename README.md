# SafeHome-Server
Safe Home (Previously Secure Smart Home) Section 2

  This main directory represents the Django Apps set-up on top of a LAMP server (Linux, Apache, MySQL, Python). None of the Server code is hosted here. The SafeHome directory contains the main configuration files for the Django installation. The main purpose of the Server lies in the SafeHomeDatabase directory and has the model files for boththe "Users" and "Devices" tables. 

  To run the server, SSH in and navigate to the first SafeHome Directory from the root folder (the one containing the managy.py file) and run the following command:
  
  >python manage.py runserver 0:[DESIRED PORT NUMBER]
  
  I've been using port 8001 because for some reason 8000 wont work. The 0 before the port number represents a placeholder Ip address and is only used because it is easy and I don't have a technical reason yet not to use it, same with the port number.

  To make changes to the database cd into /SafeHome/SafeHomeDatabase/ and edit the models.py file. More information on creating and making changes to SQLite databases here: https://docs.djangoproject.com/en/3.0/intro/tutorial02/
