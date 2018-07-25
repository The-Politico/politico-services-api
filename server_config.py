#!/usr/bin/env python

"""
Project-wide application configuration.
DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
See get_secrets() below for a fast way to access them.
"""

import logging

"""
NAMES
"""

###################################
# FILL THIS OUT
###################################
# Project name to be used in urls
# Use dashes, not underscores!
PROJECT_SLUG = 'politico-services-api'

# Django project name to be used in file paths. Cannot have dashes.
PROJECT_FILENAME = 'politicoservicesapi'

# The name of the repository containing the source
REPOSITORY_NAME = 'politico-services-api'

PRODUCTION_SERVERS = ['services.politicoapps.com']
STAGING_SERVERS = ['staging.services.politicoapps.com']

##################################
# GENERATED, LEAVE THIS STUFF
##################################

GITHUB_USERNAME = 'The-Politico'
REPOSITORY_URL = 'https://github.com/{0}/{1}'.format(
    GITHUB_USERNAME, REPOSITORY_NAME
)

SERVER_USER = 'ubuntu'
SERVER_PYTHON = 'python3'
SERVER_PROJECT_PATH = '/home/%s/apps/%s' % (SERVER_USER, REPOSITORY_NAME)
SERVER_REPOSITORY_PATH = '%s/repository' % SERVER_PROJECT_PATH
SERVER_VIRTUALENV_PATH = '%s/virtualenv' % SERVER_PROJECT_PATH
UWSGI_SOCKET_PATH = '/run/uwsgi/%s.uwsgi.sock' % PROJECT_FILENAME

# Services are the server-side services we want to enable and configure.
# A three-tuple following this format:
# (service name, service deployment path, service config file extension)
SERVER_SERVICES = [
    ('app', '/etc/uwsgi/sites', 'ini'),
    ('uwsgi', '/etc/init', 'conf'),
    ('nginx', '/etc/nginx/sites-available', 'conf'),
    ('celery', '/etc/init', 'conf')
]

"""
Logging
"""
LOG_FORMAT = '%(levelname)s:%(name)s:%(asctime)s: %(message)s'
SERVER_LOG_PATH = '/var/log/%s' % PROJECT_FILENAME
LOG_LEVEL = logging.DEBUG
