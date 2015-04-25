#Django Heroku

post = get_object_or_404(Blog, pk=1) # instead of Blog.objects.get(pk=1)


# Procfile
web: gunicon blogit.wsgi -b 0.0.0.0:$PORT -w 4 -k gevent # for Heroku


# WSGI.py
application = get_wsgi_application()
application = Cling(application)

# settings.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

# Databases
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Read 12 Factor app