# cherrypy-playground
Playing around with CherryPy


## Local Development

### Python Virtual Environment

It's nice to have a clean virtual environment in Python. 
To _create_ one, you can just run the following: `python -m venv {PATH_TO_VENV}`
To _use_ one, you need to `source` it: `source {PATH_TO_VENV}/bin/activate`

### Install Python Requirements

Run `pip install -r requirements.txt`

## Docker

### Building the container

Running the following will build the Docker container: `docker build -t cherrypy .`

### Running the container

Running the following will _run_ the Docker container: `docker run -p 8080:8080 cherrypy`