Linux Django App running on Windows 
==============================================

Sometimes you have a Django project (for Linux) which you want deploy in a PC with Windows.

For example, at house you have a computer with Linux, where you development your Django app, but you want kill your time in the office in your PC with Windows.

For this case you can use this project with which you can deploy a Django project build for Linux on a Windows machine.

Only you have follow the next easy 5 steps:

### 1- Download GitPortable for Windows
This portable application provides a linux shell that runs on windows. It's like a portable lite linux... (with git installed)
* Turn on your windows machine.
* Download and execute [Git Portable] (https://code.google.com/p/msysgit/downloads/list) application.
* Clone this repository in your development path (for instance `C:\dev`).

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
* Go to your dev path or wherever you want create the virtualenv:
    * `cd /c/dev/`
* Go to this folder and create the virtualenv.
    * `$virtualenv helloWorld-env`
* Activate the virtualenv created, command for activate virtualenv.
    * `$source helloWorld-env/Scripts/activate`
* If you want deactivate... command for deactivate virtualenv.
    * `$deactivate`

### 4- Install Django in your virtualenv
Once created the virtualenv and after activate it, we can install Django.
* Execute GitPortable Bash and execute the following command:
    * `$pip install Django==1.5`

### 5- Run the server and execute the Django Project
With the virtualenv activated and Django installed, we can run the development server and access to Django application.
* Go to Django project folder (where you can find manage.py file), in our example:
    * `cd /c/dev/linux-django-running-on-windows/helloWorld`
* Execute te server with this command:
    * `$python manage.py runserver`
* And congratulations you have your Linux Django project running on windows.
* You can access to the application from a browser.
    * `http://127.0.0.1:8000/`
