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
        'NAME': 'test.db',
        }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = True
USE_L10N = True

STATIC_URL = '/static/'
STATIC_ROOT= ''

MEDIA_ROOT = ''
ADMIN_MEDIA_PREFIX = '/admin-media/'
MEDIA_URL = '/media/'

SECRET_KEY = 't2eo^kd%k+-##ml3@_x__$j0(ps4p0q6eg*c4ttp9d2n(t!iol'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
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
    'django.contrib.staticfiles',

    'akamaru',
    'akamaru.contrib.resolve',
    'akamaru.contrib.kiba',
    'demo'
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
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    )

LOGIN_REDIRECT_URL = '/'

FACEBOOK_APP_ID = "170958219629605"
FACEBOOK_SECRET = "94c30c5265072b5bdf82174125c2d6f9"

VKONTAKTE_APP_ID = '2642738'
VKONTAKTE_SECRET = 'oKJ4yoTybg6qoqugUMeY'

TRELLO_API_KEY = '728a6bb4aa0911f0698ca28860c92ad0'
TRELLO_TOKEN = '73c37c2ad45f56c37aeb00df4c1fa9bcddf1babff1f92507c4442c01e1e9e170'

GOOGLE_CONSUMER_KEY = 'anonymous'
GOOGLE_CONSUMER_SECRET = 'anonymous'

GOOGLE_CLIENT_ID = '1018162325150.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'TE7bE_kGqoDZ4HXyccohb6kC'

AKAMARU_RESOLVE_FORM = 'akamaru-resolve'
AKAMARU_LOGIN_OK = 'profile'

try:
    from local_settings import *
except:
    pass
