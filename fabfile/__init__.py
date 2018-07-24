import copy
import os
import shutil
import server_config

from fabric.api import task
from fabric.state import env
from jinja2 import Template
from subprocess import run
from . import django, servers

"""
Base configuration
"""
env.user = server_config.SERVER_USER
env.forward_agent = True

"""
Branches

Changing branches requires deploying that branch to a host.
"""


@task
def production():
    env.hosts = server_config.PRODUCTION_SERVERS


@task
def staging():
    env.hosts = server_config.STAGING_SERVERS


@task
def master():
    """
    Work on development branch.
    """
    env.branch = 'master'


@task
def branch(branch_name):
    """
    Work on any specified branch.
    """
    env.branch = branch_name


@task
def deploy_server():
    servers.checkout_latest()
    servers.restart_service('uwsgi')


@task
def bootstrap():
    run(['django-admin', 'startproject', server_config.PROJECT_FILENAME, '.'])

    context = copy.copy(server_config.__dict__)
    template_files = [
        '_setup.py',
        'terraform/staging/_main.tf',
        'terraform/production/_main.tf',
        'terraform/scripts/_deploy.sh',
        'terraform/scripts/_postdeploy.sh'
    ]

    for file_path in template_files:
        with open(file_path) as read_template:
            write_path = file_path.replace('_', '')
            with open(write_path, 'w') as write_template:
                payload = Template(read_template.read())
                write_template.write(payload.render(**context))

        os.remove(file_path)

    shutil.rmtree('.git')
    run(['git', 'init'])
