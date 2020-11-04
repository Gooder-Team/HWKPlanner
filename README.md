# HWKPlanner

### HWKPlanner is a Django-based application that you can integrate with your Django project. It was made for the Oct-Nov 2020 Timathon Code Jam. It allows the setting of assignments and allows students to view them. Its database integration allows for it to store students, teachers and assignments.

### By the Good Team:
### KingWaffleIII (Integration with Django and README.md author), Dan (Conceptual Design and Error Checking), QuantumFox (Moral Support and Bug Testing), Code-Tap (Moral Support)

## HWKPLANNER SELF DEPLOYMENT GUIDE

**(last edited 3rd November 2020, please note that depending on when you are viewing this guide, some information may be outdated)**

*Note: we are using the Django built-in web server which **IS NOT RECOMMENDED**. This server is meant for development purposes and is not built with security in mind. In this guide, we configure the server to allow connections from the LAN (local access network which simply means whoever is connected to your Wi-Fi/router) and not from outside your LAN.  If you want users outside of your LAN to be able to use this application, consider using a host such as Heroku for security. A useful guide can be found here: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment.*

**If you have any issues, please make sure you read the step(s) correctly and if it still doesn’t work, feel free to create an issue on the GitHub repo.

**Requirements:**
1. Simple knowledge of Python and computing knowledge (recommended but possible without)
2. Suitable server/computer to which you are able to install applications, create folders/files and use the command line (command line knowledge not required). Ideally, you would want superuser (Linux/MacOS) or administrator (Windows) access that runs Linux, MacOS or Windows (HWKPlanner was made with Linux).

