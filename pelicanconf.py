# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Marvin Steadfast'
SITENAME = 'xsteadfastx'
SITEURL = ''
AVATAR = '/theme/images/avatar.png'
TIMEZONE = "Europe/Berlin"
DESCRIPTION = "the cats are not what they seem"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/xsteadfastx/'
TWITTER_NAME = 'xsteadfastx'
DISQUS_SITENAME = "xsteadfastx"
#ISSO_URL = 'http://comments.xsteadfastx.org'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 50
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ATOM = 'feed/index.html'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# path-specific metadata
EXTRA_PATH_METADATA = {
    #'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    #'extra/robots.txt',
    'extra/CNAME',
    #'code',
    #'notebooks'
    ]

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
#foobar = "barbaz"

THEME = 'themes/xsteadfastx-greg'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.youtube', 'liquid_tags.notebook', 'liquid_tags.vimeo']

#CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read()

LOAD_CONTENT_CACHE = False
