#!/bin/bash
. ~/.bash_profile
pyenv global 3.6.4
mkdir -p apps/
cd apps
git clone https://github.com/The-Politico/politico-services-api
cd politico-services-api
pip install -r requirements.txt
