"""
This file is the setting for the environment of development.
"""


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
RUN_MAIN = False
ALLOWED_HOSTS = []
CERTIFICATE_PATH_MQTT = 'C:/Users/bnb3/Documents/Work/Project/TestBed/ProtocolUtils/certificates/brokerCertificate.crt'
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testbed',
        'USER': 'postgres',
        'PASSWORD': '1qaz!QAZ1qaz',
        'HOST': '129.6.60.38',
        'PORT': '5432',
        'TEST': {
            'MIRROR': 'default'
        },
    }
}
