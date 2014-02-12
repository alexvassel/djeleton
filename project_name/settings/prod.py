from __future__ import absolute_import
from .common import *

"""
Fill with your Sentry key
RAVEN_CONFIG = {
    'dsn': 'http://3d44150fd57244fdbd21ab19fe6bc65d:fb6f7408c07f4c93b4840fec056535b2@ekouser.linus.su/sentry/3',
}

INSTALLED_APPS + (
    # ...
    'raven.contrib.django.raven_compat',
)
"""

#These thigs for loutput in uwsgi log file
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
