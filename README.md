# hippercampus_py_be

#### Virtual environment
```
$ . venv/bin/activate
```

#### Run

With `python`:
```
export FLASK_ENV=development
export FLASK_APP=hc.py
$ python -m flask run --host=127.0.0.1 --port=3003
```

With `flask`:
```
$ export FLASK_APP=my_application
$ export FLASK_ENV=development
$ flask run --port=3003
```