# from fabric.api import *
from __future__ import print_function
from fabric import api as fab
import fabric.contrib.project as project
import os
from datetime import date
from unidecode import unidecode
import string
import textwrap

# Local path configuration (can be absolute or relative to fabfile)
fab.env.deploy_path = 'output'
DEPLOY_PATH = fab.env.deploy_path

# Remote server configuration
production = 'jdevera@jacobodevera.com:22'
dest_path = '/home/jdevera/www/blog.jacobodevera.com'

# Rackspace Cloud Files configuration settings
fab.env.cloudfiles_username = 'my_rackspace_username'
fab.env.cloudfiles_api_key = 'my_rackspace_api_key'
fab.env.cloudfiles_container = 'my_cloudfiles_container'

@fab.task(alias='new')
def new_article(title=None, format='rst'):
    """
    Creates a new article
    """

    def get_date(format='%Y%m%d'):
        return date.today().strftime(format)

    def make_slug(s):
        sl = []
        s = unidecode('-'.join(s.split()))
        passthrough = string.ascii_lowercase + string.digits + '-'
        for c in s.lower():
            if c in passthrough:
                sl.append(c)
            elif c not in string.punctuation:
                sl.append('#')
        return "".join(sl)

    if title is None:
        title = raw_input("Enter title:")
    words = unicode(" ".join(title.split()), "UTF-8")
    slug = make_slug(words)
    filename = u"{}.{}".format(slug, format)
    dir_path = os.path.join('content', 'articles', get_date("%Y"), get_date("%m"))
    file_path = os.path.join(dir_path, filename)
    contents = None
    if format == 'rst':
        contents = textwrap.dedent(u"""\
                {}
                {}

                :date: {}
                :status: draft

                """).format(title, "=" * len(title), get_date("%Y-%m-%d"))
    elif format in ('md', 'mkd', 'markdown'):
        contents = textwrap.dedent(u"""\
                Title: {}
                Date: {}
                Status: draft

                """).format(title, get_date("%Y-%m-%d"))

    if contents is not None:
        if not os.path.exists(dir_path):
            print('Creating directory {}'.format(dir_path))
            os.makedirs(dir_path)
        with open(file_path, 'w') as f:
            f.write(contents.encode('utf-8'))
    print("New article: {}".format(file_path))


@fab.task
def clean():
    if os.path.isdir(DEPLOY_PATH):
        fab.local('rm -rf {deploy_path}'.format(**fab.env))
        fab.local('mkdir {deploy_path}'.format(**fab.env))

@fab.task
def cleanpyc():
    fab.local("find -name '*.pyc' -delete")

@fab.task
def build():
    fab.local('pelican -s pelicanconf.py')

@fab.task
def rebuild():
    clean()
    build()

@fab.task
def regenerate():
    fab.local('pelican -r -s pelicanconf.py')

@fab.task
def serve():
    fab.local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**fab.env))

@fab.task
def reserve():
    build()
    serve()

@fab.task
def preview():
    fab.local('pelican -s publishconf.py')

@fab.hosts(production)
@fab.task
def publish():
    fab.local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
