# shopify_developer_challenge

# Overview

This application allows users to upload individual image files, which are stored in a sqlite database. The stored images can be retrieved by image id. 

</br>

# Getting Started

## Dependencies

- requests
- flask
- flask-sqlalchemy
- flask-restful
- python
- pytest

## Running Locally
- Run pipenv:
  - pipenv install
  - pipenv shell 
- In terminal run the following:
  - EXPORT FLASK_APP=application
  - EXPORT FLASK_ENV=development
  - flask run
- To upload an image use '/upload' at end of main route (e.g. http://127.0.0.1:5000/upload)
- To retrieve an image from the sqlite database use '/<id>' at end of main route (e.g. http://127.0.0.1:5000/1)
- Can also run unit tests by running 'pytest' in either a new terminal or closing the application in current terminal

</br>  

# Next Steps
There is much room for improvement for this application.

In expanding the the functionality of adding images:
- Allow for multiple images to be added at once

In particular, the development of search functions based on:
- Characteristics of the image (e.g. tags)
- Text (e.g. allow for naming images)
- Another image (e.g. machine learning model)

Continuing to build more unit tests, specifically in regards to the aspects of uploading and storing image files.
