
# Montoliu
## Boilerplate for django projects already configured with tools.

This project is intended to be useful as a starting point to start projects with 
django. Instead of downloading every time django, then south, configuring settings for
developing with more people and so on, here is everything you need for starting
a new project with django and the tools that will help you with that task.


## Applications

Currently the only applications included are:
* Django
* South
* django-debug-toolbar

We'll be adding more applications in the future and will be included in the requirements.txt file so 
you can install them at once.

The recommendation is to use a virtualenv.

## How to use it

You have two options:

1. Copy the file requirements.txt to your computer and use it to install all the applications within a virtualenv or not. From then on, start a django project and set it up as you want.
2. Download the django project and install the requirements (within virtualenv or not).

The second option gives you some common configurations already made. But with the first option you start 
a fresh django project.

We intend to keep updated so the project schema will follow django's specifications.

## Initial Data

During development when you begin to insert data, normally you want to keep it every time you have to
have to reset your database. For this purpouse, the dumpdata.sh script has been created. All you have to do
is to execute in your project directory as follows:

$ ./dumpdata.sh

It will generate a file called initial_data.json inside your project's root directory, so every time you
execute syncdb it loads the tables with initial info.
