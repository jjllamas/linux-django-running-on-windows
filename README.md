Linux Django App running on Windows 
==============================================
  
### 1- Download GitPortable for Windows
* More info of [msysgit project] (https://code.google.com/p/msysgit/)
* Download [Git Portable] (https://code.google.com/p/msysgit/downloads/list)
* This portable application provides a linux shell that runs on windows.
* It's like a portable lite linux... (with git installed)
			 
### 2- Intall Python for Windows
* Choose and Download the executable file for Python (http://www.python.org/getit/).
* Install Python in your PC.
           
             
### 3- Install virtualenv and virtualenvwrapper from Git Portable Shell.
    pip install virtualenv
    pip install virtualenvwrapper-win

4.- Create an virtualenv for your project.
* Create a folder for store the Django projects and virtual enviorenments.
* Go to this folder and create the virtualenv.
    virtualenv helloWorld-env
* Command for activate the virtualenv.
    source helloWorld-env/Scripts/activate
* Command for deactivate the virtualenv.
    Deactivate

### 5- Install Django in your virtualenv
* Once created the virtualenv and after activete it, we can install Django.
    pip install Django==1.5

### 6- Run the server and execute the Django Project
* With the virtualenv activated and Django installed, we can run the development server and access to Django application.
Copy HelloWorld Django proyect from this repository in your development path.
And go to project path for execute te server with this command:
    python manage.py runserver
And congratulations you have your Linux Django project running on windows.
You can access to the application from a browser.
    http://127.0.0.1:8000/
