import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + "logs/debug.log"
        },
    },
    'loggers': {
        'UrlShortener': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}