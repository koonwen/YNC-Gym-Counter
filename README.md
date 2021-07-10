# YNC-Gym-Counter
The server code for the yncgym.ml website

## Contents
- Building the project
- Repository Structure

## Building the project
If you run macOS or Linux, you may generally follow the instructions and commands exactly. If you use Windows, I provide links that you can reference. These instructions use the command line to build the project, if you are unfamiliar with it, open up your file manager which is "Finder" for Mac and go to your "home" directory (This should be the folder with your name). As you type in the commands, you will be able to see what is happening.
1. Clone the repository. Open the terminal and run `git clone https://github.com/koonwen/YNC-Gym-Counter.git`. (This downloads a copy of the whole repository onto your machine so that you can work with the code. You will find that a new folder will be created in your home folder called "YNC-Gym-Counter" which holds the repository).
2. Create a virtual environment. In the terminal, navigate into the folder with `cd YNC-Gym-Counter` and run `python3 -m venv .` (This creates a new virtual environment for the project inside the repository you have just downloaded. A virtual environment allows you to isolate packages required for the project from your system wide packages. If all has gone well, you will find that there is a new folder) For Windows or general reading of venv: https://docs.python.org/3/library/venv.html
3. Activate the virtual environment. Run the command `source venv/bin/activate`. You should notice that on the left side of your command prompt a (venv) should have popped up. This indicates that you're now within your virtual environment and any packages you download will be confined inside this environment. In the event you want to deactivate the branch, you can run the command `deactivate` but don't do it now! We still need your virtual environment activated. Take note that everytime you end your terminal session by closing it, you deactivate the virtual environment.
4. Download required packages. `pip install -r requirements.txt` (Answer yes to the questions when prompted in the terminal)
5. Test if build was successful. In the terminal run `python3 run.py`. If you see the following, you're in business. Go to the link and you should see the webpage.
```
 * Serving Flask app 'app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with watchdog (inotify)
 * Debugger is active!
 * Debugger PIN: 266-406-274
```
6. Exit the program with CTRL+C and make a new branch for the project. In the terminal once again, type `git branch <name of branch>` (<name of branch> should be replaced with the following syntax "name-branchfeature". E.g. git branch koonwen-frontend).
7. Switch onto branch, `git checkout <name of branch`. 
                                           

## Application Structure        
```
.
├── app
│   ├── db
│   │   ├── db.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── reset.sql
│   │   └── schema.sql
│   ├── __init__.py
│   ├── static
│   │   └── style.css
│   ├── templates
│   │   ├── admin.html
│   │   ├── auth
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── base.html
│   │   └── index.html
│   └── views
│       ├── admin.py
│       ├── auth.py
│       ├── __init__.py
│       └── user.py
├── instance
│   └── sqlite.db
├── LICENSE
├── README.md
├── requirements.txt
├── run.py
└── tests
    ├── conftest.py
    ├── data.sql
    ├── test_auth.py
    ├── test_db.py
    ├── test_factory.py
    └── test_user.py
```
- **README.md**: A file for understanding the project. Actually what you are reading right now.
- **LICENSE**: The policy for using this repository
- **requirements.txt**: text file to instruct python what packages to download
- **run.py**: pyfile Interface to start the flask application
- **instance**: Directory to keep sqlite database files and other instance data
- **tests**: Directory for for tests
- **app**: directory holds all the code related to the website
                                           
The application structure is adapted from the flask documentation. To get a clearer understanding of all the moving parts, refer to:
https://flask.palletsprojects.com/en/2.0.x/tutorial/
