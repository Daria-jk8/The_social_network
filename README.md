# β­ The Social Network 
 > website is my little project π₯
 - Python, Django, admin, user
 - Post, Like, create, update, delete

## RESULT: 
> watch the video



https://user-images.githubusercontent.com/92945302/165134414-0e246ea5-7a8e-4cc2-a3fd-f0d7e01fc4b9.mp4



### ACTION PLAN:

Project architecture:
```bash
The_social_network/            # root directory is a container for your project
β
βββ config/                    # with your virtual environment set up and activated and Django installed, you can create a project
β   βββ __init__.py            # an empty file that tells Python that this directory should be considered a Python package
β   βββ asgi.py                # an entry-point for ASGI-compatible web servers to serve your project
β   βββ settings.py            # settings/configuration for this Django project
β   βββ urls.py                # the URL declarations for this Django project; a βtable of contentsβ of your Django-powered site. 
β   βββ wsgi.py                # an entry-point for WSGI-compatible web servers to serve your project
β 
βββ core/                      # directory is the actual Python package for your 1st app
β   β
β   βββ migrations/            # Migrations are Djangoβs way of propagating changes you make to your models          
β   β   βββ __init__.py          # (adding a field, deleting a model, etc.) into your database schema. 
β   β
β   βββ __init__.py            # Python uses this file to declare a folder as a package, which allows Django to use code from different apps 
β   β                            # to compose the overall functionality of your web application. wonβt have to touch this file
β   βββ admin.py               # file is used to display your models in the Django admin panel. You can also customize your admin panel.
β   βββ apps.py                # file is created to help the user include any application configuration for the app. 
β   βββ models.py              # declare your appβs models in this file, which allows Django to interface with the database of your web application
β   βββ tests.py               # When youβre writing new code, you can use tests to validate your code works as expected.
β   βββ views.py               # the code logic of your app in this file
β   βββ urls.py                # the URL declarations for app
β   βββ forms.py               # preparing and restructuring data to make it ready for rendering; 
β                              # creating HTML forms for the data;
β                               # receiving and processing submitted forms and data from the client;
β   
β   
βββ templates/                 # Templates - being a web framework, Django needs a convenient way to generate HTML dynamically.                
β       β              
β       βββcore/
β       β   βββ base.html             
β       β   βββ footer.html
β       β   βββ menu1.html
β       β   βββ post_create.html
β       β   βββ post_delete.html
β       β   βββ post_detail.html
β       β   βββ post_update.html
β       β   βββ posts.html
β       β
β       βββcss/
β       β    βββ style.css 
β       β
β       βββregistration/
β           βββ login.html
β           βββ signup.html
β
β
βββ users/                      # directory is the actual Python package for your 2nd app
β   β
β   βββ migrations/                   
β   β   βββ __init__.py          
β   β
β   βββ __init__.py                                
β   βββ admin.py               
β   βββ apps.py                
β   βββ models.py              
β   βββ tests.py               
β   βββ views.py               
β   βββ urls.py                                                        
β   βββ forms.py  
β
βββ manage.py                  # a command-line utility that lets you interact with this Django project in various ways   
β                                
βββREADME.md                   # instruction, notes 










