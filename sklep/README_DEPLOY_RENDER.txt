Render deployment settings:

Build command:
./build.sh

Start command:
gunicorn Sklep.wsgi:application

Recommended environment variables:
SECRET_KEY=<your-secret-key>
DEBUG=False
ALLOWED_HOSTS=.onrender.com
CSRF_TRUSTED_ORIGINS=https://<twoj-serwis>.onrender.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
