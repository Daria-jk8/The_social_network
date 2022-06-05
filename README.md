# ⭐ The Social Network 
 > website is my little project 🔥
 - Python, Django, admin, user
 - Post, Like, create, update, delete

## RESULT: 
> watch the video



https://user-images.githubusercontent.com/92945302/165134414-0e246ea5-7a8e-4cc2-a3fd-f0d7e01fc4b9.mp4



### ACTION PLAN:

Project architecture:
```bash
The_social_network/            # root directory is a container for your project
│
├── config/                    # with your virtual environment set up and activated and Django installed, you can create a project
│   ├── __init__.py            # an empty file that tells Python that this directory should be considered a Python package
│   ├── asgi.py                # an entry-point for ASGI-compatible web servers to serve your project
│   ├── settings.py            # settings/configuration for this Django project
│   ├── urls.py                # the URL declarations for this Django project; a “table of contents” of your Django-powered site. 
│   └── wsgi.py                # an entry-point for WSGI-compatible web servers to serve your project
│ 
├── core/                      # directory is the actual Python package for your 1st app
│   │
│   ├── migrations/            # Migrations are Django’s way of propagating changes you make to your models          
│   │   └── __init__.py          # (adding a field, deleting a model, etc.) into your database schema. 
│   │
│   ├── __init__.py            # Python uses this file to declare a folder as a package, which allows Django to use code from different apps 
│   │                            # to compose the overall functionality of your web application. won’t have to touch this file
│   ├── admin.py               # file is used to display your models in the Django admin panel. You can also customize your admin panel.
│   ├── apps.py                # file is created to help the user include any application configuration for the app. 
│   ├── models.py              # declare your app’s models in this file, which allows Django to interface with the database of your web application
│   ├── tests.py               # When you’re writing new code, you can use tests to validate your code works as expected.
│   └── views.py               # the code logic of your app in this file
│   └── urls.py                # the URL declarations for app
│   └── forms.py               # preparing and restructuring data to make it ready for rendering; 
│                              # creating HTML forms for the data;
│                               # receiving and processing submitted forms and data from the client;
│   
│   
├── templates/                 # Templates - being a web framework, Django needs a convenient way to generate HTML dynamically.                
│       │              
│       ├──core/
│       │   └── base.html             
│       │   └── footer.html
│       │   └── menu1.html
│       │   └── post_create.html
│       │   └── post_delete.html
│       │   └── post_detail.html
│       │   └── post_update.html
│       │   └── posts.html
│       │
│       ├──css/
│       │    └── style.css 
│       │
│       ├──registration/
│           └── login.html
│           └── signup.html
│
│
├── users/                      # directory is the actual Python package for your 2nd app
│   │
│   ├── migrations/                   
│   │   └── __init__.py          
│   │
│   ├── __init__.py                                
│   ├── admin.py               
│   ├── apps.py                
│   ├── models.py              
│   ├── tests.py               
│   └── views.py               
│   └── urls.py                                                        
│   └── forms.py  
│
└── manage.py                  # a command-line utility that lets you interact with this Django project in various ways   
│                                
└──README.md                   # instruction, notes 










