from os.path import abspath, dirname, basename, join


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_PATH = abspath(dirname(__file__))
PROJECT_NAME = basename(ROOT_PATH)

ADMINS = (
    #('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'site/test.db',
        }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
ADMIN_MEDIA_PREFIX = '/admin-media/'
MEDIA_URL = ''

SECRET_KEY = 't2eo^kd%k+-##ml3@_x__$j0(ps4p0q6eg*c4ttp9d2n(t!iol'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    join(ROOT_PATH, 'templates')
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'akamaru',
    'akamaru_demo',
    )

AUTHENTICATION_BACKENDS = (
    'akamaru.backends.facebook.FacebookBackend',
    'akamaru.backends.vkontakte.VkontakteBackend',
    'akamaru.backends.google.GoogleBackend',
    'akamaru.backends.trello.TrelloBackend',

    'django.contrib.auth.backends.ModelBackend',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    )

LOGIN_REDIRECT_URL = '/'

FACEBOOK_APP_ID = ""
FACEBOOK_SECRET = ""

VKONTAKTE_APP_ID = ''
VKONTAKTE_SECRET = ''

TRELLO_API_KEY = ''
TRELLO_TOKEN = ''

GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''

AKAMARU_LOGIN_OK = "profile"
AKAMARU_LOGIN_ERROR = "login-error"
AKAMARU_RESOLVE_FORM = "resolve"
