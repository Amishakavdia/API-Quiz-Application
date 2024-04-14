# Requests library is the popular HTTP library for making HTTP requests.
# It supports various HTTP methods, handles cookies,
# provides convenient features for working with HTTP-related tasks.
# The requests library supports various HTTP methods such as GET, POST, PUT, DELETE, etc.

import requests

#The pprint module provides a PrettyPrinter class
# used for producing more readable and visually appealing representations of complex data structures,
# especially dictionaries and lists.

from pprint import pprint

# json module is part of the standard library
# It provides functionality to encode Python objects into JSON format (serialization)
# and decode JSON data back into Python objects (deserialization).
import json

#The provided URL is an endpoint for the Open Trivia Database (OTDB) API
# which is a free-to-use API that provides trivia questions and answers.

url= "https://opentdb.com/api.php?amount=10&category=18&difficulty=hard&type=multiple"

# Requesting the url to get the data and store it into response variable
response =requests.get(url)

#print the data
print(response)

# print the data in json format
# response is a variable representing an HTTP response object,
# and it has a .json() method that returns the JSON content.
print(response.json())

#print in a more readable form
pprint(response.json())

#This line uses a with statement, which is a context manager in Python.
# It ensures that the file is properly closed after the block of code is executed.
# json.dump() is then used to serialize the JSON data and write it to the opened file (f).
# The indent=4 parameter specifies that the JSON data should be formatted with an indentation level of 4 spaces.
with open("trivia.json","w") as f:
    json.dump(response.json(),f,indent=4)