**Installation**
1. Install `python 3.8` and `pip`.
2. Install django and dependencies (`python -m pip install django --user` (Windows) or `python3 -m pip install django --user` (Linux/MacOS).
3. Create project (`django-admin startproject <project_name>`).
4. Clone the git repo and extract it.
5. Find the `app` directory and copy it into the project directory (this directory should contain a file called `manage.py` and a folder the same name as the project name) and then do the same with the `templates` directory. Afterwards, it should contain 3 folders and `manage.py`.

Setup
1. Open `settings.py` and change/add the following things:

-  Inside the `INSTALLED_APPS` array, add an entry named `app.apps.AppConfig` so the array looks something like this: (this will add our application to the actual project)
```python
INSTALLED_APPS = [
	'app.apps.AppConfig',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
```
- Inside the `DATABASES` dictionary, you can alter it to fit your needs. The actual app is made with MariaDB but has been tested with SQLite. It is recommended you leave it how it is but you can use another database if you already have one setup. This is so we can save data such as students, assignments and teachers.

- Inside the `TEMPLATES` array, add an entry in `DIRS:` called `BASE_DIR / ‘templates’` so it looks like: (this is so we can add our custom pages we created)
```python
'DIRS': [BASE_DIR / 'templates'],
```

- Now, we need to setup the time zone for the time functionality to work. Find the `TIME_ZONE` variable and change it to your time zone. This works with `tz database` time zones so go to this Wikipedia link (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), find your country code and copy the text in the `TZ database name`column and paste it into the variable. The Good Team is in England so our time zone would look like:
```python
TIME_ZONE = 'Europe/London'
```

- Finally, we need to allow users to connect with the server’s IP address. We are actually using the built-in Django development web server which is **not recommended**. This is only used for development but we’re using it in this guide since it will be within the LAN and we will configure settings.py to allow the local IP address. See the note at the start of the guide to learn how to deploy the app with Heroku. Simply add to the `ALLOWED_HOSTS` array your IP address. Please run `ipconfig` in the command prompt in Windows or `ifconfig` in Linux/MacOS to find your local IP address: (in our case this was 192.168.0.30)
```python
ALLOWED_HOSTS = ["192.168.0.30"]
```
Additionally, the web server is configured to run in debug mode which essentially shows errors in much more detail and displays system information which is not ideal for deployment. Simply change the `DEBUG` variable to `False` to enable normal error pages:
```python
DEBUG = True
```

2. Now that we’ve configured `settings.py`, we need to fix a few things to make our application compatible with your project. Firstly, we want to be able to access our application from the root of your URL for easy access. This is simply accomplished by editing our `django.urls` import and adding `include`. It should look like:
```python
from django.urls import include, path
```

Then, we need to add an entry to the `urlpatterns` array. This is to actually to call our view (the stuff that controls what we see on the webpage) when a certain URL is accessed. Normally, you would have to use `<URL>/app` but this way is easier since it now works at the root of the URL. Simply add the following entry:
```python
path('', include('app.urls'), name="index"),
```
so it looks like:
```python
urlpatterns = [
path('', include('app.urls'), name="index"),
path('admin/', admin.site.urls),
]
```

3. By default, we’ve removed the `migrations` folder from the application which is critical in Django apps. The reason for this is that we want a clean migrations folder. Essentially, the migrations folder is where Django saves models in models.py (classes which you define to add to the database; in this app, we have an Assignment model and a Student model). To initialise a migrations folder, in the app directory, create a `migrations` folder (make sure to spell it exactly!). It should be in `<project root>/app/migrations>`. Then, in the migrations folder, create a file named `__init__.py` (make sure to spell it exactly too!). Then you’re done!

4. The last step of configuration is to initialise the models in `models.py`. Follow the steps below for your OS:
**Windows:**
1. Open File Explorer and navigate to your project route (the one that contains an app folder, the `<name of your project>` folder and a `manage.py` file). 
2. In the bar above the files/folders where it displays your current location on your hard disk, click on it and delete everything in the bar. Once you have done that, type `cmd` and press enter.
3. It should open a command prompt. Now you have done that, enter into the command line the following commands: 
`python manage.py makemigrations`
`python manage.py migrate`
And you’re done! Don’t close the terminal since we’ll need it later!

**Linux/MacOS:**
1. If you are using Linux or MacOS, you are probably familiar with the command line so in terminal, enter `cd <location of your project folder (the one that contains an app folder, the <name of your project> folder and a manage.py file)>` and enter the following:
`python3 manage.py makemigrations`
`python3 manage.py migrate`
And you’re done! Don’t close the terminal since we’ll need it later!

If you are uncomfortable with the command line, open the file explorer and navigate to your project route (the one that contains an app folder, the `<name of your project>` folder and a `manage.py` file). Then, right click on any blank space in the directory and click `Open in Terminal`. Once you have done that, enter the following:
`python3 manage.py makemigrations`
`python3 manage.py migrate`
And you’re done! Don’t close the terminal since we’ll need it later!

**And that’s it for configuration! Time to set it up with students, teachers and assignments!**

5. Let’s test everything is running correctly. In the command line/terminal, enter `python manage.py runserver 0:8000` on Windows or `python3 manage.py runserver 0:8000`<sup>1</sup>. Hopefully if no errors occur, open a web browser and navigate to `<your server’s IP address>:8000` and it should bring you to a web page that says `No students are available`. This is normal since we haven’t created any students. If you got this, that means everything is working okay and you can advance to the next step. If you haven’t and got a 404 error, check you entered the code in step 2 correctly. If you still get an error, check the console to see what error occurred. If you don’t understand it, check you followed all the steps correctly and open up an issue and we’ll try to help you!

<sup>1</sup> *If you want to and you are a Linux/MacOS user, you can actually run the server on port 80 which isn’t exactly recommended but useful if security isn’t a problem. If you do this, you can just enter the IP address of the server and it’ll take you straight to the web page (browsers automatically connect to port 80 since this is the HTTP port). Firstly, you’ll need to make sure a web server isn’t running else it will be using the port. If you are using Apache, Nginx or Lighttpd, simply run `sudo systemctl stop <web server service name>` (requires sudo privileges) and then run `sudo python3 manage.py runserver 0:80`. (you’ll need Django to be installed globally so run `sudo python3 -m pip install django` before you run the previous command).*

6. Now that our application is running, we need to create students, assignments and teachers. But to do that, we need an administrator which can create the teachers and students. Thankfully, this is very easy. If you haven’t already figured it out, the manage.py file pretty much controls everything and there is a command inside of it called `createsuperuser` which creates an administrator. In the command line, stop the web server by pressing `CTRL + C` and enter the following:

**Windows:**
`python manage.py createsuperuser`

**Linux/MacOS:**
`python3 manage.py createsuperuser`

Then fill out the fields. For this guide, we will name our account `admin` with a password of `password` and no email address (this field is entirely optional). For an administrator, this is **very insecure** since this account has full access over the database. Please make sure that this is a secure password. If Django tells you there’s something wrong with the password and that it doesn’t meet the requirements for a secure password, we would recommend **not bypassing password requirements** and create a **more secure** password.

Once you have finished creating the user, you can restart the web server by retyping the command and navigate to `<URL>/admin`. You should get a web page that has a login form. If so, you did it correctly!

Login using the username and password you just created. If everything went okay, you should see the home page.

7. The next step is to create some students, some teachers and some assignments. We will also create a group for teachers which include their permissions so they cannot do things like create other users or students as we want this power to reside with the administrator. Let’s start with the teacher. Start by clicking on the `Groups` link under `Authentication and Authorization`. It should bring you to the groups page.
Next, click on `Add Group +`. Name the group whatever you want. This will house all the teachers and define their permissions so we will call the group `Teachers`. When it comes to permissions, we only want them to be able to control assignments so scroll down the menu until the permissions begin to start with `app | assignment`. Hold down `CTRL (Windows/Linux)` or `CMD (Mac)` and select all permissions that begin with `app | assignment`. Then press the `right arrow` to apply those permissions.

Once you have done that, press `SAVE`. Now, you should see a group called `Teachers`. This will hold all of our teacher permissions. Next, click `Users` under `Authentication and Authorization`. This page should be similar to the group one and you should be able to see your administrator account. If you wish, you can click on this account and change the name and/or email. Leave the permissions for this user. Let’s click on `Add User +`. This will be our teacher’s account. For the purpose of this guide, we will only be creating one account but feel free to make as many as you want. It will ask for a username and password so fill out these fields. We’ll use `Mr_Thomas` and a `randomly generated secure password`. In the command line way of doing this, you were able to bypass password requirements but in this page, these **requirements are enforced**. 

Then, press `SAVE`. It will bring you to more fields for this account. We’re going to add a first name `(James)` and a last name `(Thomas)` as well as adding the account to the group. Fill the name fields and then, under `Groups`, click on `Teachers` and then the right arrow to apply this. Finally, check the `Staff status` checkbox so that this user can login. You can also add an email address. You can ignore the permissions field and the important dates field and click on `SAVE`. 

You should see the new account in the `Users` menu. Now, we will create some students. Click on the `Students` panel under `App`. It will be similar to the `Groups”` menu. Click on `Add Student +` and enter the student’s name. Currently, the student model doesn’t have any other fields but the name which is all that is required. We’ll call our student `John Doe`. In this tutorial, we’ll only be creating one but you can create as many as you want. Click on `SAVE`. It will now appear in the menu. 
Before we create an example assignment, let’s login into the teacher’s account and see if they have the permissions they need. Click on `Log Out` on the top right and then click on `Log in again`. Enter the teacher’s username and password and click `login`. You should only see the `Assignments` panel. If so, you have setup the correct permissions!

Click on `Assignments` and then `Add Assignment +`. Fill out the `name, description, teacher and subject` fields. For the `date fields`, click on `Today` and `Now ` to select the current times and for the due date, set a date which is in the future. We’ll set the due date for a week in the future at noon. In the `Students` field, you should see the student(s) you created. Click on which ones you want to set this assignment for `(use CTRL/CMD + click to select multiple)` and then click `SAVE`. You have now set an assignment for the student and you are done with the Administration page!

7. Remember when we went to `<URL>:8000` and we got that `No students are available` page?
  
Now if you go to the same site, you should get a different page asking you to click on your name.
Click on the student’s name who you set the assignment for.
You should see the assignment you have set. If you don’t make sure you actually set the assignment for the student. Click on the assignment you set.

This page shows the details of the assignment as well as a timer for how long the assignment is active.

**And that’s it!**

*This is the end of the self deployment guide. Now that you have it working, you can create more students, teachers and assignments. The code is open source so you can always edit it if you wish. If there’s a really cool addition you want to add, feel free to create a merge request! If you have any issues, feel free to create an issue on the GitHub Repo.*

- The Good Team

## By the Good Team
## KingWaffleIII (Integration with Django), Dan (Conceptual Design), QuantumFox (Moral Support), Code-Tap (Moral Support)
