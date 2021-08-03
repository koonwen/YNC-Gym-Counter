# YNC-Gym-Counter
The server code for the yncgym.ml website

## Contents
- Building the project
- Contributing  
- Testing  
- Repository Structure

## Building the project
If you run macOS or Linux, you may generally follow the instructions and commands exactly. If you use Windows, I provide links that you can reference. These instructions use the command line to build the project, if you are unfamiliar with it, open up your file manager which is "Finder" for Mac and go to your "home" directory (This should be the folder with your name). As you type in the commands, you will be able to see what is happening.
1. Clone the repository. Open the terminal and run `git clone https://github.com/koonwen/YNC-Gym-Counter.git`. (This downloads a copy of the whole repository onto your machine so that you can work with the code. You will find that a new folder will be created in your home folder called "YNC-Gym-Counter" which holds the repository).
2. Create a virtual environment. In the terminal, navigate into the folder with `cd YNC-Gym-Counter` and run `python3 -m venv venv` (This creates a new virtual environment for the project inside the repository you have just downloaded. A virtual environment allows you to isolate packages required for the project from your system wide packages. If all has gone well, you will find that there is a new folder) For Windows or general reading of venv: https://docs.python.org/3/library/venv.html
3. Activate the virtual environment. Run the command `source venv/bin/activate`. You should notice that on the left side of your command prompt a (venv) should have popped up. This indicates that you're now within your virtual environment and any packages you download will be confined inside this environment. In the event you want to deactivate the branch, you can run the command `deactivate` but don't do it now! We still need your virtual environment activated. Take note that everytime you end your terminal session by closing it, you deactivate the virtual environment.
4. Download required packages. `pip install -r requirements.txt` (Answer yes to the questions when prompted in the terminal)
5. Test if build was successful. In the terminal run `python3 run.py`. This starts the developmental server for you to counter check if your code works. If you see the following, you're in business. Go to the link and you should see the application running.
```
 * Serving Flask app 'app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with watchdog (inotify)
 * Debugger is active!
 * Debugger PIN: 266-406-274
```
6. Exit the program with CTRL+C.

## Contributing
To contribute, please adhere to the following procedure.
- Make a new branch for the project. In the terminal, type `git branch <name of branch>` ("name of branch" should be replaced with the following syntax "name-branchfeature". E.g. git branch koonwen-frontend)
- Switch onto your branch with, `git checkout <name of branch>`
- Start developing!
- Once you are happy with your contributions, push your branch to the remote server under your branch name with `git push origin HEAD`. Then open a pull request on github which will allow me to review your code before merging the the master branch

For all other questions and queries, please email: koonwen@gmail.com

## Testing
You might notice that when you ran the developmental server with a fresh install of the application, the site shows "No data yet". This is expected because the actual data is kept on the server. However, you can mock some data by exiting the program and running `flask mock-db`. Rerun the developmental server and you should see that some data has been added.
- There are also unit tests for most of the components in the application. To run all the tests, on the command line, issue `pytest -v`. 
- To view all the test coverage over the application, run `coverage run -m pytest`. Look for the "htmlcov" that should have been generated. Inside the directory, open the "index.html" file in your browser.

## Application Structure        
```
.
├── app
│   ├── db
│   │   ├── db_utils.py
│   │   ├── __init__.py
│   │   └── models.py
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
│       ├── pi.py
│       └── user.py
├── instance
│   └── site.db
├── Jenkinsfile
├── LICENSE
├── README.md
├── requirements.txt
├── run.py
├── setup.cfg
├── setup.py
└── tests
    ├── conftest.py
    ├── db
    │   ├── test_db_utils.py
    │   └── test_models.py
    ├── mockdata.py
    ├── test_factory.py
    └── views
        ├── test_admin.py
        ├── test_auth.py
        ├── test_pi.py
        └── test_user.py
```
- **app**: Directory holds all the code related to the website.
- **instance**: Directory to keep sqlite database files and other instance data (Not shown in the repository but will get created when you first initialize the database)
The application structure is adapted from the flask documentation.
- **Jenkinsfile**: A configuration file to tell jenkins how to build and test the project on the remote server  
- **LICENSE**: The policy for using this repository.
- **README.md**: Information about the project. Actually what you are reading right now.
- **requirements.txt**: Text file to instruct python what packages to download
- **run.py**: Pyfile which acts as an interface to start the flask application.
- **setup.py**: Pyfile for package distribution.
- **setup.cfg**: Configuration files for `pytest` and `coverage` commandline tools  .
- **tests**: Directory for for tests.
  
To get a clearer understanding of all the moving parts, refer to:
https://flask.palletsprojects.com/en/2.0.x/tutorial/
