Linux Django App running on Windows 
==============================================
  
### 1- Download GitPortable for Windows
This portable application provides a linux shell that runs on windows. It's like a portable lite linux... (with git installed)
* Download and execute [Git Portable] (https://code.google.com/p/msysgit/downloads/list) application.

More info of [msysgit project] (https://code.google.com/p/msysgit/)
			 
### 2- Intall Python for Windows
For works with Django you need Python environment installed and configured.
* Choose and Download the executable file for [Python](http://www.python.org/getit/).
* Install Python in your PC.
           
             
### 3- Install and activate virtualenv.
For to be able install more Django projects in the same machine, you should use virtual environments ([virtualenv](http://www.virtualenv.org/en/latest/))
* Execute GitPortable Bash and execute the following commands:
    * `$pip install virtualenv`
    * `$pip install virtualenvwrapper-win`
* Create a folder for store the Django projects and virtual enviorenments, for example:
    * `C:\dev`
* Go to this folder and create the virtualenv.
    * `$virtualenv helloWorld-env`
* Command for activate the virtualenv.
    * `$source helloWorld-env/Scripts/activate`
* Command for deactivate the virtualenv.
    * `$Deactivate`

### 4- Install Django in your virtualenv
Once created the virtualenv and after activate it, we can install Django.
* Execute GitPortable Bash and execute the following command:
    * `$pip install Django==1.5`

### 5- Run the server and execute the Django Project
With the virtualenv activated and Django installed, we can run the development server and access to Django application.
* Copy HelloWorld Django proyect from this repository in your development path.
* Now you have two folders in your development path `C:\dev`
    * `helloWorld-env`
    * `helloWorld`
* Go to project path for execute te server with this command:
    * `$python manage.py runserver`
* And congratulations you have your Linux Django project running on windows.
* You can access to the application from a browser.
    * `http://127.0.0.1:8000/`
