from pathlib import Path
import os



BASE_DIR = Path(__file__).resolve().parent.parent


# Define BASE_DIR if not already defined
BASE_DIR = Path(__file__).resolve().parent.parent

# Authentication Settings
LOGIN_URL = '/registration/login/'
LOGIN_REDIRECT_URL = '/registration/dashboard/'  # Redirect after login
LOGOUT_REDIRECT_URL = '/registration/login/'  # Redirect after logout

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'accounts.backends.NTTFEmailBackend',  # Custom authentication backend
    'django.contrib.auth.backends.ModelBackend',  # Default Django backend
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # Ensure this is listed
]

# Template Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Global templates folder
            BASE_DIR / 'registration' / 'templates',  # App-specific templates
        ],
        'APP_DIRS': True,  # Enables loading templates from installed apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static and Media Files (Ensure proper handling of static and media)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]