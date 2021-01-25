"""
This file is the setting for the environment of dashboard to manage sensors and other things.
"""


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
RUN_MAIN = True
CERTIFICATE_PATH_MQTT = '/home/cpcc/Desktop/Project/TestBed/testbed/ProtocolUtils/certificates/brokerCertificate.crt'
ALLOWED_HOSTS = ['129.6.60.38', '127.0.0.1']
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testbed',
        'USER': 'postgres',
        'PASSWORD': '1qaz!QAZ1qaz',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'MIRROR': 'default'
        },
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}