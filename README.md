# flaskWebsite

development notes:

Create and activate your Python environment and install Flask

$ python3 -m venv pyenv
$ source pyenv/bin/activate
$ pip install flask
verify installation:
$ python -c "import flask; print(flask.__version__)"

run:
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run