# django middlewares context processors example

## Demo app created for Python Cali session - July 15 2023

### How to run this project

- Clone the repo
- Run `python manage.py runserver` and go to `http://localhost:8000/`
- Go to `app/settings.py` and uncomment line 51
- Go to `http://localhost:8000/` and check what happens.
- You may check the middleware blocking the request in `demo/middlewares.py`
- Comment line 51 and uncomment line 67
- Go to `http://localhost:8000/` and check what's different
- You may check the context processor adding the new text in `demo/context_processors.py`