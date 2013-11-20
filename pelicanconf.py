#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jacobo de Vera'
SITENAME = u'Jacobo de Vera'
SITESUBTITLE = u'The Blog'
SITEURL = u'http://blog.jacobodevera.com'
SITEURL = ''

TWITTER_USERNAME=u'jovianjake'
# GITHUB_URL='https://github.com/jdevera/dotfiles'

TIMEZONE = u'Europe/Dublin'

DEFAULT_LANG = u'en'

DATE_FORMATS = {
        'es' : '%A, %d de %B de %Y',
        'en' : '%A, %d %B %Y',
        }
PATH='content/'
DEFAULT_DATE='fs'
USE_FOLDER_AS_CATEGORY=False
DEFAULT_CATEGORY='Other'
DISPLAY_CATEGORIES_ON_MENU=False
PATH_METADATA=r'(?P<date>\d{4}/\d{2}/\d{2})-.*'
OUTPUT_SOURCES=True

ARTICLE_URL='{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS='{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL='{date:%Y}/{date:%m}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS='{date:%Y}/{date:%m}/{slug}-{lang}/index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
AUTHORS_SAVE_AS = False

STATIC_SAVE_AS = '{path}'
STATIC_URL = '{path}'

DISQUS_SITENAME = 'jacobodevera'
GOOGLE_ANALYTICS = 'UA-11921622-2'

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    ]

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }


# If disabled, content with dates in the future will get a de fault status of draft.
WITH_FUTURE_DATES=False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)
LINKS=None

# Social widget
SOCIAL = (('My code on Github', 'https://github.com/jdevera'),
        ('My LinkedIn profile', 'http://www.linkedin.com/in/jdevera'),
        ('My Twitter stream', 'http://twitter.com/#!/jovianjake'),
        )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('rst', 'md', 'markdown', 'mkd', 'mdown', 'html', 'htm')
TYPOGRIFY=True
