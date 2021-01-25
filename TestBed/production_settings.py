"""
This file is the setting for the environment of IOT Component.
"""


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
CERTIFICATE_PATH_MQTT = '/home/pi/Desktop/Project/TestBed/testbed/ProtocolUtils/certificates/brokerCertificate.crt'
ALLOWED_HOSTS = ['129.6.60.38']
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

