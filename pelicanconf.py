#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'MarcDufresne'
SITENAME = u'MarcDufresne\'s DevOps Blog'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'

THEME = 'm0rk-theme'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Blogroll
LINKS = (
    ('GitHub', 'https://github.com/MarcDufresne'),
    ('Privacy Policy', '/pages/privacy-policy/'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

GOOGLE_ANALYTICS = "UA-49795505-2"

MEDIUS_AUTHORS = {
    "MarcDufresne": {
        "image": "https://avatars0.githubusercontent.com/u/599102?s=120&v=4",
        "links": (
            ("github", "https://github.com/MarcDufresne"),
        )
    }
}

MEDIUS_CATEGORIES = {
    "Kubernetes": {
        "description": "Guides about Kubernetes",
        "logo": "https://github.com/MarcDufresne/m0rk-blog/raw/master/"
                "m0rk-theme/static/img/categories/kubernetes_logo_border.png",
        "thumbnail": "https://github.com/MarcDufresne/m0rk-blog/raw/master/"
                     "m0rk-theme/static/img/categories/kubernetes_logo_border.png"
    },
    "Python": {
        "description": "Guides about Python and related tools",
        "logo": "https://github.com/MarcDufresne/m0rk-blog/raw/master/"
                "m0rk-theme/static/img/categories/python_logo.png",
        "thumbnail": "https://github.com/MarcDufresne/m0rk-blog/raw/master/"
                     "m0rk-theme/static/img/categories/python_logo.png"
    }
}
