---
layout: post
title: Upload (Functional) Python Projects to pip and PyPI
summary: Sometimes libraries just don’t cut it.
featured-img: functional_pip
categories: Python
type: post
---

## Upload (Functional) Python Projects to pip and PyPI

Sometimes libraries just don’t cut it

![Photo by [kate rowe](https://unsplash.com/@katekatebear?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/fractals?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)](https://cdn-images-1.medium.com/max/2000/0*1-GnfHW8uTNgMiO3)

## Quick notes

Making sure we are on the same page.

* Python’s package manager pip uses the website PyPi.org for distributing and managing packages. So by uploading a package to PyPI, you are also uploading to pip.

* A package is the folder that contains the files necessary for your program to run.

* All the commands listed are for Linux. If you are on a different operating system, such as windows, you may want to use some different commands, such as python instead of python3

* In my files I use example_directory, but I upload the package as Example-Functional-Package so I refer to it differently.

* If your main file imports another local file(which it probably will), you have to import differently: If I wanted to import the python file modules.py from the same directory, I would write from . import modules Instead of writing import modules

* All the code used in the tutorial can be found [here](https://github.com/saleguas/Publications/tree/master/uploading-projects-to-pip/example_directory).

## Installing dependencies

Make sure you have the required libraries.

<script src="https://gist.github.com/saleguas/f6d2ee2c9e8b1b05101f478030f395b4.js"></script>

## Creating a project

Let’s create a quick project to publish. First, we have our empty package folder:

<script src="https://gist.github.com/saleguas/0bb072d263ee1504505c4d76bcbff206.js"></script>

Now let’s add some files:

This file will have our methods we will call. Let’s add some basic number methods:

<script src="https://gist.github.com/saleguas/064a84a2ef60cfaf03e90f141c7c5ff0.js"></script>

And for the sake of examples, let’s also make a config/ folder and add some data manipulation methods:

<script src="https://gist.github.com/saleguas/ae7ff8b31c98cd831ae695b560fe4dc9.js"></script>

Now, in the end our modules.py will look something like this:

<script src="https://gist.github.com/saleguas/6df83f007dc0c90cc4b498bf1a62572a.js"></script>

This file will be the file that runs our code. We will use an [argument parser](https://docs.python.org/2/library/argparse.html) to call our code.

    usage: parser [-h] [-f FIBONACCI] [-b FIZZBUZZ] [-s SAVE] [-p]

    Does cool stuff.

    optional arguments:
      -h, --help            show this help message and exit

    Sequences Commands:
      Generates number sequences

    -f FIBONACCI, --fibonacci FIBONACCI
                            Calculates the first N numbers in the Fibonacci sequence

      -b FIZZBUZZ, --fizzbuzz FIZZBUZZ
                            Calculates the first N values of the      FizzBuzz sequence.

    Data Management:
      Saves and manages files

    -s SAVE, --save SAVE  Pass in a file path. Saves the file to the /data
                            folder in this project.
      -p, --print           Prints all files saved in the /data folder

Our package structure should look something like this:

<script src="https://gist.github.com/saleguas/dec5e21b99240ad9ad5f165ccf48fde6.js"></script>

The goal of this tutorial is that I want to be able to run my argument parser file from the command line, such as:

<script src="https://gist.github.com/saleguas/cbb516ed10c5cdd5ae21c398cea3c8d6.js"></script>

## Creating Packaging Files

So in order to do this, we have to prepare our package for uploading. You have to add four files in order to publish your package. These files are:

## README.md

a file that described your project. The text in this file show under the description of your package. Make sure it is in the same folder as your package(but not inside your package). Might look something like this:

<script src="https://gist.github.com/saleguas/a8214ad0b2d8eb16285f3b9114066bda.js"></script>

## __init__.py

a file that is called when the package is built. Place this inside your package(s), otherwise they will not be found; the file can be completely blank, but it must exist. Ours will be blank.

## setup.py

a file that is used to build your project. Comes with various options. For this package, it will look something like this:

<script src="https://gist.github.com/saleguas/a336205e1aa76b1bf8a30d0f933ccd60.js"></script>

## Explaining the parameters

The [setup.py](https://github.com/saleguas/Publications/wiki/Uploading-(Functional)Python-Projects-to-pip-and-PyPI#-setuppy-) file has many options for building your package, and it’s important to know about them; however, I’m only covering some of the parameters.

### name

The name of the package when it is distributed. Keep in mind this can be different from your local package name(my local package name is example_directory but I upload it as Example-Functional-Package).

### version

The version of the project. You should probably use [semantic versioning.](https://semver.org/).

### author

The people that created the project. Will show in the package information.

### author_email

The email that is shown in the package information.

### description

The short description that appears in previews of the package.

### long_description

The long description that shows when viewing the package’s webpage from PyPI.

### long_description_content_type

The format the long description is in. Ours is in markdown so we put text/markdown.

### url

If the package’s source code is hosted somewhere, put the URL here. Usually a GitHub link.

### packages

The name of the package(s) in the folder(the directory name). Your project setup would be different if there was multiple sub-packages.

### package-data

If you have any static files, include the paths here. List the package first, then any directories in the package. In our case the directory is example_package and the data folder is a sub folder that we want to include.

### keywords

Words that are used in searching. They help people find your package.

### classifiers

Tags that go with your package. Gives some more information about your project. You can find all the classifiers on the [PyPI website](https://pypi.org/classifiers/).

### entry_points

Has multiple options, but the one we are interested in is console_scripts, which is the function that let's us call our function from the command line. The console_scripts automatically registers to the path. The syntax is as followed:

{command to be called by}={folder/package name}.{python file}:{function}

because the one we created is parser=example_package.parser:main, we can call the function main inside the example_package/parser.py with the name parser from the command line.

### python_requires

The python version(s) required to run the script.

## LICENSE

The license for your code. If you are unsure, [this might help you](https://choosealicense.com/).

This was a lot to handle at once, but at the end your project structure should look something like this:

<script src="https://gist.github.com/saleguas/0fb7a1104192166bebd43242e4ff5eff.js"></script>

All the source code can be found [here](https://github.com/saleguas/Publications/tree/master/uploading-projects-to-pip/example_directory).

## Testing the package

So hopefully you made it to this point error-free, and if so, you’re basically done! Let’s test our code locally to make sure it works:

 1. First we want to move to the directory with our setup.py, in our case, this would be example_directory/.

 2. Next we will run the command python3 setup.py sdist bdist_wheel to generate our dist/ folder.

![](https://cdn-images-1.medium.com/max/2000/0*qqxC34qBvXe9Speg.gif)

Now that the package is installed, try running some of the commands:

<script src="https://gist.github.com/saleguas/c6a3d185236180a918295032a70c8199.js"></script>

And hopefully it works!

## Uploading to the test platform

This step is completely optional and can be skipped; however, if you want to know how your package would perform on the actual PyPI servers it’s a good idea to try this.

 1. First, make an account on the [test PyPI website](https://test.pypi.org/).

 2. Then run python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* to upload the files.

 3. Lastly, run python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps Example_Functional_Package where Example_Functional_Package is the name of your package.

![](https://cdn-images-1.medium.com/max/2000/0*IuXZAhAAa4mM5joY.gif)

And you can see how your package would perform on the live servers!

## Uploading to PyPI

Almost identical to the test PyPI setup but with the actual website:

 1. First, make an account on the [PyPI website](https://pypi.org/).

 2. Then run twine upload dist/* or python3 -m twine upload dist/* to upload the files.

 3. Lastly, run pip install Example_Functional_Package where Example_Functional_Package is the name of your package.

If it successfully installs, try testing the program again:

<script src="https://gist.github.com/saleguas/e314392513ec70c6d1406a2e430d15fb.js"></script>

And if all is well you should be done!

## ModuleNotFoundError

One of the most common errors I was getting, something along the lines of ModuleNotFoundError: No module named X. This is most often caused by import issues(look at the Quick Notes section) and issues in the packages field in the setup.py


**[Originally Published on Medium.com Under Analytics-Vidhya](https://medium.com/analytics-vidhya/uploading-functional-python-projects-to-pip-pypi-af73af754da0)**