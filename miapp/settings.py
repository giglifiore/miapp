DEBUG = False
ALLOWED_HOSTS = ['*']  # o mejor: ['tu-app.onrender.com']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'home',
]
ALLOWED_HOSTS = ['*']  # Esto debería estar bien, ya que permite todas las direcciones

