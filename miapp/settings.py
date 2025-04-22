DEBUG = True
ALLOWED_HOSTS = ['*']  # o mejor: ['tu-app.onrender.com']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
