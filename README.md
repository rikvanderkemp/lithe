# lithe #

This came about since I needed a quick way to prototype projects. Using static HTML files can be tiresome and it misses a nice way of reusing elements as I am used to in template engines such as Twig or Jinja2. 

## Python 3 & Virtualenv ##

Make sure you have Python 3.x and Virtualenv installed. Take a look [here](https://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation) for an installation guide of Virtualenv and come back when finished.

## Initialising ##

Create a virtualenv for your new project

	 virtualenv -p python3 example_env
	 
Activate your environment using:
	
	source bin/activate

Create a folder to hold your app project and navigate to this folder e.g.

	mkdir ~/projects/lithe_site

Now clone lithe to this folder using:

	git clone https://github.com/rikvanderkemp/lithe
	

Install requirements by running

	pip install -r lithe/requirements.txt
	
This will install all requirements needed to run lithe.


# Setup lithe #

lithe comes with a quickstart setup script. Use this when starting a new site you will be up and running in no-time.

From you app folder run

	python lithe/setup.py
	
Follow the instructions it will only take a minute or so. That is it, you are now able to start prototyping with Jinja2 and even use YAML files to create an entire website with reusable templates.
		

## Side notes and disclaimers ##

* This is for obvious reasons __not__ for production usage. Although the build HTML files can safely be uploaded to your web server.
* It is meant to be simple and not complicated, function over form, KISS and all those fancy terms
* I have no intention right now to create python modules and integrations with PIP, if you would like to contribute that would be awesome.
* There is a slight chance that using this system causes blackholes and cracks in time, do not blame me.
