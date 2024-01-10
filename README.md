## AirBnB_clone
![AirBnB](./assets/AirBnB.png)

### Description
This is the first step towards building a first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

The project aims to replicate the core functionality of the popular vacation rental platform, AirBnB.

### Features
* User registration and authentication
* Property listing and management
* Search functionality with filters (location, price, amenities)
* Booking system
* Review and rating system

### Tech Stack
* __Frontend:__ HTML, CSS, JavaScript
* __Backend:__ Python (Flask)
* __Database:__ MySQL

### Environment
* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __style:__ PEP 8 (v. 1.7.0)
* __testing:__ doctest and unittest

### Repository Contents
* __models:__ directory containing the classes used for the project
* __tests:__ directory containing the unit tests for the project
* __console.py:__ command interpreter for the project
* __AUTHORS:__ file containing the authors of the project
* __README.md:__ file containing the description of the project

### Command interpreter - concole.py
The command interpreter is a program that receives and executes commands typed in by a user. It is executed by running the console.py file and can be run in two ways:
* Interactive mode: `$ ./console.py`
* Non-interactive mode: `$ echo "<command>" | ./console.py`

### How to run the console.py in interractive mode
* `quit` and `EOF` to exit the program
```
$ ./console.py
(hbnb) quit
$
```

* `help` (or `?`) to display the help message
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

* `create` to create a new instance of a class
```
$ ./console.py
(hbnb) create BaseModel
f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6
```

* `show` to print the string representation of an instance
```
$ ./console.py
(hbnb) show BaseModel f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6
[BaseModel] (f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6) {'id': 'f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6', 'created_at': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000), 'updated_at': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000)}
```

* `destroy` to delete an instance
```
$ ./console.py
(hbnb) destroy BaseModel f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6
(hbnb)
```

### How to run the console.py in interractive mode
* `echo` to print the string representation of an instance
```
$ echo "show BaseModel f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6" | ./console.py
[BaseModel] (f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6) {'id': 'f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6', 'created_at': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000), 'updated_at': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000)}
```

* `cat` to print the string representation of an instance
```
$ cat test_show
show BaseModel f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6
$ ./console.py < test_show
[BaseModel] (f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6) {'id': 'f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6', 'created_at': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000), 'updated_at': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000)}
```

### How to run the tests
* `python3 -m unittest discover tests` to run the tests
```
$ python3 -m unittest discover tests
...........
----------------------------------------------------------------------
Ran 11 tests in 0.002s

OK
```
* If the test fails, it will be displayed in the following format:
```
$ python3 -m unittest discover tests
...........F
======================================================================
FAIL: test_create (test_console.TestConsole)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/vagrant/AirBnB_clone/tests/test_console.py", line 28, in test_create
    self.assertEqual(sys.stdout.getvalue(), "[BaseModel] (f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6) {'id': 'f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6', 'created_at': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000), 'updated_at': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000)}\n")

AssertionError: '[BaseModel] (f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6) {\'id\': \'f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6\', \'created_at\': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000), \'updated_at\': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000)}\n' != '[BaseModel] (f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6) {\'id\': \'f0d2b8e7-8d0d-4b9a-9f3d-8cb7d1a0b8e6\', \'created_at\': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000), \'updated_at\': datetime.datetime(2020, 7, 1, 16, 42, 2, 639000)}\n'

----------------------------------------------------------------------
Ran 11 tests in 0.002s

FAILED (failures=1)
```

### Practical Application (use case) of the console.py file:
* 🐛 __Debugging:__ The console is your superhero sidekick for stepping through code, inspecting variables, and squashing bugs in your Airbnb Clone.

* 🚨 __Error Reporting:__ Quickly identify and fix errors to ensure your Airbnb Clone's stability and seamless functionality.

* 🔍 __Data Inspection:__ Dive deep into data structures, view property values, and debug data manipulations with ease.

* 🔄 __User Interaction Testing:__ Simulate user clicks, form submissions, and page navigation to fine-tune your Airbnb Clone's responsiveness.

* 📈 __Performance Analysis:__ Collect metrics, analyze execution times, and optimize your application for a top-notch user experience.

### Authors
* __Tijani Sheu__
    * Github - [@iahm-codes](https://www.github.com/iahm-codes)
    * Email - tijanisheuolamilekan@gmail.com
    * Twitter - [@ahmad.dev](https://twitter.com/AhmadPMTijani)
    * LinkedIn - [Tijani Sheu](https://www.linkedin.com/in/sheutijani/)

* __Fassal farah__
