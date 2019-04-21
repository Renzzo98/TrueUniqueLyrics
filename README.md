# ANTI-DUPLICATE LYRICS

An Python Script that searches the lyrics of any song, and remove any duplicate lyrics afer it had
appeared once already.

### Features

* Works with most popular songs
* Display "____" where the lyrics got cut out
* Display how much of the lyrics were repeated and cut (% meter)

## Getting Started

This script requires very little prerequisites for it work correctly. Once everything is set up and ready, simply follow the instructions and see the results. 

*Note: Ver1.0 only work on Macs (Further Support may be coming soon)*

### Prerequisites

An MacOS device is required to run the script properly due to the system commands used to output the results efficently

Here are things you need to install the software and how to install them
* Python 2.7 / 3.0
* Beautiful Soup 4
* Selenium 2.0

**An Constant and Steady Internet Connection is required to run the scirpt**

### Installing


**Python:<br />**
Python will be used for reading the script. Installing python 2.7 or 3 is recommended as an older verison of python will be outdated and required further steps.

On Mac:
```
sudo easy_install pip
```
*Note: Most Modern Mac System will come with Python and PIP already installed. However, if you have a outdated verison of Python, you may wish to continue to avoid preventable errors.*

From this moment on, if you correctly installed python 2.7 or 3, you will be have the python package manager, PIP, as it comes with the lastest version of Python. This will allow you to use the PIP command to install the remaining packages needed.

To check your python verison:
```
python --version
```
If you get a version number(e.g. "Python 2.7.5"), then it means Python is good to go

**Beautiful Soup 4 Python:<br />**
Beautiful Soup is a Python library for pulling data out of HTML and XML files. 

```
pip install beautifulsoup4
```

**Selenium:<br />**
Selenium is an Web Driver that allows you automate the use of your web application, including your browser

```
sudo easy_install selenium
```
*Note: easy_install package manager comes pre-installed with most MacOS systems*

### Running the Script

Once everything is installed, no further installation is required. 
Simply run the python script in the directory, and following the on-screen directions.

To run the python script:
```
python Anti-Duplicate.py
```


## Built With

* [Python](https://www.python.org) - The Scripting Language used
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used to prase the website and collect the key elements of the site markup
* [Selenium Web Driver](https://www.seleniumhq.org/projects/webdriver/) - Used to prase and run the website needed to collect the lyrics for the song requested


## Authors

* **Hugo Renzzo Olcese** - *All of the work* - [Renzzo98](https://github.com/Renzzo98?tab=repositories)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspiration
* etc


## Roadmap

- Fix the following bugs:
  - [ ] An Simple issue where the word "The" in the band name will cause it to fail
  - [ ] Doesn't work with weird songs like **Crazy Frog**

- Apply the script to a website


