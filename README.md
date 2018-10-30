# Flashpoint Web Scraper

This is a web scraper written in Python 3 using BeautifulSoup4 and Requests. Currently the application is capable of scraping paginated forums and like pages with minimal adjustments to a site's formatting.py file. The program will export the data into a csv file that can be used for analysis in spreadsheet programs or for upload to a database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you will need to have [Python 3](https://www.python.org/downloads/), along with the packages listed in `requirements.txt` installed on your system. It is also recommended that you use a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html) to ensure both the Python version and external libraries are of the correct version needed in order to avoid versioning issues with this project or other projects that may exist on your system. 

### Installing
#### Python 3
A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```
#### Virtual Environment

#### Install External Packages

### Demo / Getting Started
End with an example of getting some data out of the system or using it for a little demo

## Project Structure

### main.py

### extracts.py

### formatting_project_name.py

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
