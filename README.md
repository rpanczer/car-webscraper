# Flashpoint Web Scraper
This is a web scraper written in Python 3 using BeautifulSoup4 and Requests. Currently the application is capable of scraping paginated forums and like pages with minimal adjustments to a site's formatting.py file. The program will export the data into a csv file that can be used for analysis in spreadsheet programs or for upload to a database.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
To run this project, you will need to have [Python 3](https://www.python.org/downloads/), along with the packages listed in `requirements.txt` installed on your system. It is also recommended that you use a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html) to ensure both the Python version and external libraries are of the correct version needed in order to avoid versioning issues with this project or other projects that may exist on your system. 

### Installing
#### Python 3
Follow the steps on [Python.org](https://www.python.org/downloads/)  or [The Hitchhikers Guide to Python (Mac only)](https://docs.python-guide.org/starting/install3/osx/) to install python 3 on your system.

#### Virtual Environment
Once Python 3 is installed, you will need to set up a virtual environment. Follow the guide [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments) to create a virtualenv for this project.

#### Install External Packages
After navigating the to `src` directory and activating your virtual environment, you'll need to install the packages in `requirements.txt`. To do this, run:
```
pip install -r requirements.txt
```
This will install all the necessary packages in your virtualenv. You are now ready to start scraping!

### Getting Started / Demo
This program is currently configured to iterate through a forum on `http://www.oldclassiccar.co.uk` and extract data from all posts on all pages of the forum.
Extracted Data includes:
* Post ID
* Post Author
* Post Created Date
* Post Body (text entered by the author of the post) other post body info extracted is:
  * Post Images (images included by the author in their post)
  * Post Quotes (other posts quoted by the author)

To scrape `http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591` run the following code in your terminal once you're in the project's src directory:
```
python3 main.py
```
The general process of this application is as follows:
* start by running `main` to set the url, and to determine whether to create a bs4 object out of the current page or, if no posts remain, print the extracted post objects into the `threads.csv` file.
* if `main` determines the target url may have posts, `make_soup` is run. This function contacts the target url, returns the html if successful or an error if there is a network issue. The returned html is then parsed into a BeautifulSoup object and passed to the `create_post_objects` function.
* `create_post_objects` is a site specific function used to scrape the posts on the target site and turn them into dictionary objects using functions found in the project specific `formatting.py` and `extracts.py`(more details on these files can be found below), with each key storing one data type. After all post objects are created and stored in a list, the list of posts is returned back to `main`. If this list of posts has a length, the scraper will try to iterate to the next page of the forum. If the returned list contains no post objects, `main` calls `write_posts_to_csv` and passes in the list of post objects.
* `write_posts_to_csv` creates a csv file called `threads.csv` and a csv writer. The csv writer iterates through the list of post objects, formatting them into strings and writing them to the csv.

#### Design of extracts py
Holds basic functions that can be used to scrape data from a wide variety of sites. Each function in this file should be general enough to be reused.

#### Design of formatting project_name py
Holds specific functions to scrape a particular piece of data from a site. Think of these functions as custom to a site's particular structure you want to scrape. Each of these functions may or may not make use of one or more functions in extracts.py.

## Running Tests
To run automated tests for this program, open terminal and navigate to the src directory. From there, simply run the 
desired test file with:
```
python3 [test_file].py
```

Current test_files are:
* [test_extracts.py] - Tests functionality of the functions in extracts.py
* [test_formatting_classic_car.py] - Tests functionality of some of the functions in formatting_classic_car.py

## Built With

* [Requests](http://docs.python-requests.org/en/master/) - A simple HTTP library for Python
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - A Python library for pulling data out of HTML and XML files
* [CSV](https://docs.python.org/3/library/csv.html) - Python's CSV library, since CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases
