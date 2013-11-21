# from fabric.api import *
from fabric import api as fab
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
fab.env.deploy_path = 'output'
DEPLOY_PATH = fab.env.deploy_path

# Remote server configuration
production = 'jdevera@jacobodevera.com:22'
dest_path = '/home/jdevera/www/staging.jacobodevera.com'

# Rackspace Cloud Files configuration settings
fab.env.cloudfiles_username = 'my_rackspace_username'
fab.env.cloudfiles_api_key = 'my_rackspace_api_key'
fab.env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        fab.local('rm -rf {deploy_path}'.format(**fab.env))
        fab.local('mkdir {deploy_path}'.format(**fab.env))

def cleanpyc():
    fab.local("find -name '*.pyc' -delete")

def build():
    fab.local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    fab.local('pelican -r -s pelicanconf.py')

def serve():
    fab.local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**fab.env))

def reserve():
    build()
    serve()

def preview():
    fab.local('pelican -s publishconf.py')

@fab.hosts(production)
def publish():
    fab.local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
