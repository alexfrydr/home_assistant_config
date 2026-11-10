# -*- coding: utf-8 -*-
SECRET_KEY = "fy)x@x$1i5h0ri12n7o$m*gfsixvyh2qxb^zt%vro0r#zgv)!y"
SERVICE_URL = "http://90.188.250.248:8000"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'seafile',
        'PASSWORD': 'f750bd3a-5331-4483-8dda-aa26bbfdd1c7',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'
TIME_ZONE = 'Asia/Irkutsk'
FILE_SERVER_ROOT = "http://90.188.250.248:8000/seafhttp"

# >>> HA add-on managed block >>>
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/seafile-cache',
        'TIMEOUT': 3600,
    },
}
FILE_SERVER_ROOT = '/mnt/sda/seafile_1'
# <<< HA add-on managed block <<<
