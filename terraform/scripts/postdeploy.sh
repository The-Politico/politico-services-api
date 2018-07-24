#!/bin/bash
. ~/.bash_profile
pyenv global 3.6.4
cd apps/politico-services-api
python manage.py migrate
