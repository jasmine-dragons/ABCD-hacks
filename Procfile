web: gunicorn gettingstarted.wsgi --log-file -
heroku ps:scale web=1
worker: python app.py
