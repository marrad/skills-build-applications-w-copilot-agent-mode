from pathlib import Path

# ...existing code...

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': '127.0.0.1',
        'PORT': 27017,
    }
}

# Enable CORS
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']